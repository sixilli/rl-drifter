import pygame
from pygame.locals import *
import os

def event_handler(event, player):
    if event.type == KEYDOWN:
        if event.key == K_UP:
            player.moveup()
        if event.key == K_DOWN:
            player.movedown()
        if event.key == K_LEFT:
            player.moveleft()
        if event.key == K_RIGHT:
            player.moveright()

    elif event.type == KEYUP:
        if event.key == K_UP or event.key == K_DOWN or event.key == K_LEFT or event.key == K_RIGHT:
            player.movepos = [0, 0]
            player.state = 'still'

def load_png(image_name):
    base_path = os.getcwd()
    try:
        image = pygame.image.load(os.path.join(base_path, 'data', image_name))
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    
    except SystemExit:
        print('Cannot load image at ' + os.path.join(base_path, 'data', image_name))
        raise

    return image, image.get_rect()

