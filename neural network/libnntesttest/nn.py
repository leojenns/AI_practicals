import numpy as np
import copy
from helperfuncs import *





class Neuron():
    def __init__(self, activation, weights):
        self.activation = activation
        self.weights = weights
        self.inputNeuron = (len(weights) is 0)

    def __str__(self):
        pr = ""
        for i in self.weights:
            w = "weight: " + str(i) + "\n"
            pr = pr + w
        pr = pr + "activation = " + str((self.activation))
        return pr


    def result(self, input):
         return sum((zipWith((lambda x, y : x*y), input, self.weights)) )



    def deltaRule(self, learningInput, learningRate, desiredOutput):
        base = np.tanh(self.result(learningInput))
        oldWeights = copy.deepcopy(self.weights)
        for i in range(len(self.weights)):
            self.weights[i] =  ( oldWeights[i] + learningRate * learningInput[i]*Gprime(base) * (desiredOutput - base))



class Network():
    def __init__(self, next_layer):
        self.nextLayer = next_layer
        self.lastLayer = not next_layer



