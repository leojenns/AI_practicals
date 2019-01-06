from backpropagation import *
import numpy as np

print(threshold([0.2,-0.4],[1,1]))


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






a = []

a.append([3,0.03,20])
a.append([3,0.04,3])
a.append([3,0.03,7])
a.append([3,0.03,0])
a.append([3,0.03,12])
a.append([6,0.05,22])
a.append([3,0.03,6])
a.append([3,0.03,3])
a.append([3,0.03,8])
sortt(a)



