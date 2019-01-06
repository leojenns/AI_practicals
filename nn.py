import numpy as np

class nn_neuron():
    '''
    class nn-neuron: neuron class

    oo-implementation of a neuron for a neural network
    with this implementation it is possible to make a neuron
    with inputs(with there weights).

    '''
    def __init__(self,activation = 1.0,weigths = []):
        """
        def init:   initialisation function

        function that sets the basis variables for a neuron
        1. the neuron activation is the threshold for the neuron output
        2. the input_weights are the weights the inputs are a count for (top->low)
        3. the length is the amount of inputs a neuron has same amount as len(self.input_weights)
        4. the delta is the delta failure for backpropegation

        :param activation: threshold for neuron output
        :param weigths: the weight that are from the inputs in list top->low

        """
        self.neuron_activation = activation
        self.input_weigths = weigths
        self.length = len(self.input_weigths)
        self.delta = None


    def set_weigths(self,weigths):
        """
        def set_weigths:   setter for the input_Weights

        function that sets new weights to neuron input.

        :param weigths: the new weights that need to be assign to self.input_weights

        :return: None
        """
        self.input_weigths = weigths
        self.length = len(self.input_weigths)

    def set_neuron_activation(self, activation):
        """
        def set_neuron_activation:  setter for the neuron activation

        function that sets new neuron_activation

        :param activation: new neuron activation
        :return: None

        """
        self.neuron_activation = activation

    def set_delta(self,s):
        """
        def set_delta:  setter for the delta

        function that sets new delta for backpropegation

        :param delta: new delta
        :return: None

        """
        self.delta = s

    def get_result(self,input):
        """
        def get_result:  function that gives input of neuron for input.

        this function gives the result of the neuron based on input.

        :param input: the input for what the result needs to be calculated
        :return: the result of the neuron (Boolean)

        """
        if len(input) is not len(self.input_weigths):
            print(input, self.input_weigths)
            raise ValueError('amount of weigths and amount of input does not same amount')
        value = 0
        for i in range(self.length):
            value += (input[i] * self.input_weigths[i])
        #print(value , input)
        return 1 if value >= self.neuron_activation else 0


class nn_network():
    """
    class nn_network: nn network layer class
    
    oo-implementation for a neural network.
    the way this implementation is.
    1. each object has a list of nn_neuron objects 
    2. each layer if not output layer had a next layer(a other nn_network object)
    """
    def __init__(self,layer = [],next_layer = None):
        """
        def init:   initialisation function

        :param layer: a list with nn_neurons representing a layer in the network
        :param next_layer: a nn_network object with the next layer
        """
        self.layer = layer
        self.next_layer = next_layer

    def set_learn_rate(self,l):
        """
        def set_learn_rate : setter for the learnrate


        :param l:new learnrrate
        :return: none
        """
        self.learn_rate = l

    def get_result(self,input):
        """
        def get_result :  function for getting result of neural network.

        working:
        The way the get_result function works is by entering the input to the first layer.
        the function will go trought all the layers so the end result is calculated
        :param input:
        :return:result (list)
        """
        result = list(map(lambda x: x.get_result(input),self.layer))
        if self.next_layer is None:
            return result
        return self.next_layer.get_result(result)

    def set_extra_layer(self,n):
        """
        def set_extra_layer: adding function for extra layer


        :param n: new layer added to network at the end
        :return: None
        """
        if self.next_layer is None:
            self.next_layer = n
        else:
            self.next_layer.set_extra_layer(n)

    def _threshold_(self,input):
        """
        def threshold : learn function for backpropegation new thresholds (internal function)
        :param input: learning input
        :return:
        """
        for i in self.layer:
            temp = 0
            for x,y in zip(input,i.input_weigths):
                temp += (x*y)
            i.set_neuron_activation(np.tanh(temp))
        new_input = []
        if self.next_layer is not None:
            for i in self.layer:
                new_input.append(i.neuron_activation)
            self.next_layer._threshold_(new_input)
        return

    def _delta_(self,input = []):
        """
        def delta: learn function for backpropegation new delta (internal function)
        :param input: learning input
        :return: None
        """
        if self.next_layer is not None:
            self.next_layer._delta_(input)
            for i in range(len(self.layer)):
                w = []
                d = []
                for j in self.next_layer.layer:
                    w.append(j.input_weigths[i])
                    d.append(j.delta)
                temp = 0
                for x,y in zip(w,d):
                    temp+= (x*y)
                self.layer[i].set_delta((1 - np.tanh(self.layer[i].neuron_activation)) * temp)
            return
        if len(self.layer) != len(input):
            print(len(self.layer),len(input))
            raise ValueError('input failure',)
        for i in range(len(self.layer)):
            self.layer[i].set_delta((1-np.tanh(self.layer[i].neuron_activation)) * (input[i]-self.layer[i].neuron_activation))

    def _weight_(self,learningrate,input = []):
        """
        def weight : learn function for backpropegation new weight (internal function)
        :param input: learning input
        :param learningrate:  learning rate
        :return:
        """
        for i in self.layer:
            for j in range(len(i.input_weigths)):
                i.input_weigths[j] = i.input_weigths[j] + (i.delta * learningrate * input[j])
        if self.next_layer is not None:
            new_input = []
            for i in self.layer:
                new_input.append(i.neuron_activation)
            self.next_layer._weight_(learningrate,new_input)
        else:
            return

    def learn(self,input=[],learn_rate=1,should_be=[]):
        """
        def learn: learn function for back propegtion

        :param input: input on which
        :param learn_rate: learning rate
        :param should_be: desired answer
        :return: None
        """
        self._threshold_(input)
        self._delta_(should_be)
        self._weight_(learn_rate,input)

    def print_activations(self,layer=1):
        count = 0
        for i in self.layer:

            print(' layer = ',layer, 'neuron = ', count , ' threshold= ',i.neuron_activation)
            count +=1
        if self.next_layer:
           self.next_layer.print_activations(layer= layer+1)
        return

    def print_delta(self,layer=1):
        count = 0
        for i in self.layer:

            print(' layer = ',layer, 'neuron = ', count , ' delta = ',i.delta)
            count +=1
        if self.next_layer:
           self.next_layer.print_delta(layer= layer+1)
        return

    def print_weights(self,layer = 1):
        count = 0
        for i in self.layer:
            for j in i.input_weigths:
                print(' layer = ',layer, 'neuron = ', count , ' gewicht = ',j)
            count +=1
        if self.next_layer:
           self.next_layer.print_weights(layer= layer+1)
        return


