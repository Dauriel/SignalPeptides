import sys
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def genFile(file):
    dic = {"A":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"K":9,"L":10,"M":11,"N":12,"P":13,"Q":14,"R":15,"S":16,"T":17,"V":18,"W":19,"Y":20, "X": 0}
    t = open("test.txt", "w+") #name of the file
    with open(file , 'r' ) as data:
        content = data.readlines()
        text = ""
        counter = 0
        auxlength = 0
        for i in range(0,len(content),2):
            auxtext = content[i].strip()
            splitted = content[i+1].split()
            auxt = ""
            auxlength += len(auxtext)
            for letter in auxtext:
                aux = dic[letter]
                tt = [0]*21
                tt[aux] = 1
                auxt += str(tt) + "/"
            auxt += splitted[0] + "/" + splitted[1] + "%\n"
            text += auxt
            counter += 1
        t.write(text)
        t.close()
if __name__ == "__main__":
    genFile(sys.argv[1])