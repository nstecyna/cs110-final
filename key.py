class Key:
	def __init__(self, index, coordinates, img_file):
		self.id = index
		self.image = pygame.image.load(img_file).convert_alpha()
		self.top_x = coordinates[0]
		self.top_y = coordinates[1]
		self.bottom_x = coordinates[2]
		self.bottom_y = coordinates[3]

		key.rect = pygame.Rect(self.top_x, self.top_y, self.bottom_x, self.bottom_y)
