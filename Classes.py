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

import pygame

class View:
# initialize
  # index telling which view it is 
  # background image
  # list of smaller images (to place in changes that show the changes from completing puzzles)
  # Puzzles in this room, with 
    # (x,y coordinates should be tuples, but can group the Puzzles and coordinates up in a list, dictionary, etc.)
  # Keys in this room, with two sets of x,y coordinates
  # Locks in this room, with two sets of x,y coordinates

class Puzzle:
# initialize
  # index number
  # two sets of x,y coordinates
  # a function for that specific puzzle (we'll work on this after doing the structure)

class Key:
# initialize
  # index number
  # two sets of x,y coordinates

# isUsed() - if used on the correct lock (matches index number?), should remove the key from the game, unlock the lock, and return true. else everything stays the same


class Lock:
# initialize
  # index number
  # two sets of x,y coordinates

# isOpened() - if the lock is opened, remove the lock from the game