'''


#and_port single neuron
and_port = nn_neuron(activation = 1,weigths=[0.5,0.5])
#or port single neuron
or_port = nn_neuron(activation = 0.5,weigths = [0.5,0.5])
#not port single neuron
not_port = nn_neuron(activation =-0.5,weigths = [-1])



nor_port= nn_neuron(-0.5,[-1,-1])

print('norport > [0,0] > 1',nor_port.get_result([0,0]))
print('norport > [1,0] > 0',nor_port.get_result([1,0]))
print('norport > [0,1] > 0',nor_port.get_result([0,1]))
print('norport > [1,1] > 0',nor_port.get_result([1,1]))
# nandport
nand_port = nn_neuron(activation = -0.5,weigths=[-0.5,-0.5])
print('nand > [1,1] > 0 ' ,nand_port.get_result([1,1]))
print('nand > [1,0] > 1 ' ,nand_port.get_result([1,0]))
print('nand > [0,1] > 1 ' ,nand_port.get_result([0,1]))
print('nand > [0,0] > 1 ' ,nand_port.get_result([0,0]))


def adder(input):
     adder_sum  = nand_port.get_result(
        [nand_port.get_result([nand_port.get_result(input),input[0]]),
         nand_port.get_result([nand_port.get_result(input),input[1]])
        ]
    )
     carrying_bit  = nand_port.get_result([nand_port.get_result(input),nand_port.get_result(input)])
     return [adder_sum,carrying_bit ]

print('adder > [0,0]> 0,0 ' ,adder([0,0]))
print('adder > [1,0]> 1,0 ' ,adder([1,0]))
print('adder > [0,1]> 1,0 ' ,adder([0,1]))
print('adder > [1,1]> 0,1 ' ,adder([1,1]))





xor = nn_network([nn_neuron(1.0,[0.2,-0.4]),nn_neuron(1.0,[0.7,0.1])],
                      nn_network([nn_neuron(1.0,[0.6,0.9])]))



#print(xor.get_result([0,1]))
#threshold test


for i in xor.layer:
    print(i.neuron_activation)
for i in xor.next_layer.layer:
    print(i.neuron_activation)




#print(xor.get_result([0,1]))
#xor.learn_threshold([1,1])
xor.learn([1,1],0.1,[0])
xor.print_activations()

#xor.learn_delta([0])
xor.print_delta()
#xor.learn_weights(0.1,[1,1])

xor.print_weights()


print(' \n \n')

xor.threshold([1,0])
xor.print_activations()

xor.delta([1])
xor.print_delta()
xor.weight(0.1,[1,0])

xor.print_weights()

'''
