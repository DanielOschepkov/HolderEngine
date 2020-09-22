#mapBuilder
import mapList
import pygame
from pygame import *
import holderDraw

class Platform(sprite.Sprite):
	def __init__(self, x, y, img):
		sprite.Sprite.__init__(self)
		self.image = Surface((100, 100))
		self.image = image.load(img)
		self.rect = Rect(x,y,100,100)

platforms = []

def build(screen, map):
	bx=by=0
	for row in map:
		for col in row:
			if col == "#":
				block = Platform(bx, by, "resource/images/bricks.png")
			elif col == "t":
				block = Platform(bx, by, "resource/images/pc.png")
			holderDraw.entities.add(block)
			platforms.append(block)
			bx += 100
		by += 100
		bx = 0