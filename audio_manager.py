import pygame
from pygame import *

def simple_play(file):
	pygame.init()
	pygame.mixer.music.load(file)
	pygame.mixer.music.play()
	
def stop_all():
	pygame.mixer.music.stop()
	pygame.mixer.music.pause()