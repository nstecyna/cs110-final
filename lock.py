class Lock
 	def __init__(self, index, coordinates, image):
  		self.id = index
 		self.image = image
  		self.top_x = coordinates[0]
  		self.top_y = coordinates[1]
  		self.bottom_x = coordinates[2]
  		self.bottom_y = coordinates[3]
 		self.locked = True
 
 	def isUnlocked(self):
 		self.locked = False
 			self.top_x = 0
 			self.top_y = 0
 			self.bottom_x = 0
			self.bottom_y = 0
