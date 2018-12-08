# -*- coding: utf-8 -*-
"""
Created on Fri Dec 07 23:43:13 2018

@author: davidcamara
"""

import sys,os
import numpy as np

sys.path.append(os.path.dirname(os.path.realpath("../../GeneticAlgh")))

from GeneticAlgh.heuristic_calculation.evaluation.evaluation import Evaluation
from eli.elitism_knack import Elitism_knack

class Eval_knack(Evaluation):
    
    def __init__(self,limit):
        self.limit = limit
        self.fittiest = Elitism_knack(self.limit)

    def heuristic(self,pop):
        beforeConversion = pop.population.copy()
        pop.conversion()
        result = self.isDownLimit(pop)
        sumValue = self.sumTheValues(pop)
        self.fittiest.saveFitiest(pop,result,sumValue)        
        pop.setPopulation(beforeConversion)
        return False
        
    def isDownLimit(self,pop):
        chroResults = np.zeros((1,pop.numChromosomes)).ravel().astype(int)
        for chro in range(pop.numChromosomes):
            chroResults[chro] = np.any(pop.population[chro] <= self.limit)
        return chroResults
    
    def sumTheValues(self,pop):
        populationCopy = pop.population.copy()
#        print(pop.population)
        values = np.zeros((1,pop.numChromosomes)).ravel().astype(int)
        for chro in range(pop.numChromosomes):
            chromosome = populationCopy[chro]
#            print(chromosome)
            values[chro] = pop.getChroSumValue(chromosome)
        return values                
        
            
            
            
    