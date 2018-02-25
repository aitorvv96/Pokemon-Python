#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

"""

# Local imports
from Game.settings import Display_Config
from Game.utils_data_base import load_image, load_background
from .utils_display import pair_mult_num, scale, scale_bg

# 3rd party imports
import pygame

__version__ = '0.7'
__author__  = 'Daniel Alcocer (daniel.alcocer@est.fib.upc.edu)'


"""

"""
class Image(pygame.sprite.Sprite):
	def __init__(self, image, top_left_location):
		pygame.sprite.Sprite.__init__(self)
		self._image = image
		self._location = top_left_location

	def display(self,SCREEN):
		SCREEN.blit(self._image, self._location)

class Background(Image):
	def __init__(self, image_file, top_left_location = [0,0]):
		image = load_background(image_file)
		factor = Display_Config['BACKGROUND_SCALE']
		final_image =  pygame.transform.scale(image, scale_bg(image.get_size()))
		location = scale_bg(top_left_location)
		Image.__init__(self,final_image,location)

class Display:
	def __init__(self, visualize_items):
		self._visualize_items = visualize_items

	def display(self, SCREEN):
		for surface in self._visualize_items:
			surface.display(SCREEN)
