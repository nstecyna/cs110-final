class Button:
	def __init__(self, index, imagelist, coordinates, size, correctNum, maxNum):
		"""
		Creates button object, assigns an index value to it, takes image from image list, 
		ParamList: self (self), index (int), imagelist (list), coordinates (tuple), size (list), correctNum (int), maxNum (int)
		Returns: none
		"""
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
		"""
		Appends the self.clickNum value or resets it back to zero depending on whether or not it equals the maxNum value
		ParamList: self (self)
		Returns: none
		"""
		if self.clickNum == self.maxNum:
			self.clickNum = 0
		else:
			self.clickNum += 1
		if len(self.imagelist): # if the list has values (if it's not a certain order puzzle)
			self.image = self.imagelist[self.clickNum]

	def isCorrect(self):
		"""
		Returns self.clickNum as self.correctNum
		ParamList: self (self)
		Returns: self.clickNum == self.correctNum
		"""
		return self.clickNum == self.correctNum

	def isRemoved(self):
		"""
		Removes the button object from the view
		ParamList: self (self)
		Returns: none
		"""
		self.top_x = 0
		self.top_y = 0
		self.width = 0
		self.height = 0
		self.image = ''
