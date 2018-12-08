# -*- coding: utf-8 -*-
"""
Created on Fri Dec 07 17:22:39 2018

@author: davidcamara
"""

from pop.pop_knack import Pop_knack
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

