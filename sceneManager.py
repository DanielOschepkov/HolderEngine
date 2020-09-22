import pygame
from pygame import *
import holderDraw
import audio_manager
import mapBuilder
import mapList
import engine

def clear():
	holderDraw.ui = pygame.sprite.Group()
	mapBuilder.platforms = []
	holderDraw.entities = pygame.sprite.Group()

def scene_one(sc):
	clear()
	mapBuilder.build(sc, mapList.level)
	
	
	
def scene_two(player, sc):
	clear()
	bgTwo = holderDraw.uiBackground(0,0,"resource/images/floor.jpg", 200, 200)
	bgTwo = holderDraw.uiBackground(0,700,"resource/images/floor.jpg", 200, 200)
	mapBuilder.build(sc, mapList.leveltwo)
	player.active = True