import Pygame
import View
import Puzzle
import Key
import Lock

class Controller:

	def __init__(self, width = 800, height = 500):
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))

		self.button1 = button.Button(1, [], (50,50,100,100), 3, 4)
		self.puzzle1 = puzzle.Puzzle(1, (0,0,0,0), [button1])
		self.view1 = view.View(1, 'lab1.png'v, [puzzle1], [], []])


		self.background = pygame.image.load('lab1.png').convert()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))

		#setting the window/display
		self.currentView = view1 # how to tell which view we're using

		self.key = key
		self.lock = lock

		self.rightside_rect1 = pygame.Rect(top_x, top_y, bottom_x, bottom_y) #how to access the top_x etc. from classes?
		self.leftside_rect1 = pygame.Rect(top_x, top_y, bottom_x, bottom_y)
		self.key1_rect = pygame.Rect(top_x, top_y, bottom_x, bottom_y)
		self.puzzle1_rect = pygame.Rect(top_x, top_y, bottom_x, bottom_y)
		self.lock1_rect = pygame.Rect(top_x, top_y, bottom_x, bottom_y)
 		self.lock1_rectzoom = pygame.Rect(top_x, top_y, bottom_x, bottom_y)

		self.viewList = [view1]


	def mainLoop(self):
		#refreshes the screen
		#check if something's click, define what that click does

		for event in pygame.event.get():

			if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
				pos = self.position.copy()

				if rightside_rect1.collidepoint(event.pos):
					for view in self.viewList
						if view.id == self.currentView.id + 1:
							view = pygame.display.set_mode((self.width, self.height))


				if leftside_rect1.collidepoint(event.pos):
					for view in self.viewList
						if view.id == self.currentView.id - 1:
							view = pygame.display.set_mode((self.width, self.height))









				############ view1 ###########

				if rightside_rect1.collidepoint(event.pos):
					self.view2 = pygame.display.set_mode((self.width, self.height))

				if leftside_rect1.collidepoint(event.pos):
					self.view4 = pygame.display.set_mode((self.width, self.height))

				#may literally zoom in instead of moving to a new view
					#"zoom" in (basically new view)

					self.view5 = pygame.display.set_mode((self.width, self.height))

				if puzzle1_rect.collidepoint(event.pos):
					#"zoom" in
					self.view6 = pygame.display.set_mode((self.width, self.height))

				if lock1_rect.collidepoint(event.pos):

					self.view7 = pygame.display.set_mode((self.width, self.height))

				if(lock1_rectzoom.collidepoint(event.pos) and key1_inv):
					Lock.unlock()


				if key1_rect.collidepoint(event.pos):
					Key.moveKey()

				########## view2 ###########
				if rightside_rect2.collidepoint(event.pos):
					self.view3 = pygame.display.set_mode((self.width, self.height))

				if leftside_rect2.collidepoint(event.pos):
					self.view1 = pygame.display.set_mode((self.width, self.height))

				if key2_rect.collidepoint(event.pos):
					#"zoom" in (basically new view)

					self.view8 = pygame.display.set_mode((self.width, self.height))

				if puzzle2_rect.collidepoint(event.pos):
					#"zoom" in
					self.view9 = pygame.display.set_mode((self.width, self.height))

				if lock2_rect.collidepoint(event.pos):

					self.view10 = pygame.display.set_mode((self.width, self.height))


				if(lock2_rectzoom.collidepoint(event.pos) and key2_inv):
					Lock.unlock()

				############ view3 ############

				if rightside_rect3.collidepoint(event.pos):
					self.view2 = pygame.display.set_mode((self.width, self.height))

				if leftside_rect3.collidepoint(event.pos):
					self.view4 = pygame.display.set_mode((self.width, self.height))

				if key2_rect.collidepoint(event.pos):
					#"zoom" in (basically new view)

	                 	if puzzle2_rect.collidepoint(event.pos):
					#"zoom" in
					self.view9 = pygame.display.set_mode((self.width, self.height))

				if lock2_rect.collidepoint(event.pos):

					self.view10 = pygame.display.set_mode((self.width, self.height))


				if(lock2_rectzoom.collidepoint(event.pos) and key2_inv):
					Lock.unlock()

				############# view4 ############



		#Check if puzzled are correct
		puzzles = [puzzle1, puzzle2, puzzle3, puzzle4]
		for puzzle in puzzles:
			completion = False
			final_completion = 1
			if isComplete(): #more than one of these?
				completion = True
				final_completion += 1
		if final_completion = 4 #number of total puzzles, may not need this if it just is done in order.. but more if statements for combined puzzles if in order


def main():
	main_program = Controller()
	main_program.mainLoop()

main()
