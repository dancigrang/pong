import pygame, os, sys
from pygame.locals import *


class Ball():
	def __init__(self):
		self.rect = pygame.Rect(295,200,10,10)
		# pygame.draw.rect(background, (250,250,250), (295,200,10,10), 0)
		self.dx = 2
		self.dy = 0

	def move(self):
		self.rect.x += self.dx
		self.rect.y += self.dy
		
		
		if b.rect.colliderect(pl.rect):
			b.dx = b.dx*-1	
		if b.rect.colliderect(pr.rect):
			b.dx = b.dx*-1	
		


class Paddle():
	def __init__(self,x,y):
		self.rect = pygame.Rect(x,y,10,80)
		# pygame.draw.rect(background, (250,250,250), (295,200,10,10), 0)

	def move(self, dx, dy):
		self.rect.x += dx
		self.rect.y += dy
		

#make dem objects
b = Ball()
pl = Paddle(25,200)
pr = Paddle(575,200)



def main():
	pygame.init()
	screen = pygame.display.set_mode((600,400))
	pygame.display.set_caption('Pong')

	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((0, 0, 0))

	# screen.blit(background, (0,0))
	# pygame.display.flip()

	
	clock = pygame.time.Clock()
	pygame.key.set_repeat(5,5)
	
	def repaint():
		
		b.move()
		screen.blit(background, (0,0))
		background.fill((0, 0, 0))
		pygame.draw.rect(background, (250,250,250), b.rect, 0)
		pygame.draw.rect(background, (250,250,250), pl.rect, 0)
		pygame.draw.rect(background, (250,250,250), pr.rect, 0)
		pygame.display.flip()

	while True:
		clock.tick(60)
		print b.rect
		#bouncing off paddles
		
		#scoring
		if b.rect.x < 0 or b.rect.x > 600: 
			print 'point'
		
		for event in pygame.event.get():
			if event.type == QUIT:
				return False
			if event.type == KEYDOWN and event.key == K_ESCAPE:
				return False
			if event.type == KEYDOWN and event.key == K_UP:
				pr.move(0,-5)					
			if event.type == KEYDOWN and event.key == K_DOWN:
				pr.move(0,5)					
			if event.type == KEYDOWN and event.key == K_q:
				pl.move(0,-5)
			if event.type == KEYDOWN and event.key == K_a:
				pl.move(0,5)
				
		repaint()
	
main()
