class Lock:
	def __init__(self, index, imagefile, coordinates, size):
		"""
		Creates a lock object, assigns an index value to it, takes image from image list to change the background, sets its coordinates and dimensions, sets self.locked bullion value as True to indicate that the lock object has not been unlocked
		ParamList: self (self), index (int), imagefile (string), coordinates (tuple), size (list)
		Returns: none
		"""
		self.id = index
		self.image = imagefile
		self.top_x = coordinates[0]
		self.top_y = coordinates[1]
		self.width = size[0]
		self.height = size[1]
		self.locked = True

	def isUnlocked(self):
		"""
		Changes self.locked bullion value to False to indicate that the lock object has been unlocked and makes it disappear from the view
		ParamList: self (self)
		Returns: none
		"""
		self.locked = False
		self.top_x = 0
		self.top_y = 0
		self.width = 0
		self.height = 0
