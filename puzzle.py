class Puzzle:
	def __init__(self, index, buttonlist, correct_order = ''):
		"""
		Takes the button list to create certain puzzles, uses an index number to identify individual puzzles, checks whether the buttons are pressed in the correct order by creating a list and a string accumulation.
		ParamList: self (self), index(int), buttonlist(list), correct_order (string), button_num(int)
		Returns: none 
		"""
		self.id = index
		self.buttonlist = buttonlist
		# variables used to check if the phone input is correct
		self.correct_order = correct_order
		self.partial_order = []
		for i in range(len(self.correct_order) + 1): self.partial_order.append(self.correct_order[:i])
		self.order = ''

	def isComplete(self):
		"""
		Checks to see if the buttons are correct, and that they are in order, and sets the function “isComplete” to true if they are.
		ParamList: self(self)
		Returns: true(boolean)
		"""
		if self.correct_order != '':
			if self.order == self.correct_order:
				return True
			else:
				return False
		else:
			# normal check of buttons
			for button in self.buttonlist:
				if button.isCorrect() == False:
					return False
			return True

	def addsToOrder(self, button_num):
		"""
		Accumulates the buttons that are pressed using the number of eachbutton.
		ParamList: self(self), button_num(int)
		Returns: none
		"""
		self.order += str(button_num)
		if self.order not in self.partial_order:
			# resets number
			self.order = ''
