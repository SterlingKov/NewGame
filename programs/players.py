import sys
from turtle import pos
import pygame
from settings import *

WHITE = (255,255,255)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        self.image = image

        self.rect = self.image.get_rect(center=pos)

class Grandma(pygame.sprite.Sprite):
    def __init__(self,pos,image):
        super().__init__()
        self.image = image

        self.rect = self.image.get_rect(center=pos)
        
        


        

class Floor(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        self.image = image

        self.rect = self.image.get_rect(center=pos)

class WalgreenEntr(pygame.sprite.Sprite):
    def __init__(self,pos,image):
        super().__init__()
        self.image = image

        self.rect = self.image.get_rect(center=pos)

class Lean(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        self.image = image

        self.rect = self.image.get_rect(center=pos)

        
        
class BlackBarBorder(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class InventoryBar(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        self.image = image

        self.rect = self.image.get_rect(center=pos)