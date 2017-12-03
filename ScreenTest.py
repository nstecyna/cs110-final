import pygame

class Controller:
	
	def __init__(self, width = 1200, height = 800):
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))
		
		self.background = pygame.image.load('lab1.jpg').convert()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		#self.background_rect = self.background.get_rect()
		#self.background = pygame.Surface(self.screen.get_size()).convert()
		
		#self.background.fill((255,255,255))
		
		self.screen.blit((self.background), [0,0])
		
		pygame.display.update()


	def mainloop(self):
	
		running = True

		while running:
		
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False

			self.leftside_rect1 = pygame.Rect(0, 0, 100, 800)
			self.rightside_rect1 = pygame.Rect(1100, 0, 1200, 800) #how to access the top_x etc. from classes?
			

			if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
				event.pos = pygame.mouse.get_pos()

				if self.rightside_rect1.collidepoint(event.pos):
					print('clicked right box')
					self.background = pygame.display.set_mode((self.width, self.height))
					self.background = pygame.image.load('lab2.jpg').convert()
					self.background = pygame.transform.scale(self.background, (self.width, self.height))
					self.screen.blit((self.background), [0,0])
					pygame.display.update()

				elif self.leftside_rect1.collidepoint(event.pos):
					print('clicked left box')
					self.background = pygame.display.set_mode((self.width, self.height))
					self.background = pygame.image.load('lab4.jpg').convert()
					self.background = pygame.transform.scale(self.background, (self.width, self.height))
					self.screen.blit((self.background), [0,0])
					pygame.display.update()
					#self.view4 = pygame.display.set_mode((self.width, self.height))

				if self.background == :
					if self.rightside_rect1.collidepoint(event.pos):
						self.background = pygame.display.set_mode((self.width, self.height))
						self.background = pygame.image.load('lab3.jpg').convert()
						self.background = pygame.transform.scale(self.background, (self.width, self.height))
						self.screen.blit((self.background), [0,0])
						pygame.display.update()	

				#if clicked to new view
					#self.background = pygame.image.load('''that view.background''').convert()
					#self.background = pygame.transform.scale(self.background, (self.width, self.height))


def main():
	controller = Controller()
	mainloop = controller.mainloop()
main()
