class Key:
	def __init__(self, index, images, coordinates, size):
		self.id = index
		self.imagelist = images # first one will be the one you pick up, second will be the one to put on the screen
		self.top_x = coordinates[0]
		self.top_y = coordinates[1]
		self.width = size[0]
		self.weight = size[1]
		self.taken = False

	def isTaken(self):
		self.taken = True
		self.top_x, self.top_y, self.width, self.height = 0
