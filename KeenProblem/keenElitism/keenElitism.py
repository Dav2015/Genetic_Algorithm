# -*- coding: utf-8 -*-
"""
Created on Tue Dec 04 17:15:27 2018

@author: davidcamara
"""

from GeneticAlgh.elitism.elitism import Elitism

import numpy as np

class KeenElitism(Elitism):
    
    def __init__(self):
        self.minimumAttack = None
    
    def saveFitiest(self,attacks,population):
        attacks = attacks.astype(int)
        maybeMinAttacksIdx = np.where(attacks == np.min(attacks.ravel()))[0]
        maybeMinAttacksIdxUnique = np.unique(maybeMinAttacksIdx)[0]
        maybeMinAttack  = attacks[maybeMinAttacksIdxUnique][0]
        
        if maybeMinAttack < self.minimumAttack or self.minimumAttack is None:
            self.minimumAttack  = maybeMinAttack
#            print(self.minimumAttack)
#            print(population.population[maybeMinAttacksIdxUnique])
            self._setFitiest(population.population[maybeMinAttacksIdxUnique])
    
    def getAttacks(self):
        return self.minimumAttack
            
            