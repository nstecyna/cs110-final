import pygame

class View:
	def __init__(self, index, background, puzzlelist, keylist, locklist):
		self.id = index
		self.background = background
		self.puzzlelist = puzzlelist
		self.keylist = keylist
		self.locklist = locklist
