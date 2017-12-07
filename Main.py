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
		self.steven_note = note.Note(1, 'images/notes/FirstNoteSteven.png', (580,637), (119,75))
		self.garbage_note = note.Note(2, 'images/notes/ColinNote.png', (507,259), (185,99))
		self.cabinet_note = note.Note(2, 'images/notes/ColinNote2.png', (704,505), (93,33))
		self.cypher_note = note.Note(2, 'images/notes/ColinNote3.png', (0,0), (0,0))

		# Monitor Puzzle
		self.tl_monitor = button.Button(1, ['images/buttons/monitors/Blue4.png','images/buttons/monitors/Green4.png','images/buttons/monitors/Red4.png','images/buttons/monitors/Yellow4.png'], (578,382), (93,61), 2, 3)
		self.tr_monitor = button.Button(2, ['images/buttons/monitors/Blue3.png','images/buttons/monitors/Green3.png','images/buttons/monitors/Red3.png','images/buttons/monitors/Yellow3.png'], (783,380), (118,67), 0, 3)
		self.bl_monitor = button.Button(3, ['images/buttons/monitors/Blue2.png','images/buttons/monitors/Green2.png','images/buttons/monitors/Red2.png','images/buttons/monitors/Yellow2.png'], (163,445), (130,108), 1, 3)
		self.br_monitor = button.Button(4, ['images/buttons/monitors/Blue1.png','images/buttons/monitors/Green1.png','images/buttons/monitors/Red1.png','images/buttons/monitors/Yellow1.png'], (431,472), (190,130), 3, 3)
		self.monitor_puzzle = puzzle.Puzzle(1, [self.tl_monitor,self.tr_monitor,self.bl_monitor,self.br_monitor])

		# Printer Puzzle
		self.printer_shapeB = button.Button(1, ['images/buttons/printer/gRec.png','images/buttons/printer/gTri.png','images/buttons/printer/gCir.png','images/buttons/printer/gPent.png'], (569,142), (47,40), 2, 3)
		self.printer_shapeG = button.Button(2, ['images/buttons/printer/bRec.png','images/buttons/printer/bTri.png','images/buttons/printer/bCir.png','images/buttons/printer/bPent.png'], (635,149), (47,40), 1, 3)
		self.printer_shapeP = button.Button(3, ['images/buttons/printer/pRec.png','images/buttons/printer/pTri.png','images/buttons/printer/pCir.png','images/buttons/printer/pPent.png'], (696,149), (47,40), 2, 3)
		self.printer_shapeY = button.Button(4, ['images/buttons/printer/yRec.png','images/buttons/printer/yTri.png','images/buttons/printer/yCir.png','images/buttons/printer/yPent.png'], (754,153), (47,40), 3, 3)
		self.printer_puzzle = puzzle.Puzzle(2, [self.printer_shapeB,self.printer_shapeG,self.printer_shapeP,self.printer_shapeY])
		self.scissors = key.Key(1, ['images/Scissors.png', ''], (0,0), (0,0)) # rewarded key

		self.wires = lock.Lock(1, 'images/UnderComputerNoWires.png', (523,467), (82,29)) # wires to be cut by scissors
		self.cabinet_key = key.Key(2, ['images/NormalKey.jpg', 'images/OpenCabinet.png'], (0,0), (0,0)) # key to be taken from behing the wires

		self.cabinet = lock.Lock(2, 'images/OpenCabinet.png', (492,99), (130,221)) # locked cabinet

		# Telephone Puzzle
		self.phone1 = button.Button(1, [], (527,345), (58,48), 1, 0)
		self.phone2 = button.Button(2, [], (603,345), (55,48), 1, 0)
		self.phone3 = button.Button(3, [], (673,345), (59,47), 1, 0)
		self.phone4 = button.Button(4, [], (529,409), (58,45), 1, 0)
		self.phone5 = button.Button(5, [], (604,409), (52,43), 1, 0)
		self.phone6 = button.Button(6, [], (678,408), (48,43), 1, 0)
		self.phone7 = button.Button(7, [], (532,470), (52,43), 1, 0)
		self.phone8 = button.Button(8, [], (602,469), (54,40), 1, 0)
		self.phone9 = button.Button(9, [], (674,467), (49,42), 1, 0)
		self.telephone_puzzle = puzzle.Puzzle(3, [self.phone1,self.phone2,self.phone3,self.phone4,self.phone5,self.phone6,self.phone7,self.phone8,self.phone9], '348825')

		# Projector Puzzle
		self.youngersteven_button = button.Button(1, [], (491,363), (58,46), 1, 0)
		self.eileen_button = button.Button(2, [], (549,363), (52,44), 1, 0)
		self.shania_button = button.Button(3, [], (607,631), (51,47), 1, 0)
		self.melanie_button = button.Button(4, [], (497,431), (51,45), 1, 0)
		self.colin_button = button.Button(5, [], (554,432), (51,43), 1, 0)
		self.youngsteven_button = button.Button(6, [], (609,430), (51,45), 1, 0)
		self.projector_puzzle = puzzle.Puzzle(4, [self.youngersteven_button,self.anthony_button,self.shania_button,self.melanie_button,self.colin_button,self.youngsteven_button], '36142')

		self.safe_combo1 = button.Button(1, ['images/buttons/safe/1A.png','images/buttons/safe/2A.png','images/buttons/safe/3A.png','images/buttons/safe/4A.png','images/buttons/safe/5A.png','images/buttons/safe/6A.png','images/buttons/safe/7A.png','images/buttons/safe/8A.png','images/buttons/safe/9A.png'], (163,328), (109,143), 6, 8)
		self.safe_combo2 = button.Button(2, ['images/buttons/safe/1B.png','images/buttons/safe/2B.png','images/buttons/safe/3B.png','images/buttons/safe/4B.png','images/buttons/safe/5B.png','images/buttons/safe/6B.png','images/buttons/safe/7B.png','images/buttons/safe/8B.png','images/buttons/safe/9B.png'], (313,328), (109,143), 2, 8)
		self.safe_combo3 = button.Button(3, ['images/buttons/safe/1C.png','images/buttons/safe/2C.png','images/buttons/safe/3C.png','images/buttons/safe/4C.png','images/buttons/safe/5C.png','images/buttons/safe/6C.png','images/buttons/safe/7C.png','images/buttons/safe/8C.png','images/buttons/safe/9C.png'], (463,328), (109,143), 3, 8)
		self.safe_combo4 = button.Button(4, ['images/buttons/safe/1D.png','images/buttons/safe/2D.png','images/buttons/safe/3D.png','images/buttons/safe/4D.png','images/buttons/safe/5D.png','images/buttons/safe/6D.png','images/buttons/safe/7D.png','images/buttons/safe/8D.png','images/buttons/safe/9D.png'], (618,328), (109,143), 1, 8)
		self.safe_combo5 = button.Button(5, ['images/buttons/safe/1E.png','images/buttons/safe/2E.png','images/buttons/safe/3E.png','images/buttons/safe/4E.png','images/buttons/safe/5E.png','images/buttons/safe/6E.png','images/buttons/safe/7E.png','images/buttons/safe/8E.png','images/buttons/safe/9E.png'], (769,328), (109,143), 0, 8)
		self.safe_combo6 = button.Button(6, ['images/buttons/safe/1F.png','images/buttons/safe/2F.png','images/buttons/safe/3F.png','images/buttons/safe/4F.png','images/buttons/safe/5F.png','images/buttons/safe/6F.png','images/buttons/safe/7F.png','images/buttons/safe/8F.png','images/buttons/safe/9F.png'], (918,328), (109,143), 5, 8)
		self.safe_puzzle = puzzle.Puzzle(5, [self.safe_combo1,self.safe_combo2,self.safe_combo3,self.safe_combo4,self.safe_combo5,self.safe_combo6])
		self.blue_key = key.Key(3, ['images/ElderKey.png', 'images/OpenSafeNoKey.png'], (558,624), (125,51))

		self.blue_door = lock.Lock(3, 'images/OpenDoor.png', (0,0), (0,0)) # exit


		# smaller views
		# view1 smaller views
		self.plugs_view = view.View(5, 'images/Plugs.png', (122,435), (38,36), [], [], [], [], [])
		self.projector_view = view.View(6, 'images/Projector.png', (776,506), (167,82), [], [self.projector_puzzle], [], [], [])
		self.telephone_view = view.View(7, 'images/Phone.png', (421,239), (31,44), [], [self.telephone_puzzle], [], [], [])
		self.frontlab_view = view.View(8, 'images/FrontLab.png', (633,167), (823-633,346-167), [self.projector_view], [], [], [], [])
		self.whiteboard_view = view.View(9, 'images/Whiteboard.png', (845,156), (1196-845,337-157), [], [], [], [], [])

		# view2 smaller views
		self.computer_wires_view = view.View(10, 'images/UnderComputer.png', (570,386), (742,552), [], [], [self.cabinet_key], [self.wires], [])
		self.safe_view = view.View(11, 'images/ClosedSafe.png', (72,371), (60,69), [], [self.safe_puzzle], [self.blue_key], [], [])

		# view3 smaller views
		self.garbage_view = view.View(12, 'images/Garbage.png', (0,0), (0,0), [], [], [], [], [self.garbage_note])
		self.printer_monitor_view = view.View(13, 'images/monitor.png', (365,338), (538,504), [], [self.printer_puzzle], [], [self.scissors], [])
		self.printer_view = view.View(14, 'images/Printer.png', (577,349), (771-577,484-349), [], [], [self.scissors], [], [])
		self.cabinet_view = view.View(15, 'images/ClosedCabinet.jpg', (834,460), (1174-834,460-713), [], [], [], [self.cabinet], [self.cabinet_note])

		# view4 smaller views
		self.door_view = view.View(16, '', (305,19), (592-305,736-19), [], [], [], [], [self.blue_door])

		# main views
		self.view1 = view.View(1, 'images/lab1.png', (0,0), (0,0), [self.plugs_view,self.projector_view,self.telephone_view,self.frontlab_view,self.whiteboard_view], [self.monitor_puzzle], [], [], [self.steven_note])
		self.view2 = view.View(2, 'images/lab2.png', (0,0), (0,0), [self.computer_wires_view,self.safe_view], [], [], [], [])
		self.view3 = view.View(3, 'images/lab3.png', (0,0), (0,0), [self.garbage_view,self.printer_monitor_view,self.printer_view,self.cabinet_view], [], [], [], [])
		self.view4 = view.View(4, 'images/lab4.png', (0,0), (0,0), [self.door_view], [], [], [], [])

		# setting the window/display
		self.background = pygame.image.load(self.view1.background)
		# resizing the image
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		# how to tell which view we're using
		self.currentView = self.view1
		# creates a list with the first four views to use when turning left or right
		self.viewlist = [self.view1, self.view2, self.view3, self.view4,self.plugs_view,self.projector_view,self.telephone.view,self.frontlab_view,self.whiteboard_view,self.computer_wires_view,self.safe_view,self.garbage_view,self.printer_monitor_view,self.printer_view,self.cabinet_view,self.door_view]

		# list used to keep track of past views
		self.pastviewlist = []

		# used to display the image of the keys on the top of screen
		self.keylist = []

		self.rightside_rect = pygame.Rect(1100, 0, 100, 800)
		self.leftside_rect = pygame.Rect(0, 0, 100, 800)

		self.gameComplete = False

		self.screen.blit((self.background), [0,0]) # creating the screen using the background image
		self.screen.blit((pygame.image.load(self.steven_note.image)), [0,0])

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
								if (key.id == 1 and view.id == '''''') or (key.id == 2 and view.id == '''''') or (key.id == 3 and view.id == 11):
									view.background = key.imagelist[1]

						for lock in self.currentView.keylist:
							if pygame.Rect(key.top_x, key.top_y, key.width, key.height).collidepoint(event.pos) and (lock.id == key.id):
								lock.isUnlocked()
								for view in self.viewlist:
									if (lock.id == 1 and view.id == '''''') or (lock.id == 2 and view.id == '''''') or (lock.id == 3 and view.id == 16):
										view.background = lock.image
										if lock.id = 1:
											self.viewlist[13].keylist[0].top_x = 523
											self.viewlist[13].keylist[0].top_y = 467
											self.viewlist[13].keylist[0].width = 82
											self.viewlist[13].keylist[0].height = 29
										if lock.id = 2:
											self.viewlist[14].keylist[0].top_x = 704
											self.viewlist[14].keylist[0].top_y = 505
											self.viewlist[14].keylist[0].width = 93
											self.viewlist[14].keylist[0].height = 33
										if lock.id = 3:
											self.rightside_rect = pygame.Rect(0, 0, 0, 0)
											self.leftside_rect = pygame.Rect(0, 0, 0, 0)

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
								if ((view.id == self.currentView.id + 1) or (view.id == 1 and self.currentView.id == 4)) and not viewChanged:
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
								if ((view.id == self.currentView.id - 1) or (view.id == 4 and self.currentView.id == 1)) and not viewChanged:
									self.currentView = view
									viewChanged = True

					for view in self.currentView.viewlist:
						if pygame.Rect(view.top_x, view.top_y, view.width, view.height).collidepoint(event.pos):
							self.pastviewlist.append(self.currentView.id)
							self.currentView = view


					self.background = pygame.image.load(self.currentView.background)
					self.background = pygame.transform.scale(self.background, (self.width, self.height))
					self.screen.blit((self.background), [0,0]) # blits the background no matter what happens

					for puzzle in self.currentView.puzzlelist:
						for button in puzzle.buttonlist:
							if pygame.Rect(button.top_x, button.top_y, button.width, button.height).collidepoint(event.pos):
								if puzzle.id == (3 or 4): # telephone puzzle
									puzzle.addsToOrder(button.id)
								else:
									button.clicked()
									print(button.clickNum)
								# give the specific reward for the rest of the game
								if puzzle.isComplete():
									if puzzle == self.monitor_puzzle:
										self.viewlist[1].background = "images.lab1withshapes.png"
										self.currentView = self.viewlist[1]
										self.background = pygame.image.load(self.currentView.background)
										self.screen.blit((self.background), [0,0])
										for button in self.viewlist[1].puzzlelist[0].buttonlist:
											button.isRemoved()

									if puzzle == self.printer_puzzle:
										self.viewlist[13].background = "images.PrinterError.png"
										self.viewlist[12].background = "images.PrinterWithScissors.png"
										self.viewlist
										self.currentView = self.viewlist[13]
										self.background = pygame.image.load(self.currentView.background)
										self.screen.blit((self.background), [0,0])
										for button in self.viewlist[13].puzzlelist[0].buttonlist:
											button.isRemoved()

									if puzzle == self.safe_puzzle:
										self.viewlist[10].background = "images/OpenSafeWithKey.png"
										self.currentView = self.viewlist[10]
										self.background = pygame.image.load(self.currentView.background)
										self.screen.blit((self.background), [0,0])
										for button in self.viewlist[10].puzzlelist[0].buttonlist:
											button.isRemoved()

									if puzzle == self.telephone_puzzle:
										self.viewlist[6].background = "images/PhoneColin.png"
										self.currentView = self.viewlist[6]
										self.background = pygame.image.load(self.currentView.background)
										self.screen.blit((self.background), [0,0])
										for button in self.viewlist[6].puzzlelist[0].buttonlist:
											button.isRemoved()

									if puzzle == self.projector_puzzle:
										self.viewlist[5].background = "images/ProjectorOn.png"
										self.viewlist[8].background = "images/Projection.png"
										self.currentView = self.viewlist[5]
										self.background = pygame.image.load(self.currentView.background)
										self.screen.blit((self.background), [0,0])
										for button in self.viewlist[5].puzzlelist[0].buttonlist:
											button.isRemoved()

							if (button.image != ''):
								self.screen.blit(pygame.image.load(button.image), [0,0])

					for key in self.keylist:
						# want to have the key on the top of the screen now
							self.screen.blit((pygame.image.load(key.imagelist[0])), [0,0])
					print(self.pastviewlist)

					for note in self.currentView.notelist:
						if pygame.Rect(note.top_x, note.top_y, note.width, note.height).collidepoint(event.pos):
							self.screen.blit((pygame.image.load(note.image)), [0,0])

					pygame.display.update()



def main():
	main_program = Controller()
	main_program.mainLoop()

main()
