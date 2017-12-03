class Key:
	def __init__(self, index, coordinates, images):
		self.id = index
		self.imagelist = images # first one will be keychain, second will be the one to put on the screen
		self.top_x = coordinates[0]
		self.top_y = coordinates[1]
		self.bottom_x = coordinates[2]
		self.bottom_y = coordinates[3]
		self.taken = False

	def isTaken(self):
		self.taken = True
