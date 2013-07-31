import os, sys
import pygame
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()
	
class Character(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
		self.image, self.rect = load_image('mario.png', -1)
		
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.rect.center = 400,200
		self.move = 10
		
	def update(self):		
		print 'update'		
		
	def _walkleft(self):
		newpos = self.rect.move((-10,0))
		self.rect = newpos 
		
	def _walkright(self):
		newpos = self.rect.move((10,0))
		self.rect = newpos 
    

def main():
	pygame.init()
	screen = pygame.display.set_mode((800,400))
	pygame.display.set_caption('Move that bitch')

	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((250, 250, 250))

	screen.blit(background, (0,0))
	pygame.display.flip()

	guy = Character()
	allsprites = pygame.sprite.RenderPlain((guy))
	clock = pygame.time.Clock()
	
	while 1:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
			if event.type == KEYDOWN and event.key == K_RIGHT:
				guy._walkright()
			if event.type == KEYDOWN and event.key == K_LEFT:
				guy._walkleft()
				
		clock.tick(60)
		
		screen.blit(background, (0, 0))
		allsprites.draw(screen)
		pygame.display.flip()
	

main()
