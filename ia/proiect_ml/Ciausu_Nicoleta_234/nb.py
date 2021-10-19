# Creat cu ajutorul laboratorului 2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.naive_bayes import MultinomialNB

class naive_bayes:
    
    train_images = []
    train_labels = []
    test_images = []
    test_labels = []
    
    @classmethod
    # de la laborator
    def confusion_matrix(cls,predicted_labels, ground_truth_labels):
        # iau valorile prezise si valorile care trebuiau sa fie
        # si vad cate au fost prezise corect si cate gresit
        num_labels = ground_truth_labels.max() + 1
        conf_mat = np.zeros((num_labels, num_labels))

        for i in range(len(predicted_labels)):
            conf_mat[ground_truth_labels[i], predicted_labels[i]] += 1
        return conf_mat

    
    @classmethod
    # returneaza din ce bin face parte fiecare numar din x
    def values_to_bins(cls, x, bins):
        return np.digitize(x, bins) - 1
    
    @classmethod
    def load(cls):
        ############ train ###################
        print("loading train...")
        labels = pd.read_csv("../input/ai-unibuc-23-31-2021/train.txt")
        src_images = np.array(labels[labels.columns[0]].to_numpy())
        cls.train_labels = np.array(labels[labels.columns[1]].to_numpy())
        
        #flattening si adaugat in array
        for src_img in src_images:
            img = plt.imread("../input/ai-unibuc-23-31-2021/train/" + src_img).flatten() * 255
            cls.train_images.append(img)
        
        ############## validation ################
        print("loading test...")

        labels = pd.read_csv("../input/ai-unibuc-23-31-2021/validation.txt")
        src_images = np.array(labels[labels.columns[0]].to_numpy())
        cls.test_labels = np.array(labels[labels.columns[1]].to_numpy())
        
        #flattening si adaugat in array
        for src_img in src_images:
            img = plt.imread("../input/ai-unibuc-23-31-2021/validation/" + src_img).flatten() * 255
            cls.test_images.append(img)            
        
        
    @classmethod
    def run(cls):
        #pun in bins
        scores = []
        best_prediction = []
        #intervale egale, 3 a mers cel mai bine (restul dau aproape de random, gen de 33%)
        # aici testez cu mai multe
        for nr_bins in [3,5,7,11,13,17,19,23,143, 253]:
            bins = np.linspace(0, 256, num=nr_bins) 
            train_images_bins = cls.values_to_bins(cls.train_images, bins)
            test_images_bins = cls.values_to_bins(cls.test_images, bins)

            # rulez NB
            nb = MultinomialNB()
            nb.fit(train_images_bins,cls.train_labels)

            # prezicere si accuracy
            predictions = nb.predict(test_images_bins)
            score = nb.score(test_images_bins, cls.test_labels)
            scores.append([nr_bins, score, predictions])
            print(str(nr_bins-1) + " intervale, acuratete: " + str(score))
        
        best_prediction = max(scores, key=lambda x:x[1])
        print("Acuratete maxima obtinuta: " + str(best_prediction[1]) + " (cu nr de intervale = " + str(best_prediction[0]-1) + ')')
        print("Matrice de confuzie pentru acuratetea maxima:")
        # matrice de confuzie
        print(cls.confusion_matrix(best_prediction[2],cls.test_labels))

naive_bayes.load()
naive_bayes.run()


