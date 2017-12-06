class Button:
	def __init__(self, index, imagelist, coordinates, size, correctNum, maxNum):
		self.id = index
		self.imagelist = imagelist
		self.image = ''
		if len(self.imagelist): # checks if there's anything in the list
			self.image = imagelist[0]
		self.top_x = coordinates[0]
		self.top_y = coordinates[1]
		self.width = size[0]
		self.height = size[1]
		self.clickNum = 0
		self.correctNum = correctNum
		self.maxNum = maxNum

	def clicked(self):
		if self.clickNum == self.maxNum:
			self.clickNum = 0
		else:
			self.clickNum += 1
		self.image = self.imagelist[self.clickNum]

	def isCorrect(self):
		return self.clickNum == self.correctNum
