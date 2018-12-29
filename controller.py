import numpy as np
from sklearn.neural_network import MLPClassifier
import math
import random
from bionetwork import BioNetwork as bio


def main():
    #Network creation
    network = bio()

    #Obtain testing set and testing labels
    testx,testy = getData()
    testx = np.asarray(testx)
    testy = np.asarray(testy)

    #Calculate MSE of network over testing set
    total = len(testx)
    suma = 0
    for i,s in enumerate(testx):
        x = s.reshape(1,-1)
        prediction = network.predict(x)
        label = int(testy[i])
        print(prediction,label)
        suma += (prediction-label)**2 #MSE
    return suma/total

def getData(param=32):
    '''
    Retrieve data from file "test.txt"
    '''
    X = []
    Y = []
    with open("test.txt" , 'r' ) as data:
        content = data.readlines()
        for line in content:
            splitted = line.split("/")
            splitted = [x[1:-1] for x in splitted[:-2]] + splitted[-2:]
            s = []
            for x in splitted:
                aa = [int(asd) for asd in x if asd.isdigit()]
                s.append(aa)
            splitted = s
            x = []
            if (len(splitted) < param + 2):
                for value in splitted[:-2]:
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
    testx,testy = shuffle(X,Y)
    return testx,testy

def shuffle(X,Y):
    '''
    Shuffle two lists and obtain a 10% testing set
    '''
    combined = list(zip(X, Y))
    random.shuffle(combined)
    X[:], Y[:] = zip(*combined)
    n = int(len(X)/10)
    aux = len(X)
    testx = X[aux-n:]
    X = X[:aux-n]
    testy = Y[aux-n:]
    Y = Y[:aux-n]
    return testx,testy

if __name__ == "__main__":
    mse = main()
    print("MSE of:", mse)
  
