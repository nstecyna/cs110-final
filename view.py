import pygame

class View
	def __init__(self, index, imagelist, puzzlelist, keylist, locklist):
		self.id = index
		self.background = pygame.image.load(img_file).convert_alpha()
		self.imagelist = imagelist
		self.puzzle = puzzlelist
		self.key = keylist
		self.lock = locklist
	def display_room1(self, #instance_variables):
		#images/room1.png







