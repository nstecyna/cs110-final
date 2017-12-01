import pygame
import view
import puzzle
import key
import lock

#lab - part B*

#git repository setup

#code, planning, proposal

class Controller:	

	def __init__(self, width = 800, height = 500)
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.background = pygame.Surface(self.screen.get_size()).convert()
		self.view1 = pygame.display.set_mode(width, height) #setting the window/display
		self.puzzle1 = puzzle.Puzzle(. . .)
		self.key = key
		self.lock = lock

	def mainLoop(self):
		#refreshes the screen
		#check if something's click, define what that click does
		for event in pygame.event.get():
			if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
				pos = self.position.copy()

				rightside_rect1 = pygame.Rect(top_x, top_y, bottom_x, bottom_y)
				left_side_rect1 = pygame.Rect()
				keyRect = pygame.Rect(top_x, top_y, bottom_x, bottom_y)
				puzzleRect = pygame.Rect()
				lockRectZoom = pygame.Rect()

				#do we need this? maybe just to organize if we don't...

				if rightside_rect1.collidepoint(event.pos):
					
				if left_side_rect1.collidepoint(event.pos):
										

				if keyRect.collidepoint(event.pos):
					#"zoom" in (basically new view)
										
					self.view5 = pygame,display,set_mode((self.width, self.height))

				if puzzleRect.collidepoint(event.pos):
					#"zoom" in	
					self.view6 = pygame,display,set_mode((self.width, self.height))
			
				if lockRectZoom(event.pos):

					self.view7 = pygame,display,set_mode((self.width, self.height))

				if(lockRectZoom.collidepoint(event.pos) and key1_inhand):
					lock.Unlock()					
				
				if(lockRectZoom.collidepoint(event.pos) and key2_inhand):
					lock.Unlock()
		
def main():
	main_program = Controller()
	main_program.mainLoop()

main()
	
