# -*- coding: utf-8 -*-
"""
Created on Fri Dec 07 16:19:12 2018
@author: davidcamara
"""

import sys,os
import numpy as np


#sys.path.append(os.path.dirname(os.path.realpath("../../GeneticAlgh")))

from GeneticAlgh.population.population import Population 

class Pop_knack(Population):
    
    def __init__(self,numChromosomes,weightsValuesDict):
       Population.__init__(self,numChromosomes, len(weightsValuesDict))
       self.weightsValuesDict = weightsValuesDict

    def conversion(self):
       weights = self.weightsValuesDict.keys()
       populationCopy = self.population.copy()
       for w in range(len(weights)):
           row,col = np.where(self.population == w)
           populationCopy[row,col] = weights[w]
           
       self.setPopulation(populationCopy)
       
    def representChromosome(self,chromosome):
      backpack = chromosome.reshape(len(chromosome),1)
      return backpack
  
    def getChroValues(self,chromosome):
        values = np.zeros((1,self.numGenes)).ravel().astype(int)
        for chro in range(self.numGenes):
            values[chro] = self.weightsValuesDict.get(chromosome[chro])
        return values
    
    def getChroSumValue(self,chromosome):
        return np.sum(self.getChroValues(chromosome))
            
            
            
            
        