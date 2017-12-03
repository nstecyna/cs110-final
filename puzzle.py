class Puzzle:
	def __init__(self, index, coordinates, size, buttonlist):
		self.id = index
		self.top_x = coordinates[0]
		self.top_y = coordinates[1]
		self.width = size[0]
		self.height = size[1]
		self.buttonlist = buttonlist

	def isComplete(self):
		for button in buttonlist:
			if button.isCorrect() == False:
				return False
		return True
