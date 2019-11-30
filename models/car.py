import pygame
from pygame.locals import *
from utils import load_png

class Car(pygame.sprite.Sprite):
    """
    Car class
    Returns: Car object
    Functions: reinit, update, move
    Attributes: which, speed
    """

    def __init__(self, side):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('vroom.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.side = side
        self.speed = 10
        self.state = 'still'
        self.hidden_discord_tech = 'aaron gay lul'
        self.reinit()

    def reinit(self):
        self.state = 'still'
        self.movepos = [0,0]
        if self.side == 'left':
            self.rect.midleft = self.area.midleft
        elif self.side == 'right':
            self.rect.midright = self.area.midright

    def update(self):
        newpos = self.rect.move(self.movepos)
        if self.area.contains(newpos):
            self.rect = newpos
        pygame.event.pump()

    def moveup(self):
        self.movepos[1] = self.movepos[1] - (self.speed)
        self.state = 'moveup'

    def movedown(self):
        self.movepos[1] = self.movepos[1] + (self.speed)
        self.state = 'movedown'

    def moveleft(self):
        self.movepos[0] = self.movepos[0] - (self.speed)
        self.state = 'moveleft'

    def moveright(self):
        self.movepos[0] = self.movepos[0] + (self.speed)
        self.state = 'moveright'