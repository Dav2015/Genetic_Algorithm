# -*- coding: utf-8 -*-
"""
Created on Sat Dec 08 02:19:00 2018

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
		12 : 75
	}

pop = Pop_knack(3,objects)
pop.populate()
evalu = Eval_knack(20)

select = Tournament()

newPop = select.execute(pop)