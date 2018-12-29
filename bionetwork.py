from firstlayer import Firstlayer as upperlayer
from sublayer import Sublayer as bottomlayer

class BioNetwork(object):

    def __init__(self):
        print("Setting up first layer...")
        self.upper = upperlayer()
        print("Setting up second layer (1/2)...")
        self.bottomtm = bottomlayer("hottm.txt",28)
        print("Setting up second layer (2/2)...")
        self.bottomnontm = bottomlayer("hotnontm.txt",49)
        
    def predict(self,x):
        first = self.upper.predict(x)
        if(first == 1):
            return self.bottomtm.predict(x)
        else:
            return self.bottomnontm.predict(x)
                
    