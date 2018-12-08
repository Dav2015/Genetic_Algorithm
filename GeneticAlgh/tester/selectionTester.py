# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 19:35:39 2018

@author: davidcamara
"""
import numpy as np

from selection.tournament import Tournament
from heuristic_calculation.heuristic.keenEvaluation import keenEvaluation
from population.population import Population

pop = Population(4,4)
pop.populate()
evalu = keenEvaluation()
selection = Tournament(0.1)


attacks,result = evalu.heuristic(pop)
print("attacks:",attacks)
print(pop.population)
print("")
print(selection.execute(pop,attacks).population)


