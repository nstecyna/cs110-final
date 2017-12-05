class Puzzle:
	def __init__(self, index, buttonlist):
		self.id = index
		self.buttonlist = buttonlist

	def isComplete(self):
		for button in self.buttonlist:
			if button.isCorrect() == False:
				return False
		return True
