import numpy as np
import functools
import operator
import itertools
def zipWith(f, xs , ys ):
    if (len(xs) == 0 or len(ys)==0):
        return []
    return [f(xs[0], ys[0])] + zipWith(f, xs[1:], ys[1:])


def map(f, lst):
    return([f(x) for x in lst])

def zipWithMultiply(lst1, lst2):
    return zipWith(lambda x,y : x*y,lst1,lst2)

def Gprime(number, afterG = True):
    if afterG:
        return 1-G(number)
    return 1-G(G(number))

def G(number):
    return np.tanh(number)


def concat(f, lst):
    return functools.reduce(f, lst)
def tobin(lst):
    return [ 0 if (i != lst.index(max(lst))) else 1   for i in range(len(lst)) ]
