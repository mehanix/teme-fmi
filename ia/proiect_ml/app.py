
import numpy as np
import tensorflow as tf
from tensorflow import keras
import math
import matplotlib.pyplot as plt
from datetime import datetime
from tensorflow.keras import layers
from tensorflow.python.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
import cv2
physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)
def grayscale(image_label, seed):
    image, label = image_label
    grayscaled = tf.image.rgb_to_grayscale(image)
    return grayscaled, label
config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

import pandas as pd
class_names=['native','arterial','venous']

class convnet:
    shape = (50,50,3)
    batchSize = 32
    nrTraining = 15000
    nrValid = 4500
    nrEpochs = 20

    model = tf.keras.Sequential([
        layers.experimental.preprocessing.Rescaling(1./255),
        layers.experimental.preprocessing.RandomTranslation(width_factor=(-0.15,0.15),height_factor=(-0.15,0.15)),
        layers.experimental.preprocessing.RandomContrast(0.2),
        
        layers.Conv2D(64, 3, activation='relu'),
        layers.BatchNormalization(),
        layers.MaxPooling2D(),
        layers.BatchNormalization(),
        layers.Dropout(0.3),
        
        layers.Conv2D(128, 3, activation='relu'),
        layers.BatchNormalization(),
        layers.MaxPooling2D(),
        layers.BatchNormalization(),
        layers.Dropout(0.3),
        
        layers.Conv2D(128, 3, activation='relu'),
        layers.BatchNormalization(),
        layers.MaxPooling2D(),
        layers.BatchNormalization(),
        layers.Dropout(0.3),

        layers.Conv2D(256, 3, activation='relu'),
        layers.BatchNormalization(),
        layers.MaxPooling2D(),
        layers.BatchNormalization(),
        layers.Dropout(0.3),
        layers.Flatten(),
        
        layers.Dense(1024, activation='relu'),
        layers.BatchNormalization(),
        layers.Dropout(0.3),
        layers.Dense(3, activation='softmax')
        ])

    @classmethod
    def compileazaModel(cls):
        cls.model.compile(optimizer="adam",
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])

    @classmethod
    def fit(cls,dataset_train,dataset_valid):
        print(f'nrTraining{cls.nrTraining}, batchSize{cls.batchSize}, stepsperepoch {cls.nrTraining//cls.batchSize}')
        checkpoint = ModelCheckpoint('model_checkpoint.h5', monitor='val_accuracy', mode='max', verbose=1, save_best_only=True)
        earlyStopping = EarlyStopping(monitor='val_loss', mode='min', verbose=1,patience=5)
        history = cls.model.fit(
            dataset_train,
            steps_per_epoch=cls.nrTraining//cls.batchSize,
            epochs=cls.nrEpochs,
            validation_data=dataset_valid,
            validation_steps=cls.nrValid//cls.batchSize,
            callbacks=[earlyStopping, checkpoint]
        )
        timestamp  = datetime.now().strftime("%d-%m-%Y-%H:%M:%S")
        cls.model.save(f'model_{timestamp}.h5')
        return history

    @classmethod
    def visualize(cls,history):
        acc = history.history['accuracy']
        val_acc = history.history['val_accuracy']

        loss = history.history['loss']
        val_loss = history.history['val_loss']

        epochs_range = range(cls.nrEpochs)

        plt.figure(figsize=(16, 16))
        plt.subplot(1, 2, 1)
        plt.plot(epochs_range, acc, label='Training Accuracy')
        plt.plot(epochs_range, val_acc, label='Validation Accuracy')
        plt.legend(loc='lower right')
        plt.title('Training and Validation Accuracy')

        plt.subplot(1, 2, 2)
        plt.plot(epochs_range, loss, label='Training Loss')
        plt.plot(epochs_range, val_loss, label='Validation Loss')
        plt.legend(loc='upper right')
        plt.title('Training and Validation Loss')
        plt.show()

    @classmethod
    def train(cls):
            
        train_ds = tf.keras.preprocessing.image_dataset_from_directory(
                    'train',
                    image_size=(50, 50),
                    batch_size=convnet.batchSize,
                    color_mode="grayscale")

        train_va = tf.keras.preprocessing.image_dataset_from_directory(
                    'validation',
                    image_size=(50, 50),
                    batch_size=convnet.batchSize,
                    color_mode="grayscale")

        print("size",tf.data.experimental.cardinality(train_ds))
        # input()
        plt.figure(figsize=(10, 10))
        for images, labels in train_ds.take(1):
            for i in range(convnet.batchSize):
                ax = plt.subplot(math.ceil(math.sqrt(convnet.batchSize)),math.ceil(math.sqrt(convnet.batchSize)), i + 1)
                plt.imshow(images[i].numpy().astype("uint8"))
                plt.title(class_names[labels[i]])
                plt.axis("off")
        # plt.show()
        AUTOTUNE = tf.data.AUTOTUNE

        # counter = tf.data.experimental.Counter()
        # train_ds = tf.data.Dataset.zip((train_ds, (counter, counter)))
        # train_ds = ( train_ds.map(grayscale,num_parallel_calls=AUTOTUNE) )
        # train_ds = train_ds.reshape(15000, 50, 50, 1)

        # train_va = tf.data.Dataset.zip((train_va, (counter, counter)))
        # train_va = ( train_va.map(grayscale,num_parallel_calls=AUTOTUNE) )

        train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
        train_va = train_va.cache().prefetch(buffer_size=AUTOTUNE)
        train_ds = train_ds.repeat()
        train_va = train_va.repeat()

        convnet.compileazaModel()
        history = convnet.fit(train_ds, train_va)

        convnet.visualize(history)
    
    

    @classmethod
    def test(cls,path):
        

        datagen = keras.preprocessing.image.ImageDataGenerator()

        tests = datagen.flow_from_directory(
            './test_folder/',

            class_mode=None,
            batch_size=1,
            shuffle=False,
            target_size=(50,50),
            color_mode="grayscale"

        )

        # files = []
        # for file in glob.glob("validation/*.png"):
        #     file = file.split('/')
        #     files.append(file[1])
        # print(files[0])
        STEP_SIZE_TEST=tests.n//tests.batch_size
        tests.reset()
    
        mod = keras.models.load_model(path,compile = True)
        mod.summary()
        pred = mod.predict_generator(tests, steps=STEP_SIZE_TEST, verbose=1)
        # pred = mod.predict(tests)
        predictions=np.argmax(pred,axis=1)

        filenames=tests.filenames
        results=pd.DataFrame({"Filename":filenames,
                            "Predictions":predictions})
        results.to_csv("results7.csv",index=False)


        # with open("results.txt",'w') as r:
        #     for (name,clas) in zip(tests.filenames,classification):
        #         name = name.split('/')[1]
        #         r.write(f"{name},{np.argmax(clas)}\n")
                
        # i=0
        # with open("results.txt",'w') as r:
        #     for c in classification:
        #         print(files[i], np.argmax(c))
        #         i+=1
        #         p = files[i]
        #         rasp = str(np.argmax(c))
        #         s = p + "," + rasp + '\n'
                
        #         r.write(s)
        #         i+=1
        # print(img)
        # tests = tf.data.Dataset.from_tensor_slices((files));
        # tests = tests.map(_getPic)
        # model.predict(tests)

    @staticmethod
    def VisualizeModel():
        img = cv2.imread('../input/ct-fixed-dataset/fixed-dataset/train/00075648-2e8.png')
        plt.imshow(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        plt.imshow(img)
        model = Sequential(layers=[
            Conv2D(filters=1, kernel_size=2, strides=1, activation='relu', input_shape=(50, 50, 1)),
            Conv2D(filters=1, kernel_size=2, strides=1, activation='relu'),
            BatchNormalization(),
            AveragePooling2D(),
#             MaxPooling2D(),
            BatchNormalization(),
            
            Conv2D(filters=1, kernel_size=3, strides=1, activation='relu'),
            Conv2D(filters=1, kernel_size=2, strides=1, activation='relu'),
            BatchNormalization(),
            MaxPooling2D(),
            
            Conv2D(filters=1, kernel_size=3, strides=1, activation='relu'),
#             MaxPooling2D(),
            BatchNormalization(),
#             Dropout(0.35),
            
#             Conv2D(filters=128, kernel_size=3, strides=1, activation='relu'),
#             MaxPooling2D(),
#             BatchNormalization(),
# #             Dropout(0.35),
            
#             Flatten(),
#             Dense(256, activation='relu'),
#             BatchNormalization(),
#             Dropout(0.1),
#             Dense(128, activation='relu'),
#             BatchNormalization(),
#             Dropout(0.1),
#             Dense(3, activation='softmax')         
        ], name='SolidCNN')
        
        batch = img.reshape(-1, 50, 50, 1)
        conv_img = model.predict(batch)
        print(conv_img.shape)
        conv_img = np.squeeze(conv_img, axis=0)
        conv_img = conv_img.reshape(conv_img.shape[:2])
        print(conv_img.shape)
        plt.imshow(conv_img)

def main():

    # datagen = keras.preprocessing.image.ImageDataGenerator(
    #     rotation_range=17,
    #     width_shift_range=(-0.05,0.05),
    #     height_shift_range=(-0.05,0.05),
    #     # brightness_range=(-0.2,0.2)
    # )

    # tests = datagen.flow_from_directory(
    #     './test_folder/',

    #     class_mode=None,
    #     batch_size=1,
    #     shuffle=False,
    #     target_size=(50,50),
    #     color_mode="grayscale",
    #     save_to_dir="./modified",
    #     save_prefix="",
    #     save_format="png",

    # )
  
    # STEP_SIZE_TEST=tests.n//tests.batch_size
    # tests.reset()

    # mod = keras.models.load_model("model 86.h5",compile = True)
    # mod.summary()
    # pred = mod.predict_generator(tests, steps=STEP_SIZE_TEST, verbose=1)
    # normalization_layer = tf.keras.layers.experimental.preprocessing.Rescaling(1./255)
    # normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
    # normalized_va = train_va.map(lambda x, y: (normalization_layer(x), y))

    # convnet.train()
    convnet.test("acc0.87-loss0.36-lrelu.hdf5")

    # img = cv2.imread('train/0/ff84a3dd-f45.png')
    # plt.imshow(img)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # batch = img.reshape(-1, 50, 50, 1)
    # layer = layers.RandomTranslation(width_factor=(-0.15,0.15), height_factor=(-0.15,0.15))
    # conv_img = layer(batch, training=True)
    # layer = layers.RandomContrast(0.7)
    # conv_img = layer(conv_img, training=True)
    # print(conv_img.shape)
    # conv_img = np.squeeze(conv_img, axis=0)
    # conv_img = conv_img.reshape(conv_img.shape[:2])
    # print(conv_img.shape)
    # plt.imshow(conv_img)


if __name__ =="__main__":
    main()