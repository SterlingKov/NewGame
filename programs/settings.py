import pygame
pygame.init()
infoObject = pygame.display.Info()
#1920*1080
#width:960
#height:648
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h-60))

carryOn=True

background = pygame.image.load('intro_screen.png')

pspr = pygame.image.load('pspr.png').convert_alpha()
floor_im = pygame.image.load('floor.png').convert_alpha()
p_drink_im = pygame.image.load('p_drink.png').convert_alpha()
inventory_bar_im = pygame.image.load('inventory_bar.png').convert_alpha()
walgreen_entr_im = pygame.image.load('room_1.png').convert_alpha()
grandma_im = pygame.image.load('grandma.png').convert_alpha()


player_w, player_h = pspr.get_size()