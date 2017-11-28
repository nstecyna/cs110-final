# want to import the functions that each check if a different puzzle is correct, so that we can make isCorrect()
# check if that numbered puzzle is correct and change self.correct if it is true.

class Puzzle:
  index = 1
  def __init__(self, coord1, coord2, i = index):
    # two sets of x,y coordinates
    self.coord1 = coord1 # tuple
    self.coord2 = coord2 # tuple
    # index number (can be chosen when initialized, but if not, we're just going to use the accumulated index number)
    self.index = i
    if (i == index):
      index += 1
    self.complete = False
    
  # right now we're going to just use the index number to know which puzzle is which, but eventually we can try:
  # a function for that specific puzzle (we'll work on this after doing the structure)
  
  def isCorrect(self):
    # if we just set self.complete = whichPuzzle(self.index), it may return false
    # we want to use this if statement, because if the puzzle is changed afterwards to be false, we don't want
    # it to think that the puzzle is not solved anymore
    if (whichPuzzle(self.index)):
      self.complete = True
    
