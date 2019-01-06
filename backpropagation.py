from numpy import tanh

def threshold(thres,multiplairs):
    if len(thres) is not len(multiplairs):
        raise ValueError('thres and multipairs are not ame length')
    new_value  = 0

    for i in range(len(thres)):
        new_value += (thres[i] * multiplairs[i])
    return tanh(new_value)

