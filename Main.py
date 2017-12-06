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

		# Ask Colin: Do all of the button variables need to be "self", and will it give points off?

		# Notes


		# Monitor Puzzle
		self.tl_monitor = button.Button(1, ['images/buttons/monitors/Blue4.png','images/buttons/monitors/Green4.png','images/buttons/monitors/Red4.png','images/buttons/monitors/Yellow4.png'], (578,382), (93,61), 2, 3)
		self.tr_monitor = button.Button(2, ['images/buttons/monitors/Blue3.png','images/buttons/monitors/Green3.png','images/buttons/monitors/Red3.png','images/buttons/monitors/Yellow3.png'], (783,380), (118,67), 0, 3)
		self.bl_monitor = button.Button(3, ['images/buttons/monitors/Blue2.png','images/buttons/monitors/Green2.png','images/buttons/monitors/Red2.png','images/buttons/monitors/Yellow2.png'], (163,445), (130,108), 1, 3)
		self.br_monitor = button.Button(4, ['images/buttons/monitors/Blue1.png','images/buttons/monitors/Green1.png','images/buttons/monitors/Red1.png','images/buttons/monitors/Yellow1.png'], (431,472), (190,130), 3, 3)
		self.monitor_puzzle = puzzle.Puzzle(1, [self.tl_monitor,self.tr_monitor,self.bl_monitor,self.br_monitor])

		# Printer Puzzle
		self.printer_shape1 = button.Button(1, ['images/buttons/printer/gRec.png','images/buttons/printer/gTri.png','images/buttons/printer/gCir.png','images/buttons/printer/gPent.png'], (0,0), (0,0), 2, 5)
		self.printer_shape2 = button.Button(2, ['images/buttons/printer/bRec.png','images/buttons/printer/bTri.png','images/buttons/printer/bCir.png','images/buttons/printer/bPent.png'], (0,0), (0,0), 1, 5)
		self.printer_shape3 = button.Button(3, ['images/buttons/printer/pRec.png','images/buttons/printer/pTri.png','images/buttons/printer/pCir.png','images/buttons/printer/pPent.png'], (0,0), (0,0), 2, 5)
		self.printer_shape4 = button.Button(4, ['images/buttons/printer/yRec.png','images/buttons/printer/yTri.png','images/buttons/printer/yCir.png','images/buttons/printer/yPent.png'], (0,0), (0,0), 3, 5)
		self.printer_puzzle = puzzle.Puzzle(2, [self.printer_shape1,self.printer_shape2,self.printer_shape3,self.printer_shape4])
		self.scissors = key.Key(1, [], (0,0), (0,0)) # rewarded key

		self.wires = lock.Lock(1, [], (0,0), (0,0)) # wires to be cut by scissors
		self.cabinet_key = key.Key(2, [], (0,0), (0,0)) # key to be taken from behing the wires

		self.cabinet = lock.Lock(2, [], (0,0), (0,0)) # locked cabinet

		# Telephone Puzzle
		self.phone1 = button.Button(1, [], (0,0), (0,0), 1, 0)
		self.phone2 = button.Button(2, [], (0,0), (0,0), 1, 0)
		self.phone3 = button.Button(3, [], (0,0), (0,0), 1, 0)
		self.phone4 = button.Button(4, [], (0,0), (0,0), 1, 0)
		self.phone5 = button.Button(5, [], (0,0), (0,0), 1, 0)
		self.phone6 = button.Button(6, [], (0,0), (0,0), 1, 0)
		self.phone7 = button.Button(7, [], (0,0), (0,0), 1, 0)
		self.phone8 = button.Button(8, [], (0,0), (0,0), 1, 0)
		self.phone9 = button.Button(9, [], (0,0), (0,0), 1, 0)
		self.telephone_puzzle = puzzle.Puzzle(3, [self.phone1,self.phone2,self.phone3,self.phone4,self.phone5,self.phone6,self.phone7,self.phone8,self.phone9], '348825')

		# Projector Puzzle
		self.youngersteven_button = button.Button(1, [], (0,0), (0,0), 1, 0)
		self.anthony_button = button.Button(2, [], (0,0), (0,0), 1, 0)
		self.shania_button = button.Button(3, [], (0,0), (0,0), 1, 0)
		self.melanie_button = button.Button(4, [], (0,0), (0,0), 1, 0)
		self.colin_button = button.Button(5, [], (0,0), (0,0), 1, 0)
		self.youngsteven_button = button.Button(6, [], (0,0), (0,0), 1, 0)
		self.projector_puzzle = puzzle.Puzzle(4, [self.youngersteven_button,self.anthony_button,self.shania_button,self.melanie_button,self.colin_button,self.youngsteven_button], '36142')

		self.safe_combo1 = button.Button(1, [''], (0,0), (0,0), 7, 10)
		self.safe_combo2 = button.Button(2, [''], (0,0), (0,0), 3, 10)
		self.safe_combo3 = button.Button(3, [''], (0,0), (0,0), 4, 10)
		self.safe_combo4 = button.Button(4, [''], (0,0), (0,0), 2, 10)
		self.safe_combo5 = button.Button(5, [''], (0,0), (0,0), 1, 10)
		self.safe_combo6 = button.Button(6, [''], (0,0), (0,0), 6, 10)
		self.safe_puzzle = puzzle.Puzzle(5, [self.safe_combo1,self.safe_combo2,self.safe_combo3,self.safe_combo4,self.safe_combo5,self.safe_combo6])
		self.blue_key = key.Key(3, [], (0,0), (0,0))

		self.blue_door = lock.Lock(3, [], (0,0), (0,0)) # exit


		# smaller views
		# view1 smaller views
		self.plugs_view = view.View(100, 'images/Plugs.png', (0,0), (0,0), [], [], [], [])
		self.frontlab_view = view.View(100, 'images/Plugs.png', (0,0), (0,0), [], [], [], [])


		# view2 smaller views
		self.computer_wires_view = view.View(6, '', (0,0), (0,0), [], [], [self.cabinet_key], [self.wires])
		self.computer_side_view = view.View(5, '', (0,0), (0,0), [self.computer_wires_view], [], [], [])


		# view3 smaller views
		self.garbage_view = view.View(7, '', (0,0), (0,0), [], [], [], [])
		self.printer_monitor_view = view.View(8, '', (0,0), (0,0), [], [self.printer_puzzle], [], [])
		self.printer_view = view.View(9, '', (0,0), (0,0), [], [], [self.scissors], [])
		self.cabinet_view = view.View(10, 'images/closedcabinet.jpg', (0,0), (0,0), [], [], [], [self.cabinet])

		# view4 smaller views



		# main views
		self.view1 = view.View(1, 'images/lab1.png', (0,0), (0,0), [], [self.monitor_puzzle], [], [])
		self.view2 = view.View(2, 'images/lab2.jpg', (0,0), (0,0), [], [], [], [])
		self.view3 = view.View(3, 'images/lab3.jpg', (0,0), (0,0), [self.garbage_view,self.printer_monitor_view,self.printer_view], [], [], [])
		self.view4 = view.View(4, 'images/lab4.jpg', (0,0), (0,0), [], [], [], [])


		self.background = pygame.image.load(self.view1.background) # setting the window/display
		self.background = pygame.transform.scale(self.background, (self.width, self.height)) # resizing the image
		self.currentView = self.view1 # how to tell which view we're using
		self.viewlist = [self.view1, self.view2, self.view3, self.view4] # creates a list with the first four views,
		# to use when turning left or right

		self.rightside_rect = pygame.Rect(1100, 0, 100, 800)
		self.leftside_rect = pygame.Rect(0, 0, 100, 800)

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

				if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
					event.pos = pygame.mouse.get_pos()

					viewChanged = False
					# changes the view left or right
					if self.rightside_rect.collidepoint(event.pos):
						for view in reversed(self.viewlist[:4]): # only the first four views
							if ((view.id == self.currentView.id + 1) or (view.id == 1 and self.currentView.id == 4)) and not viewChanged:
								print("current: " + str(self.currentView.id) + "next: " + str(view.id))
								self.currentView = view
								viewChanged = True
					elif self.leftside_rect.collidepoint(event.pos):
						for view in self.viewlist[:4]: # only the first four views
							if ((view.id == self.currentView.id - 1) or (view.id == 4 and self.currentView.id == 1)) and not viewChanged:
								print("current: " + str(self.currentView.id) + " next: " + str(view.id))
								self.currentView = view
								viewChanged = True
					self.background = pygame.image.load(self.currentView.background)
					self.background = pygame.transform.scale(self.background, (self.width, self.height))
					self.screen.blit((self.background), [0,0]) # blits the background no matter what happens

					for view in self.currentView.viewlist:
						if pygame.Rect(view.top_x, view.top_y, view.width, view.height).collidepoint(event.pos):
							self.background = pygame.image.load(view.background).convert()
							self.background = pygame.transform.scale(self.background, (self.width, self.height))
							self.currentView = view

					for puzzle in self.currentView.puzzlelist:
						for button in puzzle.buttonlist:
							if pygame.Rect(button.top_x, button.top_y, button.width, button.height).collidepoint(event.pos):
								if puzzle.id == 3: # telephone puzzle
									puzzle.addsToOrder(button.id)
								else:
									button.clicked()
								if puzzle.isComplete():
									if puzzle == self.monitor_puzzle:
										print("cool")
									# give the specific reward for the rest of the game
							if (button.image != ''):
								self.screen.blit(pygame.image.load(button.image), [0,0])



					for key in self.currentView.keylist:
						# we're just going to make it so that the key has its real coordinates after it is active
						if key.Rect(key.top_x, key.top_y, key.width, key.height).collidepoint(event.pos):
							key.isTaken()
							# want to have it in the top of the screen now
						if key.taken:
							self.screen.blit((pygame.image.load(key.images[1])), [0,0])

						for lock in self.currentView.keylist:
							if lock.Rect(key.top_x, key.top_y, key.width, key.height).collidepoint(event.pos) and (lock.id == key.id):
								lock.isUnlocked()

					pygame.display.update()


def main():
	main_program = Controller()
	main_program.mainLoop()

main()
