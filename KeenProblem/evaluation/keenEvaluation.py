# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 14:45:46 2018

@author: davidcamara
"""

#import sys,os
#sys.path.append(os.path.dirname(os.path.realpath("../../GeneticAlgh")))

from GeneticAlgh.heuristic_calculation.evaluation.evaluation import Evaluation
from KeenProblem.keenElitism.keenElitism import KeenElitism

import numpy as np

class KeenEvaluation(Evaluation):
    
    def __init__(self):
        self.fittiest = KeenElitism()
            
    def heuristic(self,population):
        attacks = self.attacks(population)    
    
        self.fittiest.saveFitiest(attacks,population)
        if self.fittiest.getAttacks() == 0:
            return True
        return False
        
    def attacks(self,population):
        attacks = np.zeros((population.numChromosomes,1))
        for chro in range(population.numChromosomes):
#            print("chro = ",chro)
            chromosome = population.population[chro]
            table = population.representChromosome(chromosome)
            attacks[chro][0] = self.countAttacks(chromosome,table)
        return attacks
                    
    def countAttacks(self,chromosome,table):
        counterA = 0;
        counterA += self.checkHorizontalAttack(table)
        counterA += self.checkVerticalAttack(table)
        counterA += self.checkDiagonalAttack(chromosome)
#        print(counterA)
        return counterA
            
          
    def checkHorizontalAttack(self,table):
#        count all the ones that are in the same 
#        line minus the keen that we are checking
        result = np.sum(table,axis=-1)
        idx = np.where(result>=2)[0]
        attacks = np.sum(result[idx])-len(idx)
#        print("hor",attacks)
        return attacks
    
    def checkVerticalAttack(self,table):
#        count all the ones that are in the same 
#        line minus the keen that we are checking
        result = np.sum(table,axis=0)
        idx = np.where(result>=2)[0]
        attacks = np.sum(result[idx])-len(idx)
#        print("hor",attacks)
        return attacks
    
    def checkDiagonalAttack(self,chromosome):
        counterA = 0
#        print("chromo",chromosome)
        for genCol in range(len(chromosome)):
            genRow = chromosome[genCol]
            genKeen = genCol+genRow
            for nextGenCol in range(genCol+1,len(chromosome)):
                nextGenRow = chromosome[nextGenCol]
                nextGenKeen = nextGenCol + nextGenRow

                difCol = nextGenCol-genCol
                difRow = nextGenRow-genRow
#                print([genRow,genCol],[nextGenRow,nextGenCol])
                if genKeen == nextGenKeen or (difCol - difRow) == 0:
                    counterA = counterA + 1
#                    print("upDown",genKeen==nextGenKeen)
#                    print("DownUp",difCol-difRow==0)
#                    print("")
#        print("dig",counterA)
        return counterA
                
            
        
            
        
        
         
        
        
        
            
                        
        
        
        
        
        
    
    
    
        
    