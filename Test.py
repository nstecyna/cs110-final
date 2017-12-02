import pygame

class Controller:

	def __init__(self, width = 1200, height = 800):
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))
		
		self.background = pygame.image.load('lab1.png').convert()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		#self.background_rect = self.background.get_rect()
		#self.background = pygame.Surface(self.screen.get_size()).convert()
		
		#self.background.fill((255,255,255))
		
		self.screen.blit((self.background), [0,0])
		
		pygame.display.update()
		
	def mainloop(self):
	
		pygame.key.set_repeat(1,50)
		running = True

		while running:
		
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				
				#if clicked to new view
					#self.background = pygame.image.load('''that view.background''').convert()
					#self.background = pygame.transform.scale(self.background, (self.width, self.height))


def main():
	controller = Controller()
	mainloop = controller.mainloop()
main()
