class Button:
	def __init__(self, index, imageList, coordinates, correctNum, maxNum):
		self.clickNum = 0
		self.correctNum = 3
	
	def clicked(self):
		if self.clickNum = maxNum:
			self.clickNum = 0
		else:
			self.clickNum += 1
		self.image = self.imageList[self.clickNum]
