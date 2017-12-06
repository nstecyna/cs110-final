import pygame

class View:
	def __init__(self, index, background, coordinates, size, viewlist, puzzlelist, keylist, locklist, notelist):
		self.id = index
		self.background = background
		self.top_x = coordinates[0]
		self.top_y = coordinates[1]
		self.width = size[0]
		self.height = size[1]
		self.viewlist = viewlist
		self.puzzlelist = puzzlelist
		self.keylist = keylist
		self.locklist = locklist
		self.notelist = notelist
