class Note:
	def __init__(self, index, image, coordinates, size):
		"""
		Creates a note object, assigns an index value to it, takes image from image file, sets its coordinates and dimensions
		ParamList: self (self), index (int), image (string), coordinates (tuple), size (list)
		Returns: none
		"""
		self.id = index
		self.image = image
		self.top_x = coordinates[0]
		self.top_y = coordinates[1]
		self.width = size[0]
		self.height = size[1]
