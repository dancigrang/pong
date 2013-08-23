import pygame, os, sys, time, random
from pygame.locals import *


class Ball():
	def __init__(self, x):
		self.rect = pygame.Rect(295,200,10,10)

		self.dx = 2*x
		self.dy = random.uniform(-2,2)
		# print self.dy

	def move(self):
		self.rect.x += self.dx
		self.rect.y += self.dy
		
		# bounce x paddles left paddle
		if b.rect.colliderect(pl.rect):
			b.dx = b.dx*-1	
			self.rect.x += 2
			self.angle(pl)
		# bounce x paddles right paddle
		if b.rect.colliderect(pr.rect):
			self.rect.x -= 2
			b.dx = b.dx*-1	
			self.angle(pr)

		# bounce y borders bottom
		if self.rect.y >= 390:
			b.dy = b.dy * -1
		
		# bounce y borders top
		if self.rect.y <= 0:
			b.dy = b.dy * -1

	def angle(self, r):
			offset = ((r.rect.y - b.rect.y) + 55)/12
			if offset >= 5:
				self.dy = -6
			elif offset == 4:
				self.dy = -4
			elif offset == 3:
				self.dy = -2
			elif offset ==2:
				self.dy = 2
			elif offset == 1:
				self.dy = 4
			elif offset <= 0:
				self.dy = 6


class Paddle():
	def __init__(self,x,y):
		self.rect = pygame.Rect(x,y,10,60)

	def move(self, dy):
		if self.rect.y <= 340 or self.rect.y >= 0:
			self.rect.y += dy
			if self.rect.y > 340:
				self.rect.y = 340
			elif self.rect.y < 0:
				self.rect.y = 0
		

#make dem objects
b = Ball(1)
pl = Paddle(10,170)
pr = Paddle(580,170)




def main():
	pygame.init()
	screen = pygame.display.set_mode((600,400))
	pygame.display.set_caption('Pong')

	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((0, 0, 0))
	pscore1 = 0
	pscore2 = 0
	
	clock = pygame.time.Clock()
	pygame.key.set_repeat(5,5)
	
	def repaint():
		
		screen.blit(background, (0,0))
		background.fill((0, 0, 0))
		b.move()
		pygame.draw.rect(background, (250,250,250), b.rect, 0)
		pygame.draw.rect(background, (250,250,250), pl.rect, 0)
		pygame.draw.rect(background, (250,250,250), pr.rect, 0)
		pygame.display.flip()

	while True:
		clock.tick(60)
		
		#bouncing off paddles
		
		#player 1 scored
		if b.rect.x > 620:
			time.sleep(2)
			b.__init__(-1)
			pl.__init__(10,200)
			pr.__init__(580,200)
			pscore1 += 1
			print "Player 1 Score: ", pscore1, " | ", pscore2, " :Player 2 Score"

		# player 2 scored
		if b.rect.x < -20:
			time.sleep(2)
			b.__init__(1)
			pl.__init__(10,200)
			pr.__init__(580,200)
			pscore2 += 1
			print "Player 1 Score: ", pscore1, " | ", pscore2, " :Player 2 Score"


		keys = pygame.key.get_pressed()

		if keys[K_UP]:
			pr.move(-5)
		if keys[K_DOWN]:
			pr.move(5)
		if keys[K_q]:
			pl.move(-5)
		if keys[K_a]:
			pl.move(5)

		for event in pygame.event.get():
			if event.type == QUIT:
				return False
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					return False
		if pscore1 == 9 or pscore2 == 9:
			return False

		repaint()
	
main()
