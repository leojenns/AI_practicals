from helperfuncs import *
import copy
class Neuron():

    def __init__(self,weights = []):
        """ init function 
        :param weights:
        :returns: 
        :rtype: 

        """
        self.weights = weights
        self.length = len(self.weights)
        self.delta = None

    def __str__(self):
        """string represitation

        :returns: string represitation
        :rtype: string

        """
        wstr = ["weights : "+(str(x)+"\n") for x in self.weights]
        return concat(operator.add, wstr)

    def len(self):
        """len of the weights list

        :returns: length of number of weights
        :rtype: int

        """
        self.length = len(self.weights)

    def setweights(self, weights):
        """set the weights

        :param weights: lst
        :returns: nothing
        :rtype: noting

        """

        self.weights = weights
        self.length = len(self.weights)

    def setActivation(self, s):
        """set activation

        :param s: int 
        :returns: nothing
        :rtype:  nothing

        """
        self.activation = s

    def setDelta(self,s):
        """set delta

        :param s: int
        :returns:  nothing
        :rtype: nothing

        """
        self.delta = s

    def result(self, input):
        """result of neuron

        :param input: input of neuron 
        :returns: result of neuro
        :rtype: int

        """
        if len(input) is len(self.weights):
                return sum(zipWithMultiply(self.weights, input))
        raise ValueError('amount of weights and amount of input does not same amount')
        print(input, self.weights)
    def DeltaRule(self,learningInput, learningRate, desiredAnswer):
        """delta regel

        :param learningInput: learing input 
        :param learningRate:  learning rate
        :param desiredAnswer: desired answer
        :returns: new weights
        :rtype: lst

        """
        base = G(self.result(learningInput))
        for i in range(self.length):
            self.weights[i] = self.weights[i] + learningRate * learningInput[i] * Gprime(base) *(desiredAnswer - base)
        self.len()
        return(self.weights)

class Network():

    def __init__(self,layer = [],next_layer = None):
        """init function for network

        :param layer: list of neurons of current layer
        :param next_layer: new network with new layers
        :returns: nothing
        :rtype: 

        """

        self.layer = layer
        self.next_layer = next_layer

    def setLearnRate(self,l):
        """ set learning rate

        :param l: new learning rate (int)
        :returns: noting
        :rtype: nothing

        """

        self.learn_rate = l

    def result(self,input):
        """result of network

        :param input: list of input
        :returns: result 
        :rtype: list of int

        """
        result = list(map(lambda x: x.result(input),self.layer))
        if self.next_layer is None:
            return tobin(result)
        return self.next_layer.result(result)

    def setExtraLayer(self,next):
        """set next layer
        :param next: next network
        :returns: nothing
        :rtype: nothing

        """
        if self.next_layer is None:
            self.next_layer = next
        else:
            self.next_layer.setExtraLayer(next)

    def threshold(self,input):
        """calculate treshold

        :param input: train input
        :returns: nothing
        :rtype: nothing

        """
        for i in self.layer:
            temp = 0
            for x,y in zip(input,i.weights):
                temp += (x*y)
            i.setActivation(G(temp))
        new_input = []
        if self.next_layer is not None:
            for i in self.layer:
                new_input.append(i.activation)
            self.next_layer.threshold(new_input)
        return

    def delta(self,input = []):
        """calculate delta rule network
        :param input: train input
        :returns: nothing
        :rtype: nothing

        """

        if self.next_layer is not None:
            self.next_layer.delta(input)
            for i in range(len(self.layer)):
                w = []
                d = []
                for j in self.next_layer.layer:
                    w.append(j.weights[i])
                    d.append(j.delta)
                temp = 0
                for x,y in zip(w,d):
                    temp+= (x*y)
                self.layer[i].setDelta((Gprime(self.layer[i].activation)) * temp)
            return
        if len(self.layer) != len(input):
            print(len(self.layer),len(input))
            raise ValueError('input failure',)
        for i in range(len(self.layer)):
            self.layer[i].setDelta((Gprime(self.layer[i].activation)) * (input[i]-self.layer[i].activation))

    def weight(self,learningrate,input = []):
        """calculate new weights

        :param learningrate: float learning rate
        :param input: train input
        :returns: nothing
        :rtype: nothing

        """

        for i in self.layer:
            for j in range(len(i.weights)):

                i.weights[j] =round( i.weights[j] + (i.delta * learningrate * input[j]),2)
        if self.next_layer is not None:
            new_input = []
            for i in self.layer:
                new_input.append(i.activation)
            self.next_layer.weight(learningrate,new_input)
        else:
            return

    def learn(self,input=[],learn_rate=1,should_be=[]):
        """learn network

        :param input: trai input list of numbers
        :param learn_rate: learn rate float
        :param should_be: desired resultof network
        :returns: nothing
        :rtype: nothing

        """

        self.threshold(input)
        self.delta(should_be)
        self.weight(learn_rate,input)

    def print_activations(self,layer=1):
        """print the activation

        :param layer: int
        :returns: printed on console all activations of network with next layers activations
        :rtype: nothing

        """
        count = 0
        for i in self.layer:

            print(' layer = ',layer, 'neuron = ', count , ' threshold= ',i.activation)
            count +=1
        if self.next_layer:
           self.next_layer.print_activations(layer= layer+1)
        return

    def print_delta(self,layer=1):
        """print delta of network

        :param layer: int
        :returns: printed on console all the deltas of the network
        :rtype: nothing

        """
        count = 0
        for i in self.layer:

            print(' layer = ',layer, 'neuron = ', count , ' delta = ',i.delta)
            count +=1
        if self.next_layer:
           self.next_layer.print_delta(layer= layer+1)
        return

    def print_weights(self,layer = 1):
        """print all the weights

        :param layer: int
        :returns: printed on the console all the weights of all the layers
        :rtype: 

        """
        count = 0
        for i in self.layer:
            for j in i.weights:
                print(' layer = ',layer, 'neuron = ', count , ' gewicht = ',j)
            count +=1
        if self.next_layer:
           self.next_layer.print_weights(layer= layer+1)
        return
