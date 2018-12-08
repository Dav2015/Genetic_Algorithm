# -*- coding: utf-8 -*-
"""
Created on Sat Dec 08 14:51:28 2018

@author: davidcamara
"""

import sys,os
import numpy as np


from GeneticAlgh.population.population import Population 

class KeenPop(Population):
    
  def representChromosome(self,chromosome):
      table = np.zeros((self.numGenes,self.numGenes))
      for col in  range(len(chromosome)):
          table[chromosome[col]][col] = 1
      return table