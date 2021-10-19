import numpy as np
from datetime import datetime
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.python.keras.callbacks import ModelCheckpoint
import pandas as pd

class convnet:

    # Parametri reglabili
    pathTrain = '/kaggle/input/ml-dtset/train'
    pathValid = '/kaggle/input/ml-dtset/validation'
    pathTests = '/kaggle/input/ml-dtset/test_folder/'
    
    batchSize = 16
    nrEpochs = 250
    
    # Modelul in sine
    model = keras.Sequential([
        # Rescaling -> normalizare de la [0,255] la [0,1] - float
        layers.experimental.preprocessing.Rescaling(1./255),
        
        # Data augumentation -> am observat diferente de contrast si centrare in imaginile din dataset
        # asa ca am extins datele cu variante cu contrast diferit / descentrate putin
        # rezultat: performanta mai buna si overfit mai putin
        layers.experimental.preprocessing.RandomTranslation(width_factor=(-0.15,0.15),height_factor=(-0.15,0.15)),
        layers.experimental.preprocessing.RandomContrast(0.2),
        
        # 4 straturi de convolutie pentru extragerea feature-urilor relevante din imagini
        # maxpooling -> downsampling
        # regularizare prin dropout pentru a preveni overfit-ul
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
        
        # layer de clasificare
        layers.Dense(1024, activation='relu'),
        layers.BatchNormalization(),
        layers.Dropout(0.3),
        layers.Dense(3, activation='softmax')
        ])

    @classmethod
    def incarcaDataset(cls, path, isTesting):
        #incarca datele din path si returneaza-le
        batches = 1 if isTesting else cls.batchSize
        shuffle = not isTesting
        return keras.preprocessing.image_dataset_from_directory(
                    path,
                    image_size=(50, 50),
                    batch_size=batches,
                    shuffle=shuffle,
                    color_mode="grayscale")

    @classmethod
    def compileazaModel(cls):
        # compilez cu adam si sparsecategoricalcrossentropy
        cls.model.compile(optimizer="adam",
              loss=keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])

    @classmethod
    def fit(cls,dataset_train,dataset_valid):
        # antrenamentul efectiv are loc aici, in functia fit
        
        #am avut earlystopping la un moment dar dar pana la urma nu m-am mai folosit de el
        checkpointLowLoss = ModelCheckpoint('acc{val_accuracy:.3f}_loss{val_loss:.3f}.h5', monitor='val_accuracy', mode='max', verbose=1, save_best_only=True, save_weights_only=False, restore_best_weights=True)
#         earlyStopping = EarlyStopping(monitor='val_loss', mode='min', verbose=1,patience=80)
        
        history = cls.model.fit(
            dataset_train,
            epochs=cls.nrEpochs,
            validation_data=dataset_valid,
            callbacks=[checkpointLowLoss]
        )
        # salveaza modelul antrenat + data/ora la care a fost facut
        timestamp  = datetime.now().strftime("%d-%m-%Y-%H:%M")
        cls.model.save(f'model_{timestamp}.h5')
        
        # returnez asta pt ploturi viitoare
        return history

    @classmethod
    def train(cls):
        # imi incarc dataseturile
        train_ds = cls.incarcaDataset(path=cls.pathTrain, isTesting=False)
        train_va = cls.incarcaDataset(path=cls.pathValid,isTesting=False)
        
        # optimizare pentru TensorFlow - prefetch un nr variabil de date in avans pt a scapa de bottleneck pe hdd
        train_ds = train_ds.cache().prefetch(buffer_size=tf.data.AUTOTUNE)
        train_va = train_va.cache().prefetch(buffer_size=tf.data.AUTOTUNE)

        #compileaza modelul si antreneaza-l pe datasetul dat
        convnet.compileazaModel()
        convnet.fit(train_ds, train_va)

    @classmethod
    def test(cls,path):
        #incarca datele de test
        test_ds = cls.incarcaDataset(path=cls.pathTests, isTesting=True)
        
        #incarca modelul salvat
        model = keras.models.load_model(path,compile = True)
        
        #fa prezicerile si obtine eticheta corecta
        predictions = model.predict(test_ds, verbose=1)
        predictions = np.argmax(predictions,axis=1)

        #Scoate numele in formatul corect si write to file
        full_paths=test_ds.file_paths
        filenames = []
        for f in full_paths:
            name = f.split('/')[-1]
            filenames.append(name)

        results=pd.DataFrame({"id":filenames, "label":predictions})
        
        results.to_csv("results.csv",index=False)

    @classmethod
    def matriceConfuzie(cls, pathModel):
        # din laborator!
        def _compute(predicted_labels, ground_truth_labels):
            num_labels = ground_truth_labels.max() + 1
            conf_mat = np.zeros((num_labels, num_labels))

            for i in range(len(predicted_labels)):
                conf_mat[ground_truth_labels[i], predicted_labels[i]] += 1
            return  conf_mat
        
        #incarc date validation
        date = cls.incarcaDataset(path=cls.pathValid, isTesting=True)
        #incarca modelul salvat
        model = keras.models.load_model(pathModel,compile = True)
        
        #fa prezicerile si obtine eticheta corecta
        predictions = model.predict(date, verbose=1)
        predictions = np.argmax(predictions,axis=1)
        
        # am citit pozele n ordine deci astea s labelurile
        trueLabels = [0 for x in range(1500)] + [1 for x in range(1500)] + [2 for x in range(1500)]
        trueLabels = np.array(trueLabels)
        print(_compute(predictions,trueLabels))
        
def main():
  
    # in functie de ce vreau sa fac, decomentez randul pe care-l folosesc
    convnet.train()
    # convnet.test("../input/antrenat/model 86.h5")
    # convnet.matriceConfuzie('../input/antrenat/model 86.h5')


if __name__ =="__main__":
    main()
