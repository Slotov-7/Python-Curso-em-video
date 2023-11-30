import pygame
pygame.init()
pygame.mixer.music.load('ex21.mp3')
input('Digite algo para tocar')
pygame.mixer.music.play()
input('Digite algo para parar')