import pygame, os, sys
from pygame.locals import *

class Ball():
	def __init__(self):
		self.rect = pygame.Rect(295,200,10,10)
		# pygame.draw.rect(background, (250,250,250), (295,200,10,10), 0)

	def move(self, dx, dy):
		# print 'update'
		self.rect.x += dx
		self.rect.y += dy

class Paddle():
	def __init__(self):
		self.rect = pygame.Rect(295,200,100,10)
		# pygame.draw.rect(background, (250,250,250), (295,200,10,10), 0)

	def move(self, dx, dy):
		# print 'update'
		self.rect.x += dx
		self.rect.y += dy

def main():
	pygame.init()
	screen = pygame.display.set_mode((600,400))
	pygame.display.set_caption('Pong')

	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((0, 0, 0))

	# screen.blit(background, (0,0))
	# pygame.display.flip()

	b = Ball()
	clock = pygame.time.Clock()

	while True:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == QUIT:
				return False
			if event.type == KEYDOWN and event.key == K_ESCAPE:
				return False
			if event.type == KEYDOWN and event.key == K_UP:
				b.move(0,-10)
			if event.type == KEYDOWN and event.key == K_DOWN:
				b.move(0,10)
			if event.type == KEYDOWN and event.key == K_LEFT:
				b.move(-10,0)
			if event.type == KEYDOWN and event.key == K_RIGHT:
				b.move(10,0)

		screen.blit(background, (0,0))
		background.fill((0, 0, 0))
		pygame.draw.rect(background, (250,250,250), b.rect, 0)
		pygame.display.flip()
	
main()