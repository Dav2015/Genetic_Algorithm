# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 13:00:35 2018

@author: davidcamara
"""
import sys,os

sys.path.append(os.path.dirname(os.path.realpath("")))

from GeneticAlgh.selection.tournament import Tournament
from GeneticAlgh.recomendation.mutation.mutation import Mutation
from GeneticAlgh.recomendation.crossover.crossover import Crossover
from GeneticAlgh.geneticAlghMain import GeneticAlgh

from KeenProblem.evaluation.keenEvaluation import KeenEvaluation
from KeenProblem.keenPop.keenPop import KeenPop

"Fork and RUN"
pop = KeenPop(50,6)
pop.populate()
selection = Tournament()
evalu = KeenEvaluation()
cross = Crossover(0.9)
mutation = Mutation(0.9)
keen = GeneticAlgh(sys.maxsize,pop,evalu,selection,cross,mutation)
solution = keen.execute()
print(solution)






