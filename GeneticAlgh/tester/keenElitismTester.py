# -*- coding: utf-8 -*-
"""
Created on Tue Dec 04 18:01:39 2018

@author: davidcamara
"""


from selection.tournament import Tournament
from KeenProblem.evaluation.keenEvaluation import KeenEvaluation
from population.population import Population
from recomendation.mutation.mutation import Mutation
from recomendation.crossover.crossover import Crossover

from geneticAlghMain import GeneticAlgh

pop = Population(4,4)
pop.populate()
evalu = KeenEvaluation()
cross = Crossover(0.8)
selection = Tournament(0.1)
mutation = Mutation(1)

keen = GeneticAlgh(pop,evalu,selection,cross,mutation)

solution = keen.execute()



