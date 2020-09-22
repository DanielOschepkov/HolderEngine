import pygame
from pygame import *
import mapBuilder

meshes = []
ui = pygame.sprite.Group()
entities = pygame.sprite.Group()

class uiBackground(sprite.Sprite):
	def __init__(self, x, y, img, w, h):
		sprite.Sprite.__init__(self)
		self.image = Surface((w, h))
		self.image = image.load(img)
		self.rect = Rect(x,y,w,h)
		ui.add(self)

class uiButton(sprite.Sprite):
	def __init__(self, x, y):
		sprite.Sprite.__init__(self)
		self.image = Surface((100, 100))
		self.image = image.load("resource/UI/start.png")
		self.rect = Rect(x,y,100,100)
		ui.add(self)

class StaticMesh:
	width = 0
	height = 0
	color = 0
	screenType = 0
	x = 0
	y = 0
	def __init__(self, x, y, height, width, color):
		self.height = height
		self.width = width
		self.color = color
		self.x = x
		self.y = y

def update(screen):
	ui.draw(screen)
	entities.draw(screen)