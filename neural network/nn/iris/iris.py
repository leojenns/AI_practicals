from libnn import *

import csv
import copy
import operator

def sort_table(table, cols):
    """ sort a table by multiple columns
        table: a list of lists (or tuple of tuples) where each inner list
               represents a row
        cols:  a list (or tuple) specifying the column numbers to sort by
               e.g. (1,0) would sort by column 1, then by column 0
    """
    for col in reversed(cols):
        table = sorted(table, key=operator.itemgetter(col))
    return table

def sortt(mytable):
    for row in sort_table(mytable, (2,0)):
        print (row)
#init the network with random based weight.
#based on research online the number of neurons is as follows 4 - 5 - 3 - 3  
iris_network = Network(layer=[Neuron([-0.2,0.4,-0.5,0.2]),Neuron([0.3,0.1,0.9,0.33]),Neuron([-0.1, 0.3,-1.3,0.3]),Neuron([0.3,0.2,-0.1,0.4]),Neuron([0.4,-0.3,-0.5,0.7])])
iris_network.setExtraLayer(Network([Neuron([1.4, 2, 0.4, -0.9, 0.2]),Neuron([-0.3 ,-0.3 ,0.7 ,-0.9, 0.1]),Neuron([-2.4, -1.1, 0.4, 2.2, 0.7])]))
iris_network.setExtraLayer(Network([Neuron([0.3,0.7,0.5]),Neuron([-0.7,0.6,0.9]),Neuron([-0.5,2.7,1.3])]))
#copy of the network
iris_copy = copy.deepcopy(iris_network)

# empty data 
data            = []
training_data   = []
validation_data = []


#open shuffled csv data and read rows and ad to data 
with open('shuffled.csv','r') as d :
    reader = csv.reader(d,delimiter = ',')
    for row in reader:
        data.append(row)
# split 20-80 the data
training_data = data[:(int(len(data)*0.8))]
validation_data = data[int(len(data)*0.8):]

ml = iris_copy 
#learning rate
lr = 0.1
#learn with loop of 1000
for _ in range(1000):
    #loop training data
    for data_point in training_data:

        for i in range(4):
            data_point[i] = float(data_point[i])

        if data_point[4] == 'Iris-virginica':

            ml.learn(data_point[0:4],lr,[0,0,1])
        elif data_point[4]== 'Iris-versicolor':
            ml.learn(data_point[0:4],lr,[0,1,0])
        else:
            ml.learn(data_point[0:4],lr,[1,0,0])
#init correct int to 0
correct = 0
# init total number of validation data
total   = len(validation_data)

#validation loop 
for validation_point in validation_data:

    for i in range(4):
        validation_point[i] = float(validation_point[i])

    if validation_point[4] == 'Iris-virginica':
        if ml.result(validation_point[0:4]) == [0,0,1]:

            correct = correct + 1
    elif validation_point[4]== 'Iris-versicolor':
        if ml.result(validation_point[0:4])==[0,1,0]:

            correct = correct + 1
    else:
        if ml.result(validation_point[0:4])==[1,0,0]:

            correct = correct + 1


print("number correct : ", correct)
print("number total : ", total)
print("score (in &): ", (correct/ total) * 100)

