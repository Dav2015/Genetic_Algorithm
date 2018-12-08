# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 14:05:36 2018

@author: davidcamara
"""

import numpy as np

class Population(object):

  def __init__(self,numChromosomes,numGenes):
    self.numGenes = numGenes
    self.numChromosomes = numChromosomes
    self.population = np.zeros((self.numChromosomes,self.numGenes)).astype(int)

  def populate(self):
      ''''Start the population randomly'''
      for row in range(self.numChromosomes):
          for col in range(self.numGenes):
              genePos = np.random.randint(0,self.numGenes)
              self.population[row][col] = genePos

  def representChromosome(self,chromosome):
      ''''Implement!'''
      abstract

  def setPopulation(self,population):
      self.population = population
