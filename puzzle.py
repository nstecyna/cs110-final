class Puzzle:
	def __init__(self, index, buttonlist, correct_order = ''):
		self.id = index
		self.buttonlist = buttonlist
		# variables used to check if the phone input is correct
		self.correct_order = correct_order
		self.partial_order = []
		for i in range(len(self.correct_order) + 1): self.partial_order.append(self.correct_order[:i])
		self.order = ''

	def isComplete(self):
		# if this is an ordered button puzzle
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
		# accumulates the button pressed
		self.order += str(button_num)
		if self.order not in self.partial_order:
			# resets number
			self.order = ''
