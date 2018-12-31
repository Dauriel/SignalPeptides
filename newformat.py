import sys
import os
from collections import Counter
import pandas as pd
import numpy as np
from newnumbered import genFile as genFile

def main(arc,out):
    ff = "rawsamples.txt"
    f = open(ff, "w+")
    text = genratios(arc)
    f.write(text)
    f.close()
    genFile(ff,out)
    os.remove(ff)


def genratios(folder):
    collectionpath = "./" + folder
    directory = os.fsencode(collectionpath)
    text = ""
    for file in os.listdir(directory):
        f = collectionpath + "/" + os.fsdecode(file)
        try:
            with open(f , 'r' ) as archive:
                content = archive.readlines()
                filteredcontent = filter(content)
                auxtext = contenttext(filteredcontent)
                text+=auxtext
        except FileNotFoundError:
            print("File not found")
    return text

def contenttext(content):
    text = ""
    for element in content:
        textaux = ""
        sequence = "".join(element[1:])
        sequence = sequence.replace("\n","")
        sequence = sequence[:32]
        textaux += sequence + "\n"
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
    main(sys.argv[1],sys.argv[2])
