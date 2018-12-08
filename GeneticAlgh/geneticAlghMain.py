# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 14:03:10 2018

@author: davidcamara
"""
import sys

sys.path.append("/heuristic_calculation")
sys.path.append("/population")

class GeneticAlgh(object):
    '''Main Class!'''

    def __init__(self,maxIterations,popClass,evaluClass,selection,crossover,mutation):
        self.maxIterations = maxIterations
        self.popClass = popClass
        self.evalu = evaluClass
        self.select = selection
        self.cross = crossover
        self.mut = mutation

    def execute(self):
        '''
        See the image in github in the same folder as this file
        while we dont have a result continue to select crossover and mutate
        '''
        self.randomPopulate()
        result = self.evaluation()
        result = False
        counter = 0
        while not result and counter <= self.maxIterations:
            self.selection()
            self.crossover()
            self.mutation()
            result = self.evaluation()
            counter += 1
        return self.solution(self.evalu.fittiest.getFitiest())

    def solution(self,chromosome):
        '''Put the solution in a visualization mode'''
        return self.popClass.representChromosome(chromosome)

    def randomPopulate(self):
        '''populate randomly'''
        self.popClass.populate()

    def evaluation(self):
        '''output the from the heuristic test'''
        result = self.evalu.heuristic(self.popClass)
        return result

    def selection(self):
        '''make selection'''
        self.select.execute(self.popClass)

    def crossover(self):
        '''make crossover'''
        self.cross.execute(self.popClass)

    def mutation(self):
        '''make mutation'''
        self.mut.execute(self.popClass)
