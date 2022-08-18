import pygame
import sys
from settings import*
pygame.init()

constant_sprites = pygame.sprite.Group()

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill((255,255,255))
        self.image.set_colorkey((255,255,255))
        pygame.draw.rect(self.image, (100,100,100), [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Ball(pygame.sprite.Sprite):
    def __init__(self, x,y,width,height):
        self.image = pygame.Surface([width,height])
        self.image.fill((255,255,255))
        self.image.set_colorkey((255,255,255))
        pygame.draw.circle(self.image, (0,255,0), (50,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

paddle1 = Paddle(infoObject.current_w/6, infoObject.current_h/2+50,50,100)
paddle2 = Paddle(infoObject.current_w/6*5, infoObject.current_h/2+50,50,100)

ball = Ball(infoObject.current_w/2,infoObject.current_h/2,50,0)

constant_sprites.add(paddle1,paddle2)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    
    
    screen.fill((0,0,0))
    constant_sprites.update()
    constant_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)


