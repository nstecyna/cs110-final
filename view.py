import pygame

class View:
	def __init__(self, index, coordinates, imagelist, puzzlelist, keylist, locklist):
		self.id = index
		self.background = pygame.image.load(img_file).convert_alpha()
		self.imagelist = imagelist
		self.puzzle = puzzlelist
		self.key = keylist
		self.lock = locklist

		self.top_x = coordinates[0]
		self.top_y = coordinates[1]
		self.bottom_x = coordinates[2]
		self.bottom_y = coordinates[3]

		leftside_rect1 = pygame.Rect(self.top_x, self.top_y, self.bottom_x, self.bottom_y)
		rightside_rect1 = pygame.Rect(self.top_x + 100, self.top_y, self.bottom_x + 100, self.bottom_y)		

		if self.id = 1:
			self.puzzle_coor_x1 = coordinates[x]
			self.puzzle_coor_y1 = coordinates[y]
			self.puzzle_coor_x2 = coordinates[x]
			self.puzzle_coor_y2 = coordinates[y]
			puzzle_rect = pygame.Rect(self.puzzle_coor_x1, self.puzzle_coor_y1, self.puzzle_coor_x2, self.puzzle_coor_y2)

		elif self.id = 2:
			self.puzzle_coor_x1 = coordinates[x]
			self.puzzle_coor_y1 = coordinates[y]
			self.puzzle_coor_x2 = coordinates[x]
			self.puzzle_coor_y2 = coordinates[y]
			puzzle_rect = pygame.Rect(self.puzzle_coor_x1, self.puzzle_coor_y1, self.puzzle_coor_x2, self.puzzle_coor_y2)

		elif self.id = 3:
			self.puzzle_coor_x1 = coordinates[x]
			self.puzzle_coor_y1 = coordinates[y]
			self.puzzle_coor_x2 = coordinates[x]
			self.puzzle_coor_y2 = coordinates[y]
			puzzle_rect = pygame.Rect(self.puzzle_coor_x1, self.puzzle_coor_y1, self.puzzle_coor_x2, self.puzzle_coor_y2)

		elif self.id = 4:
			self.puzzle_coor_x1 = coordinates[x]
			self.puzzle_coor_y1 = coordinates[y]
			self.puzzle_coor_x2 = coordinates[x]
			self.puzzle_coor_y2 = coordinates[y]
			puzzle_rect = pygame.Rect(self.puzzle_coor_x1, self.puzzle_coor_y1, self.puzzle_coor_x2, self.puzzle_coor_y2)


	def display_room1(self, "lab1.jpg", "lab2.jpg", "lab3.jpg", "lab4.jpg", coordinates): #instance_variables):
		if self.id 






