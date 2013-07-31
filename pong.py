import pygame

def main():
	pygame.init()
	screen = pygame.display.set_mode((600,400))
	pygame.display.set_caption('Pong')

	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((0, 0, 0))

	screen.blit(background, (0,0))
	pygame.display.flip()

	
main()
