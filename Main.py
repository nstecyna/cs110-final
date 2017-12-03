import Pygame
import View
import Puzzle
import Key
import Lock

class Controller:

	def __init__(self, width = 1200, height = 800):
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))

		self.button1 = button.Button(1, [], (50,50,100,100), 3, 4)
		self.puzzle1 = puzzle.Puzzle(1, (0,0,0,0), [button1])
		self.view1 = view.View(1, 'lab1.png'v, [puzzle1], [], []])


		self.background = pygame.image.load('lab1.png').convert() # setting the window/display
		self.background = pygame.transform.scale(self.background, (self.width, self.height)) # resizing the image
		self.currentView = view1 # how to tell which view we're using

		self.rightside_rect = pygame.Rect(1100, 0, 1200, 8000)
		self.leftside_rect = pygame.Rect(0, 0, 100, 800)
		self.lock1_rect = pygame.Rect(top_x, top_y, bottom_x, bottom_y)
 		self.lock1_rectzoom = pygame.Rect(top_x, top_y, bottom_x, bottom_y)

		self.viewList = [view1]

		self.gameComplete = False

		self.screen.blit((self.background), [0,0]) # creating the screen using the background image

	def mainLoop(self):
		# refreshes the screen
		# check if something's click, define what that click does

		for event in pygame.event.get():

			if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
				event.pos = self.position.copy()

				# changes the view left or right
				# need to add how
				if rightside_rect.collidepoint(event.pos):
					for view in self.viewList[:4]: # only the first four views
						if view.id == self.currentView.id + 1:
							self.background = pygame.image.load(view.background).convert()
							self.background = pygame.transform.scale(self.background, (self.width, self.height))
							self.screen.blit((self.background), [0,0])


				if leftside_rect.collidepoint(event.pos):
					for view in self.viewList[:4]: # only the first four views
						if view.id == self.currentView.id - 1:
							self.background = pygame.image.load(view.background).convert()
							self.background = pygame.transform.scale(self.background, (self.width, self.height))
							self.screen.blit((self.background), [0,0])

				for puzzle in currentView.puzzleList:
					if pygame.Rect(puzzle.top_x, puzzle.top_y, puzzle.bottom_x, puzzle.bottom_y).collidepoint(event.pos):
						# need to pull up the smaller view
						# self.background = pygame.image.load(SMALLERVIEW.background).convert()
						# self.background = pygame.transform.scale(self.background, (self.width, self.height))
						# self.screen.blit((self.background), [0,0])

						for button in puzzle.buttonList:
							if pygame.Rect(button.top_x, button.top_y, button.bottom_x, button.bottom_y).collidepoint(event.pos):
								button.clickNum += 1
								if puzzle.isComplete():
									# give the specific reward for the rest of the game

				for key in currentView.keyList:
					# we're just going to make it so that the key has its real coordinates after it is active
					if key.Rect(key.top_x, key.top_y, key.bottom_x, key.bottom_y).collidepoint(event.pos):
						key.isTaken()

					for lock in currentView.keyList:
						if lock.Rect(key.top_x, key.top_y, key.bottom_x, key.bottom_y).collidepoint(event.pos) and (lock.id == key.id):
							lock.isUnlocked()


				pygame.display.update()


def main():
	main_program = Controller()
	main_program.mainLoop()

main()
