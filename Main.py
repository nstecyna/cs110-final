import pygame
import view
import puzzle
import key
import lock
import button
import note

class Controller:

	def __init__(self, width = 1200, height = 800):
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))

		# Ask Colin: Do all of the button variables need to be "self", and will it give points off?

		# Notes
		steven_note = note.Note(1, 'images/notes/FirstNoteSteven.png', (580,637), (119,75))
		garbage_note = note.Note(2, 'images/notes/ColinNote.png', (507,259), (185,99))
		cabinet_note = note.Note(2, 'images/notes/ColinNote2.png', (0,0), (0,0))
		cypher_note = note.Note(2, 'images/notes/ColinNote3.png', (512,644), (114,83))

		# Monitor Puzzle
		tl_monitor = button.Button(1, ['images/buttons/monitors/Blue4.png','images/buttons/monitors/Green4.png','images/buttons/monitors/Red4.png','images/buttons/monitors/Yellow4.png'], (578,382), (93,61), 2, 3)
		tr_monitor = button.Button(2, ['images/buttons/monitors/Blue3.png','images/buttons/monitors/Green3.png','images/buttons/monitors/Red3.png','images/buttons/monitors/Yellow3.png'], (783,380), (118,67), 0, 3)
		bl_monitor = button.Button(3, ['images/buttons/monitors/Blue2.png','images/buttons/monitors/Green2.png','images/buttons/monitors/Red2.png','images/buttons/monitors/Yellow2.png'], (163,445), (130,108), 1, 3)
		br_monitor = button.Button(4, ['images/buttons/monitors/Blue1.png','images/buttons/monitors/Green1.png','images/buttons/monitors/Red1.png','images/buttons/monitors/Yellow1.png'], (431,472), (190,130), 3, 3)
		monitor_puzzle = puzzle.Puzzle(1, [tl_monitor,tr_monitor,bl_monitor,br_monitor])

		# Printer Puzzle
		printer_shapeB = button.Button(1, ['images/buttons/printer/gRec.png','images/buttons/printer/gTri.png','images/buttons/printer/gCir.png','images/buttons/printer/gPent.png'], (569,142), (47,40), 2, 3)
		printer_shapeG = button.Button(2, ['images/buttons/printer/bRec.png','images/buttons/printer/bTri.png','images/buttons/printer/bCir.png','images/buttons/printer/bPent.png'], (635,149), (47,40), 1, 3)
		printer_shapeP = button.Button(3, ['images/buttons/printer/pRec.png','images/buttons/printer/pTri.png','images/buttons/printer/pCir.png','images/buttons/printer/pPent.png'], (696,149), (47,40), 2, 3)
		printer_shapeY = button.Button(4, ['images/buttons/printer/yRec.png','images/buttons/printer/yTri.png','images/buttons/printer/yCir.png','images/buttons/printer/yPent.png'], (754,153), (47,40), 3, 3)
		printer_puzzle = puzzle.Puzzle(2, [printer_shapeB,printer_shapeG,printer_shapeP,printer_shapeY])
		scissors = key.Key(1, ['images/Scissors.png', 'images/PrinterNoScissors.png'], (0,0), (0,0)) # rewarded key

		wires = lock.Lock(1, 'images/UnderComputerNoWires.png', (517,463), (90,35)) # wires to be cut by scissors
		cabinet_key = key.Key(2, ['images/NormalKey.png', 'images/UnderComputerEmpty.png'], (0,0), (0,0)) # key to be taken from behing the wires

		cabinet = lock.Lock(2, 'images/OpenCabinet.png', (492,99), (130,221)) # locked cabinet

		# Telephone Puzzle
		phone1 = button.Button(1, [], (527,345), (56,48), 1, 0)
		phone2 = button.Button(2, [], (603,345), (55,48), 1, 0)
		phone3 = button.Button(3, [], (673,345), (59,47), 1, 0)
		phone4 = button.Button(4, [], (529,409), (58,45), 1, 0)
		phone5 = button.Button(5, [], (604,409), (52,43), 1, 0)
		phone6 = button.Button(6, [], (678,408), (48,43), 1, 0)
		phone7 = button.Button(7, [], (532,470), (52,43), 1, 0)
		phone8 = button.Button(8, [], (602,469), (54,40), 1, 0)
		phone9 = button.Button(9, [], (674,467), (49,42), 1, 0)
		telephone_puzzle = puzzle.Puzzle(3, [phone1,phone2,phone3,phone4,phone5,phone6,phone7,phone8,phone9], '348825')

		# Projector Puzzle
		youngersteven_button = button.Button(1, [], (491,361), (56,48), 1, 0)
		eileen_button = button.Button(2, [], (551,361), (51,48), 1, 0)
		shania_button = button.Button(3, [], (607,360), (49,48), 1, 0)
		melanie_button = button.Button(4, [], (497,431), (51,45), 1, 0)
		colin_button = button.Button(5, [], (554,432), (51,43), 1, 0)
		youngsteven_button = button.Button(6, [], (609,430), (51,45), 1, 0)
		projector_puzzle = puzzle.Puzzle(4, [youngersteven_button,eileen_button,shania_button,melanie_button,colin_button,youngsteven_button], '36142')

		safe_combo1 = button.Button(1, ['images/buttons/safe/1A.png','images/buttons/safe/2A.png','images/buttons/safe/3A.png','images/buttons/safe/4A.png','images/buttons/safe/5A.png','images/buttons/safe/6A.png','images/buttons/safe/7A.png','images/buttons/safe/8A.png','images/buttons/safe/9A.png'], (163,328), (109,143), 6, 8)
		safe_combo2 = button.Button(2, ['images/buttons/safe/1B.png','images/buttons/safe/2B.png','images/buttons/safe/3B.png','images/buttons/safe/4B.png','images/buttons/safe/5B.png','images/buttons/safe/6B.png','images/buttons/safe/7B.png','images/buttons/safe/8B.png','images/buttons/safe/9B.png'], (313,328), (109,143), 2, 8)
		safe_combo3 = button.Button(3, ['images/buttons/safe/1C.png','images/buttons/safe/2C.png','images/buttons/safe/3C.png','images/buttons/safe/4C.png','images/buttons/safe/5C.png','images/buttons/safe/6C.png','images/buttons/safe/7C.png','images/buttons/safe/8C.png','images/buttons/safe/9C.png'], (463,328), (109,143), 3, 8)
		safe_combo4 = button.Button(4, ['images/buttons/safe/1D.png','images/buttons/safe/2D.png','images/buttons/safe/3D.png','images/buttons/safe/4D.png','images/buttons/safe/5D.png','images/buttons/safe/6D.png','images/buttons/safe/7D.png','images/buttons/safe/8D.png','images/buttons/safe/9D.png'], (618,328), (109,143), 1, 8)
		safe_combo5 = button.Button(5, ['images/buttons/safe/1E.png','images/buttons/safe/2E.png','images/buttons/safe/3E.png','images/buttons/safe/4E.png','images/buttons/safe/5E.png','images/buttons/safe/6E.png','images/buttons/safe/7E.png','images/buttons/safe/8E.png','images/buttons/safe/9E.png'], (769,328), (109,143), 0, 8)
		safe_combo6 = button.Button(6, ['images/buttons/safe/1F.png','images/buttons/safe/2F.png','images/buttons/safe/3F.png','images/buttons/safe/4F.png','images/buttons/safe/5F.png','images/buttons/safe/6F.png','images/buttons/safe/7F.png','images/buttons/safe/8F.png','images/buttons/safe/9F.png'], (918,328), (109,143), 5, 8)
		safe_puzzle = puzzle.Puzzle(5, [safe_combo1,safe_combo2,safe_combo3,safe_combo4,safe_combo5,safe_combo6])
		blue_key = key.Key(3, ['images/ElderKey.png', 'images/OpenSafeNoKey.png'], (0,0), (0,0))

		blue_door = lock.Lock(3, 'images/TheEnd.png', (295,0), (310,775)) # exit


		# smaller views
		# view1 smaller views
		plugs_view = view.View(4, 'images/Plugs.png', (122,435), (38,36), [], [], [], [], [])
		projector_view = view.View(5, 'images/Projector.png', (776,506), (167,82), [], [projector_puzzle], [], [], [])
		telephone_view = view.View(6, 'images/Phone.png', (421,239), (31,44), [], [telephone_puzzle], [], [], [])
		frontlab_view = view.View(7, 'images/FrontLab.png', (480,150), (450,230), [telephone_view,projector_view], [], [], [], [])
		whiteboard_view = view.View(8, 'images/Whiteboard.png', (930,156), (266,180), [], [], [], [], [])

		# view2 smaller views
		computer_wires_view = view.View(9, 'images/UnderComputer.png', (570,386), (742,552), [], [], [cabinet_key], [wires], [])
		safe_view = view.View(10, 'images/ClosedSafe.png', (72,371), (60,69), [], [safe_puzzle], [blue_key], [], [])

		# view3 smaller views
		garbage_view = view.View(11, 'images/Garbage.png', (834,460), (340,253), [], [], [], [], [garbage_note])
		printer_monitor_view = view.View(12, 'images/monitor.png', (365,338), (173,166), [], [printer_puzzle], [], [scissors], [])
		printer_view = view.View(13, 'images/Printer.png', (568,345), (214,148), [], [], [scissors], [], [])
		cabinet_view = view.View(14, 'images/ClosedCabinet.png', (143,516), (366,264), [], [], [], [cabinet], [cabinet_note])

		# view4 smaller views
		door_view = view.View(15, 'images/DoorWithLock.png', (265,110), (135,270), [], [], [], [blue_door], [])

		# main views
		view1 = view.View(0, 'images/lab1.png', (0,0), (0,0), [plugs_view,frontlab_view,whiteboard_view], [monitor_puzzle], [], [], [steven_note])
		view2 = view.View(1, 'images/lab2.png', (0,0), (0,0), [computer_wires_view,safe_view], [], [], [], [])
		view3 = view.View(2, 'images/lab3.png', (0,0), (0,0), [garbage_view,printer_monitor_view,printer_view,cabinet_view], [], [], [], [])
		view4 = view.View(3, 'images/lab4.png', (0,0), (0,0), [door_view], [], [], [], [cypher_note])


		# creates a list with the first four views to use when turning left or right
		self.viewlist = [view1, view2, view3, view4,plugs_view,projector_view,telephone_view,frontlab_view,whiteboard_view,computer_wires_view,safe_view,garbage_view,printer_monitor_view,printer_view,cabinet_view,door_view]
		# how to tell which view we're using
		self.currentView = self.viewlist[0]
		# list used to keep track of past views
		self.pastviewlist = []

		# setting the window/display
		self.background = pygame.image.load(self.currentView.background)
		# resizing the image
		self.background = pygame.transform.scale(self.background, (self.width, self.height))

		# used to display the image of the keys on the top of screen
		self.keylist = []

		self.rightside_rect = pygame.Rect(1100, 0, 100, 800)
		self.leftside_rect = pygame.Rect(0, 0, 100, 800)

		self.gameComplete = False

		self.screen.blit((self.background), [0,0]) # creating the screen using the background image
		self.screen.blit((pygame.image.load(steven_note.image)), [0,0]) # starts the game looking at steven's note

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

					for key in self.currentView.keylist:
						# we're just going to make it so that the key has its real coordinates after it is active
						if pygame.Rect(key.top_x, key.top_y, key.width, key.height).collidepoint(event.pos):
							key.isTaken()
							self.keylist.append(key)
							for view in self.viewlist:
								if (key.id == 1 and view.id == 13) or (key.id == 2 and view.id == 9) or (key.id == 3 and view.id == 10):
									view.background = key.imagelist[1]
									self.currentView = view

					for lock in self.currentView.locklist:
						for key in self.keylist:
							if pygame.Rect(lock.top_x, lock.top_y, lock.width, lock.height).collidepoint(event.pos) and (lock.id == key.id):
								for view in self.viewlist:
									if (lock.id == 1 and view.id == 9) or (lock.id == 2 and view.id == 14) or (lock.id == 3 and view.id == 15):
										view.locklist[0].isUnlocked()
										view.background = lock.image
										if lock.id == 1:
											# add the coordinates for the key in the wires, so the mouse can collide with it
											view.keylist[0].top_x = 517
											view.keylist[0].top_y = 463
											view.keylist[0].width = 90
											view.keylist[0].height = 35
										elif lock.id == 2:
											view.notelist[0].top_x = 704
											view.notelist[0].top_y = 505
											view.notelist[0].width = 93
											view.notelist[0].height = 33
										else:
											self.rightside_rect = pygame.Rect(0, 0, 0, 0)
											self.leftside_rect = pygame.Rect(0, 0, 0, 0)
											self.keylist = []
										self.currentView = view

					viewChanged = False
					# changes the view left or right
					if self.rightside_rect.collidepoint(event.pos):
						if len(self.pastviewlist): # if we have a past view
							pastview = self.pastviewlist.pop()
							for view in self.viewlist:
								if view.id == pastview:
									self.currentView = view
									viewChanged = True
						else:
							for view in reversed(self.viewlist[:4]): # only the first four views
								if ((view.id == self.currentView.id + 1) or (view.id == 0 and self.currentView.id == 3)) and not viewChanged:
									self.currentView = view
									viewChanged = True
					elif self.leftside_rect.collidepoint(event.pos):
						if len(self.pastviewlist): # if we have a past view
							pastview = self.pastviewlist.pop()
							for view in self.viewlist:
								if view.id == pastview:
									self.currentView = view
									viewChanged = True
						else:
							for view in self.viewlist[:4]: # only the first four views
								if ((view.id == self.currentView.id - 1) or (view.id == 3 and self.currentView.id == 0)) and not viewChanged:
									self.currentView = view
									viewChanged = True

					for view in self.currentView.viewlist:
						if pygame.Rect(view.top_x, view.top_y, view.width, view.height).collidepoint(event.pos) and not viewChanged:
							self.pastviewlist.append(self.currentView.id)
							self.currentView = view
							viewChanges = True


					self.background = pygame.image.load(self.currentView.background)
					self.background = pygame.transform.scale(self.background, (self.width, self.height))
					self.screen.blit((self.background), [0,0]) # blits the background no matter what happens

					for puzzle in self.currentView.puzzlelist:
						for button in puzzle.buttonlist:
							if pygame.Rect(button.top_x, button.top_y, button.width, button.height).collidepoint(event.pos):
								if button.image == '': # telephone puzzle or projector_puzzle
									puzzle.addsToOrder(button.id)
								else:
									button.clicked()
								# give the specific reward for the rest of the game
								if puzzle.isComplete():
									if puzzle.id == 1: # first puzzle (monitors)
										self.viewlist[0].background = "images/lab1withshapes.png"
										self.currentView = self.viewlist[0]
										self.background = pygame.image.load(self.currentView.background)
										self.screen.blit((self.background), [0,0])
										for button in self.viewlist[0].puzzlelist[0].buttonlist:
											button.isRemoved()

									if puzzle.id == 2: # second puzzle (printer)
										self.viewlist[12].background = "images/PrinterError.png"
										self.viewlist[13].background = "images/PrinterWithScissors.png"
										self.viewlist[13].keylist[0].top_x = 365
										self.viewlist[13].keylist[0].top_y = 524
										self.viewlist[13].keylist[0].width = 486
										self.viewlist[13].keylist[0].height = 157
										self.currentView = self.viewlist[12]
										self.background = pygame.image.load(self.currentView.background)
										self.screen.blit((self.background), [0,0])
										for button in self.viewlist[12].puzzlelist[0].buttonlist:
											button.isRemoved()

									if puzzle.id == 3: # third puzzle (telephone)
										self.viewlist[6].background = "images/PhoneColin.png"
										self.currentView = self.viewlist[6]
										self.background = pygame.image.load(self.currentView.background)
										self.screen.blit((self.background), [0,0])
										for button in self.viewlist[6].puzzlelist[0].buttonlist:
											button.isRemoved()

									if puzzle.id == 4: # fourth puzzle (projector)
										self.viewlist[5].background = "images/ProjectorOn.png"
										self.viewlist[8].background = "images/Projection.png"
										self.currentView = self.viewlist[5]
										self.background = pygame.image.load(self.currentView.background)
										self.screen.blit((self.background), [0,0])
										for button in self.viewlist[5].puzzlelist[0].buttonlist:
											button.isRemoved()

									if puzzle.id == 5: # fifth puzzle (safe)
										self.viewlist[10].background = "images/OpenSafeWithKey.png"
										self.viewlist[10].keylist[0].top_x = 558
										self.viewlist[10].keylist[0].top_y = 624
										self.viewlist[10].keylist[0].width = 125
										self.viewlist[10].keylist[0].height = 51
										self.currentView = self.viewlist[10]
										self.background = pygame.image.load(self.currentView.background)
										self.screen.blit((self.background), [0,0])
										for button in self.viewlist[10].puzzlelist[0].buttonlist:
											button.isRemoved()

							if (button.image != ''):
								self.screen.blit(pygame.image.load(button.image), [0,0])

					for key in self.keylist:
						# want to have the key on the top of the screen now
							self.screen.blit((pygame.image.load(key.imagelist[0])), [0,0])

					for note in self.currentView.notelist:
						if pygame.Rect(note.top_x, note.top_y, note.width, note.height).collidepoint(event.pos):
							self.screen.blit((pygame.image.load(note.image)), [0,0])

					pygame.display.update()



def main():
	main_program = Controller()
	main_program.mainLoop()

main()
