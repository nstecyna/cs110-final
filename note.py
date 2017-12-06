class Note:
	def __init__(self, index, image, coordinates, size):
		self.id = index
		self.image = image
		self.top_x = coordinates[0]
		self.top_y = coordinates[1]
		self.width = size[0]
		self.weight = size[1]
