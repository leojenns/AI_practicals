from random import randint, shuffle
from copy import copy


class cards:
    def __init__(self, l = [i for i in range(1,11)],part = None ):
        self.list = l
        self.part = part

    def str(self):
        return ("parts split is ", self.list[:self.part], ", " , self.list[self.part:] )


    def closest(self):
        fst     = self.list[:self.part]
        snd     = self.list[self.part:]
        return abs( 36 - sum(fst)), abs( 36 - sum(snd))

    def anabolic(self):
        shuffled = copy(self.list)
        shuffle(shuffled)
        new_parts = randint(0,10)

        opt1 = cards(l = shuffled , part = self.part)
        opt2 = cards(l = self.list, part = new_parts)
        opt3 = cards(l = shuffled , part = new_parts)
        opt4 = cards(l = self.list, part = self.part)
