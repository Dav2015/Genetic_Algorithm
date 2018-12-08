# -*- coding: utf-8 -*-
"""
Created on Sat Dec 08 01:39:48 2018

@author: davidcamara
"""
import sys,os
sys.path.append(os.path.dirname(os.path.realpath("")))

from GeneticAlgh.selection.tournament import Tournament
from GeneticAlgh.recomendation.crossover.crossover import Crossover
from GeneticAlgh.recomendation.mutation.mutation import Mutation
from GeneticAlgh.geneticAlghMain import GeneticAlgh

from pop.pop_knack import Pop_knack
from evalu.eval_knack import Eval_knack


#(wieght,value)
objects = {
		8 : 10 ,
		6 : 20,
		4 : 30,  
		2 : 40,
      30 : 40
	}

pop = Pop_knack(50,objects)
pop.populate()
evalu = Eval_knack(40)
select = Tournament()
cross = Crossover(0.9)
mutation = Mutation(0.9)
gene = GeneticAlgh(5000,pop,evalu,select,cross,mutation)

print(gene.execute())







