import random
import operator
from functools import reduce 

"""
script for running evolution algorithm applied to two pilesof cards going from 1 to 10

including repproduction and mutaion 

"""


def fitness(p1,p2):
    """Fitness function

    :param p1: list of int pile 1  
    :param p2: list of int pile 2
    :returns:  fitness number
    :rtype:    int

    """
    mistakesum=abs(sum(p1)-10)    #sum of p1 disstance of 10
    mistakeprod=abs(reduce(operator.mul,p2,1)-360) # mul of p2  distance to 360
    return mistakesum+mistakeprod # return the total distance of bofe piles

def champ(population):
    """Getting best individual of population

    :param population:  population dict {}
    :returns: best individual
    :rtype: dict

    """
    x = min(population, key = population.get) # lowest fitness number is best individual
    return {x: population[x]} # return the best individual


def reproduce(champa,snd):
    """ evolve function make children of best two individuals

    :param champa: individual best of the population
    :param snd: individual snd best of the population
    :returns: two new individuals made of the champa and the snd 
    :rtype: list of dict

    """
    
    champlist = list(champa.keys())[0] #piles of champa 
    
    champslist = champlist[0] + champlist[1] # combine piles to total pile 
    sndlist = list(snd.keys())[0] #piles of snd
    sndslist = sndlist[0] + sndlist[1] # combine piles to total pile 

    """
    split the champslist on the length of first pile of snd
    and second pile snd
    """
    firstborn=(champslist[:len(sndlist[0])],champslist[-len(sndlist[1]):]) 
    
    firstbornscore = fitness(firstborn[0],firstborn[1])
    """
    split sndslist on length of first pile of champa and second pile of champa  
    """ 
    sndborn=(sndslist[:len(champlist[0])],sndslist[-len(champlist[1]):])
    
    sndbornscore = fitness(sndborn[0],sndborn[1])


    return [{firstborn:firstbornscore},{sndborn:sndbornscore}]



def mutate(x):
    """mutate a individual

    :param x: individual 
    :returns: new individual
    :rtype:  dict

    """
    #make list of piles
    p0 =list(list(x.keys())[0][0])
    p1 =list(list(x.keys())[0][1])
    # random bool shuffle p0 
    if(random.randint(0,1)):
        random.shuffle(p0)
    # random bool shuffle p1
    if(random.randint(0,1)):
        random.shuffle(p1)
    # add piles together 
    l=p0+p1
    # length of pile 0  minus 1 
    lp0=len(p0)-1
    #init m (int)
    m=0
    #if pile 0 shorter then 9 then add or substract 1 of len 
    if(lp0<9):
        m=random.randint(-1,1)
    lp0+=m
    #split piles again based on new len of pile 0 
    p0 = l[-lp0:]
    p1 = l[:lp0]
    #return mutant
    return {(tuple(p0),tuple(p1)):fitness(p0,p1)}
    

def ChangePopulation(population):
    """function for changing the population

    :param population: 
    :returns: newpopoulation
    :rtype: dict

    """
    #empty population
    newpopulation = {}
    #best of population
    champion = champ(population)
    #piles of champ
    k = list(champion.keys())[0]
    #delete champion of population
    del population[k]
    #add champion to new population
    newpopulation.update(champion)

    for x in range (5):
	#get second best 
        snd = champ(population)
        # get piles of snd best
        k = list(snd.keys())[0]
        # delete second best of population
        del population[k]
        #add second best to new population
        newpopulation.update(snd)
        # reproduce with best and second best  
        children = reproduce(champion,snd)
        #add children to new population
        newpopulation.update(children[0])
        newpopulation.update(children[1])
        #add mutated children to new population
        newpopulation.update(mutate(children[1]))
        newpopulation.update(mutate(children[0]))
    
    return newpopulation #return the new population



#empty population
population={}
#make base population
for _ in range(20):
    #new cards
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #shuffle the cards
    random.shuffle(cards)
    #slice cards
    slice = random.randint(1, 9)
    
    #make separte piles based on slice
    _0 = tuple(cards[:slice])
    _1 = tuple(cards[slice:])
    # add piles and the score of the piles to population
    population[(_0, _1)] = fitness(_0, _1)


# evolution on the base population with 100 iterations
for _ in range(100):
    #evolve
    population = ChangePopulation(population)
    #print new population
    print(population)
