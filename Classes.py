class View:
	def __init__(self, keylist, puzzlelist):
		self.keylist[0]
		self.keylist[1]

class Puzzle:
	def __init__(self, imagelist, coordinates, puzzle_number):
		self.imagelist = imagelist	
		self.x = coordinates[0]
		self.y = coordinates[1]
		self.complete = False
		self.number = puzzle_number
	def isCompleted(self):
		self.complete = whichPuzzle(self.number)

p = Puzzle(imagelist, (2,3), 1)
p.puzzlenumber

	
class Key:
	def __init__(self, location):
		self.x = location[0]
		self.y = location[1]




def whichPuzzle(number):
	if (number == 1):
		puzzle1()
	elif ...

