#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Module that contains useful functions to work with images
and do some calculations.

This module contains the following functions to import to another classes:

	pair_mult_num
	scale
	scale_bg
	center_to_top_left
	final_scale
	transalte
	num_to_text
"""

# Local imports
from Game.settings import Display_Config

__version__ = '0.7'
__author__  = 'Daniel Alcocer (daniel.alcocer@est.fib.upc.edu)'



def pair_mult_num(pair, num):
	return (int(pair[0]*num),int(pair[1]*num))

def scale(pair):
	return pair_mult_num(pair, Display_Config['SCALE'])

def scale_bg(pair):
	fact = Display_Config['SCALE']*Display_Config['BACKGROUND_SCALE']
	return (int(pair[0]*fact), int(pair[1]*fact))

def center_to_top_left(pos, sprite_size):
	return (pos[0]-sprite_size[0]/2,pos[1]-sprite_size[1]/2)

def final_scale(pair, factor):
	fact = Display_Config['SCALE']*factor
	return (int(pair[0]*fact), int(pair[1]*fact))

def transalte(pos, desp):
	return (pos[0]+desp[0],pos[1]+desp[1])

def num_to_text(num,max_digits=2):
	s_num= str(num)
	if len(s_num) < max_digits:
		spaces = max_digits-len(s_num)
		for i in range(0,spaces):
			s_num = ' '+s_num
	return s_num