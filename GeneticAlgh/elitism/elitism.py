# -*- coding: utf-8 -*-
"""
Created on Tue Dec 04 16:42:13 2018

@author: davidcamara
"""

class Elitism:
    '''The best prevails
       Save the best chromosomes
    '''
    
    def __init(self):
        self.fitiest = None
        
    def saveFitiest(self,fitiest):
        '''what is the metric for the fitiest chromosome?'''
        abstract
    
    def getFitiest(self):
        return self.fitiest
    
    def _setFitiest(self,newFit):
        self.fitiest = newFit
        
    
    