import numpy as np
import sys
from sklearn.neural_network import MLPClassifier
import math
import random
from bionetwork import BioNetwork as bio


def main(arc):
    #Network creation
    network = bio()

    #Obtain testing set and testing labels
    X = getData(arc)
    X = np.asarray(X)
    #Calculate MSE of network over testing set

    positive = 0
    negative = 0
    print("Processing samples...")
    for i,s in enumerate(X):
        x = s.reshape(1,-1)
        prediction = network.predict(x)
        if(prediction == 1):
            positive+=1
        else:
            negative+=1            
    return positive,negative

def getData(arc,param=32):
    '''
    Retrieve data from file "onehot.txt"
    '''
    X = []
    with open(arc, 'r' ) as data:
        content = data.readlines()
        for line in content:
            splitted = line.split("/")
            splitted = [x[1:-1] for x in splitted[:-1]]
            s = []
            for x in splitted:
                aa = [int(asd) for asd in x if asd.isdigit()]
                s.append(aa)
            splitted = s
            x = []
            for value in splitted:
                x.append(value)
            while(len(x) <param):
                aux = [1] + [0] * 20
                x.append(aux)
            X.append(x)
    return X

if __name__ == "__main__":
    positive,negative = main(sys.argv[1])
    print("Positive samples:", positive)
    print("Negative samples:", negative)
  