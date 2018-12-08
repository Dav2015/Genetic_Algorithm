# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 14:30:28 2018

@author: davidcamara
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 19:35:39 2018

@author: davidcamara
"""
import numpy as np

from selection.tournament import Tournament
from KeenProblem.evaluation.keenEvaluation import KeenEvaluation
from population.population import Population
from recomendation.crossover.crossover import Crossover

popClass = Population(4,4)
popClass.populate()

evalu = KeenEvaluation()

cross = Crossover()


crossoverPopulation = np.zeros((popClass.numChromosomes,popClass.numGenes))
for ch in range(0,popClass.numChromosomes-1,2):
    parent0 = popClass.population[ch]
    parent1 = popClass.population[ch+1]
    print("parent",parent0,parent1)
    
#    create childs
    childs = [0,0]
    for child in range(len(childs)):
        randomGens = np.random.randint(0,2,popClass.numGenes)    
        gensFromParent0 = np.where(randomGens==0)[0]
        gensFromParent1 = np.where(randomGens==1)[0]    
        createdChild = np.zeros((1,popClass.numGenes)).ravel()
        createdChild[gensFromParent0] = parent0[gensFromParent0]
        createdChild[gensFromParent1] = parent1[gensFromParent1]
        childs[child] = createdChild
    print("child:",childs)
        
    crossoverPopulation[ch] = childs[0]
    crossoverPopulation[ch+1] = childs[1]
    
if popClass.numChromosomes % 2 !=0:
    crossoverPopulation[-1] = popClass.population[-1]
print("oldPop",popClass.population)
popClass.setPopulation(crossoverPopulation.astype(int))
print("newPop",popClass.population)


   
    
#print("pop:",pop.pop)
#print("newPOP:",newPop)
    
        

        
       

    
    
    
    
    
    
    












