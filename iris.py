from nn import *
import numpy as np
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



iris_network = nn_network(layer=[nn_neuron(1.2,[-0.2,0.4,-0.5,0.2]),nn_neuron(2.5,[0.3,0.1,0.9,0.33]),nn_neuron(7.0,[-0.1, 0.3,-1.3,0.3]),nn_neuron(5.4,[0.3,0.2,-0.1,0.4]),nn_neuron(-6.8,[0.4,-0.3,-0.5,0.7])])

iris_network.set_extra_layer(nn_network([nn_neuron(-0.2,[1.4, 2, 0.4, -0.9, 0.2]),nn_neuron(1.4,[-0.3 ,-0.3 ,0.7 ,-0.9, 0.1]),nn_neuron(-1.2,[-2.4, -1.1, 0.4, 2.2, 0.7])]))
iris_network.set_extra_layer(nn_network([nn_neuron(1.8,[0.3,0.7,0.5]),nn_neuron(1.6,[-0.7,0.6,0.9]),nn_neuron(1.2,[-0.5,2.7,1.3])]))
iris_copy = copy.deepcopy(iris_network)


data = []
training_data = []
validation_data = []

with open('shuffled.csv','r') as d :
    reader = csv.reader(d,delimiter = ',')
    for row in reader:
        data.append(row)

training_data = data[:(int(len(data)*0.8))]
validation_data = data[int(len(data)*0.8):]
ml = iris_copy
lr = 0.01
for data_point in training_data:
    print(data_point)
    for i in range(4):
        data_point[i] = float(data_point[i])
    print(data_point)
    if data_point[4] == 'Iris-virginica':
        ml.learn(data_point[0:4],lr,[0,0,1])
    elif data_point[4]== 'Iris-versicolor':
        ml.learn(data_point[0:4],lr,[0,1,0])
    else:
        ml.learn(data_point[0:4],lr,[1,0,0])

for validation_point in validation_data:
    #print(ml.get_result(validation_point))
    #print(validation_point)
    for i in range(4):
        validation_point[i] = float(validation_point[i])
    print(ml.get_result(validation_point[0:4]))

    if validation_point[4] == 'Iris-virginica':
        if ml.get_result(validation_point[0:4]) == [0,0,1]:
            print(1)
    elif validation_point[4]== 'Iris-versicolor':
        if ml.get_result(validation_point[0:4])==[0,1,0]:
            print(1)
    else:
        if ml.get_result(validation_point[0:4])==[1,0,0]:
            print(1)



'''

m = []
m_i =[]

h = 10
print(h)
for lr in np.arange(0.001, 0.3, 0.001):
    iris = copy.deepcopy(iris_copy)
    for _ in range(h):

        with open('shuffled.csv','r') as d :
            reader = csv.reader(d,delimiter = ',')
            for row in reader:
                for i in range(4):
                    row[i] = float(row[i])
                if row[4] == 'Iris-virginica':
                    iris.learn(row[0:4],lr,[0,0,1])
                elif row[4]== 'Iris-versicolor':
                    iris.learn(row[0:4],lr,[0,1,0])
                else:
                    iris.learn(row[0:4],lr,[1,0,0])




    count = 0

    with open('shuffled.csv','r') as d :
        reader = csv.reader(d,delimiter = ',')
        for row in reader:
            for i in range(4):
                row[i] = float(row[i])
            if row[4] == 'Iris-virginica':
                l=[0,0,1]
            elif row[4]== 'Iris-versicolor':
                l =[0,1,0]
            else:
                l = [1,0,0]

            if iris.get_result(row[0:4]) == l:
                count +=1


    m.append(count)
    m_i.append(lr)

print(max(m))
print(m_i[m.index(max(m))])
'''

"""
values = []
for times in range(0,50):
    print(times)
    for lr in np.arange(0.01,0.04, 0.0005):



        iris = copy.deepcopy(iris_copy)
        for _ in range(times):

            with open('shuffled.csv','r') as d :
                reader = csv.reader(d,delimiter = ',')
                for row in reader:
                    for i in range(4):
                        row[i] = float(row[i])
                    if row[4] == 'Iris-virginica':
                        iris.learn(row[0:4],lr,[0,0,1])
                    elif row[4]== 'Iris-versicolor':
                        iris.learn(row[0:4],lr,[0,1,0])
                    else:
                        iris.learn(row[0:4],lr,[1,0,0])

        with open('shuffled.csv','r') as d :
            reader = csv.reader(d,delimiter = ',')
            for row in reader:
                for i in range(4):
                    row[i] = float(row[i])
                if row[4] == 'Iris-virginica':
                    l=[0,0,1]
                elif row[4]== 'Iris-versicolor':
                    l =[0,1,0]
                else:
                    l = [1,0,0]

                if iris.get_result(row[0:4]) == l:
                    count +=1

        values.append([times,lr,count])

sortt(values)
'''

46, 0.027500000000000017, 97]
[46, 0.03350000000000002, 97]
[47, 0.027000000000000017, 97]
[47, 0.027500000000000017, 97]
[48, 0.027500000000000017, 97]
[48, 0.03150000000000002, 97]
[48, 0.03350000000000002, 97]
[49, 0.027000000000000017, 97]
[49, 0.027500000000000017, 97]
[37, 0.03350000000000002, 99]
[42, 0.03150000000000002, 99]
[44, 0.03150000000000002, 99]
[44, 0.03350000000000002, 99]
[47, 0.03350000000000002, 99]
[48, 0.027000000000000017, 99]
[49, 0.03150000000000002, 99]

'''
"""
