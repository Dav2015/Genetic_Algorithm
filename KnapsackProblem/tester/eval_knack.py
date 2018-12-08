# -*- coding: utf-8 -*-
"""
Created on Sat Dec 08 00:35:44 2018

@author: davidcamara
"""

from pop.pop_knack import Pop_knack
from evalu.eval_knack import Eval_knack
import numpy as np


#(wieght,value)
objects = {
		5 : 10 ,
		10 : 40,
		3 : 50,
		12 : 75
	}

pop = Pop_knack(3,objects)

pop.populate()

evalu = Eval_knack(20)

evalu.heuristic(pop)


