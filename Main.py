import pygame
import view
import puzzle
import key
import lock
import button

class Controller:

	def __init__(self, width = 1200, height = 800):
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))

		self.tl_button = button.Button(1, [], (578,382), (93,61), 0, 3)
		self.tr_button = button.Button(2, [], (783,380), (118,67), 1, 3)
		self.bl_button = button.Button(3, [], (163,445), (130,108), 2, 3)
		self.br_button = button.Button(4, [], (431,472), (190,130), 3, 3)
		self.monitor_puzzle = puzzle.Puzzle(1, (0,0), (0,0), [self.tl_button,self.tr_button,self.bl_button,self.br_button])
		self.view1 = view.View(1, 'lab1.png', [self.monitor_puzzle], [], [])

		self.background = pygame.image.load(self.view1.background).convert() # setting the window/display
		self.background = pygame.transform.scale(self.background, (self.width, self.height)) # resizing the image
		self.currentView = self.view1 # how to tell which view we're using

		self.rightside_rect = pygame.Rect(1100, 0, 100, 800)
		self.leftside_rect = pygame.Rect(0, 0, 100, 800)

		self.view = [self.view1]

		self.gameComplete = False

		self.screen.blit((self.background), [0,0]) # creating the screen using the background image

		pygame.display.update()

	def mainLoop(self):
		# refreshes the screen
		# check if something's click, define what that click does

		running = True

		while running:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False

				if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
					event.pos = pygame.mouse.get_pos()

					# changes the view left or right
					# need to add how
					if self.rightside_rect.collidepoint(event.pos):
						for view in self.viewlist[:4]: # only the first four views
							if view.id == self.currentView.id + 1 or (view.id == 0 and self.currentView.id == 4):
								self.background = pygame.image.load(view.background).convert()
								self.background = pygame.transform.scale(self.background, (self.width, self.height))
								self.currentView = view
								self.screen.blit((self.background), [0,0])


					if self.leftside_rect.collidepoint(event.pos):
						for view in self.viewlist[:4]: # only the first four views
							if view.id == self.currentView.id - 1 or (view.id == 4 and self.currentView.id == 0):
								self.background = pygame.image.load(view.background).convert()
								self.background = pygame.transform.scale(self.background, (self.width, self.height))
								self.currentView = view
								self.screen.blit((self.background), [0,0])

					for puzzle in self.currentView.puzzlelist:
						if pygame.Rect(puzzle.top_x, puzzle.top_y, puzzle.width, puzzle.height).collidepoint(event.pos):
							# need to pull up the smaller view
							# self.background = pygame.image.load(SMALLERVIEW.background).convert()
							# self.background = pygame.transform.scale(self.background, (self.width, self.height))
							# self.currentView = SMALLERVIEW
							# self.screen.blit((self.background), [0,0])

							for button in puzzle.buttonlist:
								if pygame.Rect(button.top_x, button.top_y, button.width, button.height).collidepoint(event.pos):
									button.clickNum += 1
									if puzzle.isComplete():
										if puzzle == puzzle1:
											print('cool')
										# give the specific reward for the rest of the game

					for key in self.currentView.keylist:
						# we're just going to make it so that the key has its real coordinates after it is active
						if key.Rect(key.top_x, key.top_y, key.width, key.height).collidepoint(event.pos):
							key.isTaken()

						for lock in self.currentView.keylist:
							if lock.Rect(key.top_x, key.top_y, key.width, key.height).collidepoint(event.pos) and (lock.id == key.id):
								lock.isUnlocked()


					pygame.display.update()


def main():
	main_program = Controller()
	main_program.mainLoop()

main()
