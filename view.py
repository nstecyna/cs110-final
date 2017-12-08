import pygame

class View:
	def __init__(self, index, background, coordinates, size, viewlist, puzzlelist, keylist, locklist, notelist):
		"""
		Creates view object, assigns an index value to it, sets background from background image, sets its coordinates and dimensions, stores smaller views, puzzles, keys, locks, and notes in each of the different views from lists
		ParamList: self (self), index (int), background (string), coordinates (tuple), size (list), viewlist (list), puzzlelist (list), keylist (list), locklist (list), notelist (list)
		Returns: none
		"""
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
