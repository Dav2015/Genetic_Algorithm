# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 19:32:11 2018

@author: davidcamara
"""
import numpy as np

from selection import Selection

class Tournament(Selection):

    def execute(self,popClass):
        newPopClass = self.makeTournament(popClass)
        return newPopClass

    def createRandomSelection(self,numChro):
        selecArr = np.random.randint(0,numChro,numChro*2)
        selecArr = selecArr.reshape((numChro,2))
        return selecArr

    def makeTournament(self,popClass):
        numChro = popClass.numChromosomes
        numGenes = popClass.numGenes
        selectRandomArr = self.createRandomSelection(numChro)
        selectPopulation = np.zeros((numChro,numGenes))
        for ch in range(numChro):
            tourChromo0 = selectRandomArr[ch][0]
            tourChromo1 = selectRandomArr[ch][1]
            selected = np.min([tourChromo0,tourChromo1])
            selectPopulation[ch] = popClass.population[selected]
        popClass.setPopulation(selectPopulation.astype(int))
        return popClass
