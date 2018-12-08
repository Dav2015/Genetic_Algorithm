# -*- coding: utf-8 -*-
"""
Created on Sat Dec 08 09:07:58 2018

@author: davidcamara
"""

from GeneticAlgh.recomendation.mutation.mutation import Mutation

class Mut_knack(Mutation):
    
    def __mutation(self,popClass):
        newPopClass = Mutation.__mutation(self)
        newPopClass.conversion()
        return new
        
        