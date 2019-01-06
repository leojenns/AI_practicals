from libnn import *
import time
import random

#and_port single neuron
and_port = Neuron(weights=[0.5,0.5])
#or port single neuron
or_port = Neuron(weights = [0.5,0.5])
#not port single neuron
not_port = Neuron(weights = [-1])



nor_port= Neuron([random.uniform(0,1) for _ in range(3)])

print('norport > [0,0] > 1',nor_port.result([0,0,1]))
print('norport > [1,0] > 0',nor_port.result([1,0,1]))
print('norport > [0,1] > 0',nor_port.result([0,1,1]))
print('norport > [1,1] > 0',nor_port.result([1,1,1]))
# nandport

nand_port = Neuron(weights=[-0.5,-0.5])
print('nand > [1,1] > 0 ' ,nand_port.result([1,1]))
print('nand > [1,0] > 1 ' ,nand_port.result([1,0]))
print('nand > [0,1] > 1 ' ,nand_port.result([0,1]))
print('nand > [0,0] > 1 ' ,nand_port.result([0,0]))



def adder(input):
     adder_sum  = nand_port.result(
        [nand_port.result([nand_port.result(input),input[0]]),
         nand_port.result([nand_port.result(input),input[1]])
        ]
    )
     carrying_bit  = nand_port.result([nand_port.result(input),nand_port.result(input)])
     return [adder_sum,carrying_bit ]

print('adder > [0,0]> 0,0 ' ,adder([0,0]))
print('adder > [1,0]> 1,0 ' ,adder([1,0]))
print('adder > [0,1]> 1,0 ' ,adder([0,1]))
print('adder > [1,1]> 0,1 ' ,adder([1,1]))

#deltaRule


learningRate = 0.001
noropt = [([1,1,1],0) , ([1,0,1],0),([0,1,1],0),([0,0,1],1)]
resul = []
for i in range(50100):
    nor_port.DeltaRule(noropt[0][0],learningRate,noropt[0][1])
    nor_port.DeltaRule(noropt[3][0],learningRate,noropt[3][1])
    nor_port.DeltaRule(noropt[1][0],learningRate,noropt[1][1])
    nor_port.DeltaRule(noropt[2][0],learningRate,noropt[2][1])

    time.sleep(0)


    #print(nor_port)

resul.append(nor_port.result([0,0,1]))
resul.append(nor_port.result([1,0,1]))
resul.append(nor_port.result([0,1,1]))
resul.append(nor_port.result([1,1,1]))

resul = tobin(resul)

print("00 gives = ",resul[0])
print("10 gives = ",resul[1])
print("01 gives = ",resul[2])
print("11 gives = ",resul[3])
#working(nor poort)
