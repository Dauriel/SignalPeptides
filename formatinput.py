import sys
import os
from collections import Counter
import pandas as pd
import numpy as np
from numbered import genFile as genFile

def main(negativetm, positivetm,negative,positive):
    ff = "rawsamples.txt"
    f = open(ff, "w+")
    folders = [[negativetm,1,0],[positivetm,1,1],[negative,0,0],[positive,0,1]]
    for folder in folders:
        text = genratios(folder[0],folder[1],folder[2])
        f.write(text)
    f.close()
    genFile(ff)
    os.remove(ff)


def genratios(folder,tm,charge):
    collectionpath = "./" + folder
    directory = os.fsencode(collectionpath)
    text = ""
    for file in os.listdir(directory):
        f = collectionpath + "/" + os.fsdecode(file)
        try:
            with open(f , 'r' ) as archive:
                content = archive.readlines()
                filteredcontent = filter(content)
                auxtext = contenttext(filteredcontent,tm,charge)
                text+=auxtext
        except FileNotFoundError:
            print("File not found")
    return text

def contenttext(content,tm,charge):
    text = ""
    for element in content:
        textaux = ""
        sequence = element[1]
        textaux += sequence + " " + str(tm) + " " + str(charge) + "\n"
        text+=textaux
    return text

def filter(content):
    total = []
    aux = []
    for element in content:
        if ">" in element:
            if aux:
                total.append(aux)
                aux = []
        aux.append(element)
    total.append(aux)
    return total

def syntax():
    root = sys.argv[0]
    print ("\n%s file\n\n \t\tor \n\n%s -f folder\n" % (root,root), file = sys.stderr)
    sys.exit()

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
