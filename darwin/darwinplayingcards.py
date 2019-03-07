from random import randint, shuffle
from copy import copy


class houseofcards:
    def __init__(self, l = [i for i in range(1,11)],part = random.randint(1,9) ):
        self.cards = l
        self.cut = cut
        self.society = []


    def str(self):
        return ("parts split is ", self.list[:self.part], ", " , self.list[self.part:] )


    def closest(self):
        fst     = self.list[:self.part]
        snd     = self.list[self.part:]
        return abs( 36 - sum(fst)), abs( 36 - sum(snd))

    def anabolic(self, x, y):
        sum_x = sum(x)
        mul_y = mult(y)
        return (abs(sum_x -36) + abs(mul_y -360))

    def get_the_kids(self, mam, dad):
        mams = mam[0]  + mam[1]
        paps = pap[0]  + pap[1]
        temp = list(map(len, [mam[0],mam[1],pap[0],pap[1]]))
        r_int = random.choice(r_int)
        kiddo_0 = (mams[r_int:],  paps[:r_int])
        r_int = random.choice(r_int)
        kiddo_1 = (mams[:r_int], paps[r_int:])
        return (kiddo_0, kiddo_1)



    def next_gen(self):
        next_generation = []
        champ = self.get_highest()
        next_generation.append(champ)
        for _ in range(5):
            snd = self.get_best()
            next_generation.append(snd)
            kids = get_the_kids(champ, snd)
            next_generation.append(kids[0])
            next_generation.append(kids[1])
            next_generation.append(mutants(kids[1]))
            next_generation.append(mutants(kids[0]))


    def mutants(self,kiddo):
        a = kiddo[0]
        b = kiddo[1]
        random.shuffle(a)
        random.shuffle(b)
        return

    def loop(self, count = 20):
        self.score_list = []
        self.society    = []
        for _ in range(count):

            self.cards = [i for i in range(1,11)]
            random.shuffle(self.cards)
            self.cut = random.randint(1,9)

            c_1 = self.cards[:self.cut]
            c_2 = self.cards[self.cut:]

            self.score_list += [anabolic(c_1, c_2)]
            self.society    += [(c_1, c_2)]


    def print_society(self, count = 100):
        for _ in range(count):
            self.society = self.next_gen()
            print(self.society)

    def get_best(self):
        temp = self.score_list.index(min(self.score_list))
        return self.soiety.pop(temp)


    def mult(self, lst, result = 1):
        if not lst:
            return result
        return mult(lst[1:],result * lst[0])
