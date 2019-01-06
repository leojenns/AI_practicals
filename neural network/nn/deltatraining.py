from libnn import *


xor = Network([Neuron([0.2, -0.4]),Neuron([0.7,0.1])] , (Network([Neuron([0.6,0.9])])))








print(xor.result([0,1]))
#xor.learn_threshold([1,1])
print("first learning")
xor.learn([1,1],0.1,[0])



xor.print_weights()

xor.learn([1,0],0.1,[1])
print("\n\n")
xor.print_weights()




'''

recursiefe functie die van (int , int , gewicht van int ) -> gewicht te voegt aaan bepaald neuron om zo bais te crearen
laag , neuron , gewicht
'''
