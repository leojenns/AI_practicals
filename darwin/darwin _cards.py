import random
import operator
from functools import reduce 

def fitness(p1,p2):
    mistakesum=abs(sum(p1)-10)    
    mistakeprod=abs(reduce(operator.mul,p2,1)-360)
    return mistakesum+mistakeprod

def champ(population):
    x = min(population, key = population.get)
    return {x: population[x]}


def reproduce(champa,second):
    
    champlist = list(champa.keys())[0]
    
    champslist = champlist[0] + champlist[1]
    secondlist = list(second.keys())[0] 
    secondslist = secondlist[0] + secondlist[1]

    firstborn=(champslist[:len(secondlist[0])],champslist[-len(secondlist[1]):])
    
    firstbornscore = fitness(firstborn[0],firstborn[1])
    secondborn=(secondslist[:len(champlist[0])],secondslist[-len(champlist[1]):])
    
    secondbornscore = fitness(secondborn[0],secondborn[1])


    return [{firstborn:firstbornscore},{secondborn:secondbornscore}]



def mutate(x):
    l0 =list(list(x.keys())[0][0])
    l1 =list(list(x.keys())[0][1])
    if(random.randint(0,1)):
        random.shuffle(l0)
        random.shuffle(l1)

    l=l0+l1
    ll1=len(l0)-1
    m=0
    if(ll1!=0 and ll1!=9):
        m=random.randint(-1,1)
    ll1+=m
    l0 = l[-ll1:]
    l1 = l[:ll1]
    return {(tuple(l0),tuple(l1)):fitness(l0,l1)}
    

def ChangePopulation(population):
    newpopulation = {}
    champion = champ(population)
    k = list(champion.keys())[0]
    del population[k]
    newpopulation.update(champion)

    for x in range (5):
        second = champ(population)
        k = list(second.keys())[0]
        del population[k]
        newpopulation.update(second)
        children = reproduce(champion,second)
        newpopulation.update(children[0])
        newpopulation.update(children[1])
        newpopulation.update(mutate(children[1]))
        newpopulation.update(mutate(children[0]))

    return newpopulation




population={}

for _ in range(20):
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.shuffle(cards)
    slice = random.randint(1, 9)
    

    _0 = tuple(cards[:slice])
    _1 = tuple(cards[slice:])
    population[(_0, _1)] = fitness(_0, _1)

for _ in range(100):
    population = ChangePopulation(population)
    print(population)
