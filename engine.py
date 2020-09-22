#Engine construction
import pygame
from pygame import *
import colors
import holderDraw
import mapBuilder
import mapList
import audio_manager
import sceneManager
import player as plr
import GameLogic

screen = pygame.display.set_mode((640, 	320),0,32)
scene = "menu"

def update():
	holderDraw.update(screen)
	GameLogic.update(screen)
	for e in pygame.event.get():
		if e.type == pygame.MOUSEBUTTONDOWN:
			GameLogic.press(screen, e)
	