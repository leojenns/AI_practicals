from libnn.nn import *

##base NOR
NOR = Neuron(-0.5, [-1,-1])
print(NOR)
##train NOR with input 1,0 -> 0
NOR.deltaRule([1,0],0.1,0)
print(NOR)
