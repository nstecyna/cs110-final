class Lock:
	def __init__(self, index, imagefile, coordinates, size):
		self.id = index
		self.image = imagefile
		self.top_x = coordinates[0]
		self.top_y = coordinates[1]
		self.width = size[0]
		self.weight = size[1]
		self.locked = True

	def isUnlocked(self):
		self.locked = False
		self.top_x = 0
		self.top_y = 0
		self.bottom_x = 0
		self.bottom_y = 0
