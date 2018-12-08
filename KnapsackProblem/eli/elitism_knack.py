# -*- coding: utf-8 -*-
"""
Created on Sat Dec 08 00:22:44 2018

@author: davidcamara
"""

import sys,os
import numpy as np

sys.path.append(os.path.dirname(os.path.realpath("../../GeneticAlgh")))

from GeneticAlgh.elitism.elitism import Elitism

class Elitism_knack(Elitism):
    
    def __init__(self,limit):
        self.limit = limit
        self.minWeight = 0
        self.maxValue = 0
        self.chromosome = 0
                
    def saveFitiest(self,pop,result,sumValue):
        for chro in range(pop.numChromosomes):
            if result[chro] and (sumValue[chro] > self.maxValue):
                self.minWeight = np.sum(pop.population[chro])
                self.maxValue = sumValue[chro]
                self.chromosome = pop.population[chro].copy()
        
    def getFitiest(self):
        return self.chromosome
    
    