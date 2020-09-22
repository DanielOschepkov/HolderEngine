#HolderEngine v1.0
#Created by: Daniil Oschepkov
import pygame
from pygame import *
import engine
from engine import *
import audio_manager
import GameLogic

bgColor = (0,66,106)
BLACK = (0,0,0)
pygame.init()
pygame.display.set_caption("Holder Engine Android test")
mainLoop = True
clock = pygame.time.Clock()

GameLogic.init()

while mainLoop:
	engine.screen.fill((255,255,255))
	engine.update()
	pygame.display.update()
	clock.tick(30)