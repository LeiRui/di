#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

from Levenshtein import Levenshtein
import numpy as np
import math

def sim(tx,ty):
	"linear weighted similarity"
	w=[0.1 for x in range(10)]
	w[0]=0.5
	s=[0 for x in range(10)]
	for i in {0}:
		s[i]=Levenshtein.Jaro_Winkler(tx[i],ty[i])
	for i in range(1,9):
		s[i]=Levenshtein.edit_sim(tx[i],ty[i])
	if tx[9]==ty[9]: #exact match
		s[9]=1
	else:
		s[9]=0
	return np.dot(w,s)
	
def logistic_sim(tx,ty):
	return 1/(1+math.exp(-sim(tx,ty)))
	
def sim_only_name(tx,ty):
	return Levenshtein.Jaro_Winkler(tx[0],ty[0])		

def sim_simple(tx,ty):
	z=Levenshtein.Jaro_Winkler(tx[0],ty[0])*0.5+Levenshtein.edit_sim(tx[1],ty[1])*0.5
	return 1/(1+math.exp(-z))
