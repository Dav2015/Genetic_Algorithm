# -*- coding: utf-8 -*-
"""
Created on Sat Dec 08 02:50:33 2018

@author: davidcamara
"""

from pop.pop_knack import Pop_knack
from evalu.eval_knack import Eval_knack
from GeneticAlgh.selection.tournament import Tournament
from GeneticAlgh.recomendation.crossover.crossover import Crossover
from GeneticAlgh.recomendation.mutation.mutation import Mutation
from GeneticAlgh.geneticAlghMain import GeneticAlgh

#(wieght,value)
objects = {
		5 : 10 ,
		10 : 40,
		3 : 50,
		12 : 75,
      8 : 10,
      2 : 50
	}

pop = Pop_knack(4,objects)
pop.populate()
print(pop.population)

mut = Mutation(0.9)

newPop = mut.execute(pop)

print(newPop.population)




