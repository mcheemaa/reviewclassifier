#started 

import math
import re

class Bayes_Classifier:

    def __init__(self):

        self.alpha = 1

        self.vocab = set([])
        self.wordsPosC = 0
        self.wordsNegC = 0

        self.numPosR = 0
        self.numNegR = 0

        self.megPos = set([])
        self.megNeg = set([])

        self.wordCountPos = {}
        self.wordCountNeg = {}

    def removePunc(self, text):


        orig = text
        punc = ""'!()-[]{};:'"\,<>./?@#$%^&*_~''" # took it from geeksforgeeks

        for word in orig:
            if word in punc:
                orig = orig.replace(word, "")

        return (orig)


    def train(self, lines):

        for l in lines:
            l = l.replace("\n", " ")
            data = l.split("|")
            
            #print("Checking : ", data[0])
            
            numStar = data[0]
            text = data[2]

            text = self.removePunc(text)

            words = text.split(" ")

            if (numStar == "1"):
                self.numNegR += 1
            else:
                self.numPosR += 1

            for w in words:
                w = w.lower()
                self.vocab.add(w)

                if (numStar == "1"):
                    self.wordsNegC += 1
                    self.megNeg.add(w)

                    if (w in self.wordCountNeg):
                        self.wordCountNeg[w] += 1
                    else:
                        self.wordCountNeg[w] = 1

                else:
                    self.wordsPosC += 1
                    self.megPos.add (w)

                    if (w in self.wordCountPos):
                        self.wordCountPos[w] += 1
                    else:
                        self.wordCountPos[w] = 1

    def classify(self, lines):

        vocSize = len(self.vocab)

        finalSentiment = []

        #print( "Numbe of Postive Reviews : " , self.numNegR)

        probPos = math.log(float(self.numPosR) / float((self.numPosR + self.numNegR)))
        probNeg = math.log(float(self.numNegR) / float((self.numPosR + self.numNegR)))

        for l in lines:
            l = l.replace("\n", " ")
            data = l.split("|")
            
            #print("Checking : ", data[0])
            
            numStar = data[0]
            text = data[2]
            text = self.removePunc(text)

            words = text.split(" ")

            probNegW = probNeg
            probPosW = probPos

            for W in words:
                W = W.lower()

                
                if (W in self.wordCountNeg):
                    #print("W is  : " , W )
                    probNegW += math.log(float((self.wordCountNeg[W]) + self.alpha) / float((self.wordsNegC + vocSize)))

                    if (W not in self.wordCountPos):
                        probPosW += math.log (1.0 / float((self.wordsPosC + ( vocSize + 1))))

                if (W in self.wordCountPos):
                    probPosW += math.log(float((self.wordCountPos[W]) + self.alpha) / float((self.wordsPosC + vocSize)))
                    
                    if (W not in self.wordCountNeg):
                        probNegW += math.log (1.0 / float((self.wordsNegC + (vocSize + 1))))


            if (probNegW > probPosW):
                finalSentiment.append("1")
            else:
                finalSentiment.append("5")
        
        return finalSentiment
        
