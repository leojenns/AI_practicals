import numpy as np
import functools
import operator
import itertools

def zipWith(f, xs , ys ):
    """
    python version of the zip with function 

    f  = function with two parameters
    xs = list
    ys = list
    return = list with results 

    """
    if (len(xs) == 0 or len(ys)==0):
        return []
    return [f(xs[0], ys[0])] + zipWith(f, xs[1:], ys[1:])


def map(f, lst):
    """
    python version of map function 
    f    = function with one parameter
    lst  = list
    returns  = list with all the ressults

    """
    return([f(x) for x in lst])

def zipWithMultiply(lst1, lst2):
    """
    zip with with mul function 

    lst1 = list
    lst2 = list
    return = list with multiplications 
    """
    return zipWith(lambda x,y : x*y,lst1,lst2)

def Gprime(number, afterG = True):
    """    
    one minus tanh of tanh 
    for backpropegration

    number  = int
    afterG = bool  " for if G function is calle before"
    return = int  
    """
    if afterG:
        return 1-G(number)
    return 1-G(G(number))

def G(number):
    """
    shorter function for calling tanh

    number  = int 
    result  = int 
    """
    return np.tanh(number)


def concat(f, lst):
    """
    f = function
    lst = list
    shorter funcion for reduce(foldr)
    """
    return functools.reduce(f, lst)
def tobin(lst):
    """
    return list where max is 1 others are 0 
    """
    return [ 0 if (i != lst.index(max(lst))) else 1   for i in range(len(lst)) ]
