import pygame

class Controller:

	def __init__(self, width = 800, height = 500):
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))
		
		#self.background = pygame.image.load('lab1.JPG')
		#background_rect = self.background.get_rect()
		self.background = pygame.Surface(self.screen.get_size()).convert()
		self.background.fill((255,255,255))
		self.screen.blit(self.background, (0,0))
		pygame.display.update()
		
def main():
	controller = Controller()
	pygame.key.set_repeat(1,50)
	running = True

	while running:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
main()
