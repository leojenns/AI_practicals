from libnn.nn import *



## nor poort
NOR = Neuron(-0.5, [-1,-1])
## not poort
NOT = Neuron(0, [-1])
## and poort
AND = Neuron(1, [-0.5,-0.5])
## or poort
OR  = Neuron(0.5, [0.5,0.5])
## nand poort
NAND = Neuron(-0.5, [-0.5,-0.5])



##norpoort test:

print(" [1,1] -> False ", NOR.result([1, 1]))
print(" [1,0] -> False ", NOR.result([1, 0]))
print(" [0,1] -> False ", NOR.result([0, 1]))
print(" [0,0] -> False ", NOR.result([0, 0]))


##adder:


def adder(input):
     adder_sum  = NAND.result(
        [NAND.result([NAND.result(input),input[0]]),
         NAND.result([NAND.result(input),input[1]])
        ]
    )
     carrying_bit  = NAND.result([NAND.result(input),NAND.result(input)])
     return [adder_sum,carrying_bit ]


#adder test:

print('adder > [0,0]> 0,0 ' ,adder([0,0]))
print('adder > [1,0]> 1,0 ' ,adder([1,0]))
print('adder > [0,1]> 1,0 ' ,adder([0,1]))
print('adder > [1,1]> 0,1 ' ,adder([1,1]))
