#Main player file
import pygame
from pygame import *
import holderDraw

class Player(sprite.Sprite):
	def __init__(self,x,y,img):
		self.playerx = x
		self.playery = y
		self.movetox = 0
		self.movetoy = 0
		self.speed = 3
		self.active = False
		self.movenow = False
		sprite.Sprite.__init__(self)
		self.image = Surface((100,100))
		self.image = image.load(img)
		self.rect = Rect(self.playerx,self.playery,100,100)
	def update(self, px, py):
		if self.rect.x == px and self.rect.y == py:
			self.movenow = False
		if self.movenow == True:
			if self.rect.x> px:
				self.rect.x-= self.speed 
			elif self.rect.x < px:
				self.rect.x+= self.speed 
			if self.rect.y> py:
				self.rect.y -= self.speed 
			elif self.rect.y < py:
				self.rect.y += self.speed 
	def draw(self, screen):
		if self.active == True:
			screen.blit(self.image, (self.rect.x, self.rect.y))

