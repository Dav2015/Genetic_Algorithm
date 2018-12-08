# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 17:27:19 2018

@author: davidcamara
"""
import numpy as np

from GeneticAlgh.recomendation.recomendation import Recomendation

class Mutation(Recomendation):

    def execute(self,popClass):
        newPopClass = self.__mutation(popClass)
        return newPopClass

    def __mutation(self,popClass):
        '''choose a gene and  mutate randomly'''
        for chro in range(popClass.numChromosomes):
            if self.probUse > np.random.rand():
                randomGen = np.random.randint(0,popClass.numGenes)
                randomIdx = np.random.randint(0,popClass.numGenes)
                popClass.population[chro][randomIdx] = randomGen
        return popClass
