class Key:
	def __init__(self, index, images, coordinates, size):
		"""
		Creates a key object, assigns an index value to it, takes image from image list, sets its coordinates and dimensions, sets self.taken bullion value as False to indicate that it has not been picked up
		ParamList: self (self), index (int), images (list), coordinates (tuple), size (list)
		Returns: none
		"""
		self.id = index
		self.imagelist = images # first one will be the one you pick up, second will be the one to put on the screen
		self.top_x = coordinates[0]
		self.top_y = coordinates[1]
		self.width = size[0]
		self.height = size[1]
		self.taken = False

	def isTaken(self):
		"""
		Changes self.taken bullion value to True, indicating that it has been picked up and makes it disappear from the view
		ParamList: self (self)
		Returns: none
		"""
		self.taken = True
		self.top_x = 0
		self.top_y = 0
		self.width = 0
		self.height = 0
