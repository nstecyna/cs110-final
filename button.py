class Button:
	def __init__(self, index, imageList, coordinates, size, correctNum, maxNum):
		self.id = index
		self.imageList = imageList
		self.top_x = coordinates[0]
		self.top_y = coordinates[1]
		self.width = size[0]
		self.weight = size[1]
		self.clickNum = 0
		self.correctNum = correctNum
		self.maxNum = maxNum

	def clicked(self):
		if self.clickNum == maxNum:
			self.clickNum = 0
		else:
			self.clickNum += 1
		self.image = self.imageList[self.clickNum]

	def isCorrect():
		return self.clickNum == self.correctNum
