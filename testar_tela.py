import pygame, sys
from pygame.locals import *
from sys import exit

pygame.init()
WIDTH,HEIGHT = 600,600
screen = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
foto_01 = pygame.image.load("foto01.jpg")
foto_02 = pygame.image.load("foto02.jpg")
foto_03 = pygame.image.load("foto03.jpg")
foto_04 = pygame.image.load("foto04.jpg")
foto_05 = pygame.image.load("foto05.jpg")
foto_06 = pygame.image.load("foto06.jpg")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.blit(foto_01,(0,0))
    screen.blit(foto_02,(200,0))
    screen.blit(foto_03,(400,0))
    screen.blit(foto_04,(0,200))
    screen.blit(foto_05,(200,200))
    screen.blit(foto_06,(400,200))
    pygame.display.update()
