# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 14:03:10 2018

@author: davidcamara
"""
import sys

sys.path.append("/heuristic_calculation")
sys.path.append("/population")

class GeneticAlgh(object):

    def __init__(self,maxIterations,popClass,evaluClass,selection,crossover,mutation):
#    def __init__(self,population,evaluation,selection):
        self.maxIterations = maxIterations
        self.popClass = popClass
        self.evalu = evaluClass
        self.select = selection
        self.cross = crossover
        self.mut = mutation

    def execute(self):
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
        return self.popClass.representChromosome(chromosome)

    def randomPopulate(self):
        self.popClass.populate()

    def evaluation(self):
#        heuristic here
        result = self.evalu.heuristic(self.popClass)
#        print("")
#        print("evaluation",evaluationResults,result)
        return result

    def selection(self):
        self.select.execute(self.popClass)

    def crossover(self):
        self.cross.execute(self.popClass)

    def mutation(self):
        self.mut.execute(self.popClass)
