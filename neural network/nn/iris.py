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


iris_network = createNetwork([4,5,3,3],-1,1)
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
lr = 0.1
for _ in range(5000):
    for data_point in training_data:
        #print(data_point)
        for i in range(4):
            data_point[i] = float(data_point[i])
        #print(data_point[4])
        if data_point[4] == 'Iris-virginica':
           # print("fucking hell")
            ml.learn(data_point[0:4],lr,[0,0,1])
        elif data_point[4]== 'Iris-versicolor':
            ml.learn(data_point[0:4],lr,[0,1,0])
        else:
            ml.learn(data_point[0:4],lr,[1,0,0])
win     = len(validation_data)
correct = 0
for validation_point in validation_data:
    #print(ml.result(validation_point))
    #print(validation_point)
    for i in range(4):
        validation_point[i] = float(validation_point[i])
    #print(ml.result(validation_point[0:4]))

    if validation_point[4] == 'Iris-virginica':
        if tobin(ml.result(validation_point[0:4])) == [0,0,1]:
            print(1)
            correct = correct + 1
    elif validation_point[4]== 'Iris-versicolor':
        if tobin(ml.result(validation_point[0:4]))==[0,1,0]:
            print(2)
            correct = correct + 1
    else:
        if tobin(ml.result(validation_point[0:4]))==[1,0,0]:
            print(3)
            correct = correct +1

print (" total validation points are :", win)
print ("total correct are ", correct)
print ("score =" , win / correct *100)




