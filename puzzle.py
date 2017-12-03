class Puzzle:
	def __init__(self, index, coordinates, size, buttonList):
		self.id = index
		self.top_x = coordinates[0]
		self.top_y = coordinates[1]
		self.width = size[0]
		self.weight = size[1]
		self.buttonList = buttonList

	def isComplete(self):
		for button in buttonList:
			if button.isCorrect() == False:
				return False
		return True
