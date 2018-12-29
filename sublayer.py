import numpy as np
from sklearn.neural_network import MLPClassifier
import math
import random

class Sublayer(object):

    def __init__(self,f,nodes):
        self.getData(f)
        self.train(nodes)
        
    def predict(self,x):
        return int(self.network.predict(x)[0])

    def train(self,nodes):
        self.X = np.asarray(self.X)
        self.X = self.X.reshape(self.X.shape[0],self.X.shape[1] * self.X.shape[2])
        self.Y = np.asarray(self.Y)
        self.testx = np.asarray(self.testx)
        self.testx = np.asarray(self.testx)  
        self.network = MLPClassifier(activation="relu", validation_fraction=0.22,hidden_layer_sizes=(nodes,),max_iter=1000)
        self.network.fit(self.X,self.Y)
                
    def getData(self,f,param=32):
        X = []
        Y = []
        with open(f, 'r' ) as data:
            content = data.readlines()
            for line in content:
                splitted = line.split("/")
                splitted = [x for x in splitted[:-1]] + splitted[-1:]
                s = []
                for x in splitted:
                    aa = [int(asd) for asd in x if asd.isdigit()]
                    s.append(aa)
                splitted = s
                x = []
                if (len(splitted) < param + 1):
                    for value in splitted[:-1]:
                        x.append(value)
                else:
                    for value in splitted[:param]:
                        x.append(value)
                while(len(x) <param):
                    aux = [1] + [0] * 20
                    x.append(aux)
                y = splitted[-1][0]
                X.append(x)
                Y.append(y)
        self.X = X
        self.Y = Y
        self.shuffle()
    
    def shuffle(self):
        X = self.X
        Y = self.Y
        combined = list(zip(X, Y))
        random.shuffle(combined)
        X[:], Y[:] = zip(*combined)
        n = int(len(X)/10)
        aux = len(X)
        self.testx = X[aux-n:]
        self.X = X[:aux-n]
        self.testy = Y[aux-n:]
        self.Y = Y[:aux-n]
