from numpy import tanh
from functools import reduce

def calculate_treshold(weights, thresholds ):
    if len(weights) is not len(thresholds):
        raise ValueError('amount of weigths and amount of input does not same amount')
    temp = 0
    for i, j in zip(weights,thresholds):
        print(i,j)
        temp += i*j
    return tanh(temp)

#print(calculate_treshold([0.6 , 0.9],[-0.2,0.66]))


def delta(threshold,weights = [], last_deltas = [] ,is_output = False,output = 0,should_be = 0):
    print(threshold)
    g_accent = 1 - (tanh(threshold))
    if is_output:
        print('g accent output',g_accent,' should_be',should_be,' output' , output, g_accent * (should_be - output))

        return g_accent * (should_be - output)
    temp_2 = 0
    for i , j in zip(weights,last_deltas):
        temp_2 += i*j
    return g_accent * temp_2

#print(delta(weights = [0.69,0.09], threshold = [1,0] , weigth=0.88, last_delta=0.22 ))


def calculate_weigths( old_weigth, learn_rate,input_threshold, delta):
    return old_weigth + (learn_rate * input_threshold * delta)

    # oude gewicht + leerrate * threshold input neuron *delta output neuron










