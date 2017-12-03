class Puzzle:
	def __init__(self, index, coordinates, buttonList):
		self.id = index
		self.top_x = coordinates[0]
		self.top_y = coordinates[1]
		self.bottom_x = coordinates[2]
		self.bottom_y = coordinates[3]
		self.buttonList = buttonList

		puzzle_rect = pygame.Rect(self.top_x, self.top_y, self.bottom_x, self.bottom_y)

		if self.id = 1:
			puzzle_1 = self.id
		elif self.id = 2:
			puzzle_2 = self.id
		elif self.id = 3:
			puzzle_3 = self.id
		elif self.id = 4:
			puzzle_4 = self.id
	
	def first_puzzle(self):
		self.red_comp = pygame.draw.rect("lab1.png", (255, 0, 0), (20,20,40,40),0)
		self.blue_comp = pygame.draw.rect("lab1.png", (0, 50, 255), (30,30,40,40),0)
		self.green_comp = pygame.draw.rect("lab1.png", (0, 255, 0), (40,40,40,40),0)
		self.yellow_comp = pygame.draw.rect("lab1.png", (255, 255, 0), (50,50,40,40),0)


	def isComplete(self):
		for button in buttonList:
			if button.isCorrect() == False:
				return False
		return True

	
