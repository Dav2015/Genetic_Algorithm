# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 17:37:28 2018

@author: davidcamara
"""

import numpy as np

from selection.tournament import Tournament
from heuristic_calculation.heuristic.keenEvaluation import keenEvaluation
from population.population import Population
from recomendation.mutation.mutation import Mutation

pop = Population(4,4)
pop.populate()
evalu = keenEvaluation()
selection = Tournament(0.1)
mutation = Mutation(1)


print("population",pop.population)
pop = mutation.execute(pop)
print("mutPop",pop.population)


