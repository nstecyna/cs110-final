class Puzzle
	def __init__(self, index, coordinates):
		self.id = index
		self.top_x = coordinates[0]
		self.top_y = coordinates[1]
		self.bottom_x = coordinates[2]
		self.bottom_y = coordinates[3]
		self.complete = False
