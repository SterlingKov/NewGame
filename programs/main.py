import pygame
from settings import *
from players import *
pygame.init()

#print(infoObject.current_w, infoObject.current_h)

BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (100,100,100)
LGRAY = (210,210,210)
DBROWN = (101,67,33)

pygame.display.set_caption("gmae")

#sprites
constant_sprites = pygame.sprite.Group()

#room 0 sprites
room_0_sprites = pygame.sprite.Group()
room_1_sprites = pygame.sprite.Group()

entrances = pygame.sprite.Group()

player = Player((infoObject.current_w/2,infoObject.current_h/2),pspr)
floor = Floor((infoObject.current_w/4*2,540),floor_im)
p_drink = Lean((infoObject.current_w/2-200, infoObject.current_h/2-200),p_drink_im)
walgreen_entr = WalgreenEntr((infoObject.current_w/2,infoObject.current_h/2),walgreen_entr_im)
grandma = Grandma((600,600),grandma_im)
#p_drink1 = Lean((infoObject.current_w/2-50, infoObject.current_h/2-100),p_drink_im)

#border
black_bar_l = BlackBarBorder( 0,0,infoObject.current_w/4,infoObject.current_h)
black_bar_2 = BlackBarBorder( infoObject.current_w/4*3,0,infoObject.current_w/4,infoObject.current_h)
black_bar_3 = BlackBarBorder( 0,0,infoObject.current_w,infoObject.current_h/5)
black_bar_4 = BlackBarBorder( 0,infoObject.current_h/5*4,infoObject.current_w,infoObject.current_h/5)

#sprite list
constant_sprites.add(player,black_bar_l,black_bar_2,black_bar_3,black_bar_4)

#room sprites
room_0_sprites.add(floor,p_drink,grandma)
room_1_sprites.add(walgreen_entr)

#loop stuff
px = 300
py = 200
xincr=5
yincr=5


pressed = False

lvl=0

def proximity():
    if player.rect.x - p_drink.rect.x <= 50 and player.rect.x - p_drink.rect.x >= -50 and player.rect.y - p_drink.rect.y <= 50 and player.rect.y - p_drink.rect.y >= -50:
        return True
    else:
        return False



#inventory stuff
inv = []
inventory = pygame.sprite.Group()
inventory_bar = InventoryBar((infoObject.current_w/2, 915),inventory_bar_im)
inventory.add(inventory_bar)

dropped_items = []

def cck_for_drp_items(room):
    for i in room:
        if i == p_drink:
            dropped_items.append(i)


dropped_items_list = pygame.sprite.Group()

for i in range(len(dropped_items)):
    dropped_items_list.add(dropped_items[i])


def controls():
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

    
    constant_sprites.update()
    dropped_items_list.update()
    inventory.update()
    #sprite group drawing
    
    constant_sprites.draw(screen)
    dropped_items_list.draw(screen)
    inventory.draw(screen)

    #keybinds
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
            player.rect.x-=xincr
            if player.rect.x <= infoObject.current_w/4:
                player.rect.x+=xincr
    if keys[pygame.K_d]:
            player.rect.x+=xincr
            if player.rect.x+player_w >= infoObject.current_w/4*3:
                player.rect.x-=xincr
    if keys[pygame.K_s]:
            player.rect.y+=yincr
            if player.rect.y+player_h >= infoObject.current_h/5*4:
                player.rect.y-=yincr
    if keys[pygame.K_w]:
            player.rect.y-=yincr
            if player.rect.y <= infoObject.current_h/5:
                player.rect.y+=yincr

    
    if keys[pygame.K_e]:
        if proximity():
            print(1)
            for i in dropped_items:
                inv.append(i)
                dropped_items.pop(dropped_items.index(i))
                dropped_items_list.remove(i)
                inventory.add(i)
                if inv.index(i) == 0:
                    inv[inv.index(i)].rect.x = infoObject.current_w/2 - 61
                    inv[inv.index(i)].rect.y = 907
                    #dropped_items.append(p_drink1)
                    break
                elif inv.index(i) == 1:
                    inv[inv.index(i)].rect.x = infoObject.current_w/2 - 35
                    inv[inv.index(i)].rect.y = 907
                    break
                elif inv.index(i) == 2:
                    inv[inv.index(i)].rect.x = infoObject.current_w/2 - 9
                    inv[inv.index(i)].rect.y = 907
                    break
                elif inv.index(i) == 3:
                    inv[inv.index(i)].rect.x = infoObject.current_w/2 + 35
                    inv[inv.index(i)].rect.y = 907
                    break
                elif inv.index(i) == 4:
                    inv[inv.index(i)].rect.x = infoObject.current_w/2 + 61
                    inv[inv.index(i)].rect.y = 907
                    break



    #pygame.draw.rect(screen, BLACK, [0,0,infoObject.current_w/4,infoObject.current_h])
    #pygame.draw.rect(screen, BLACK, [infoObject.current_w/4*3,0,infoObject.current_w/4,infoObject.current_h])
    #pygame.draw.rect(screen, BLACK, [0,0,infoObject.current_w,infoObject.current_h/5])
    #pygame.draw.rect(screen, BLACK, [0,infoObject.current_h/5*4,infoObject.current_w,infoObject.current_h/5])

    pygame.display.flip()

class GameState():
    def __init__(self):
        self.state = 'intro'

    def intro(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type==pygame.MOUSEBUTTONDOWN:
                self.state='room_0'
        screen.blit(background,(0,0))

        pygame.display.flip()

    def room_0(self):
            self.state = 'room_0'
            controls()
            cck_for_drp_items(room_0_sprites)
            room_0_sprites.update()
            room_0_sprites.draw(screen)
            if player.rect.x > infoObject.current_w/2 - 20 and player.rect.x < infoObject.current_w/2 + 20 and player.rect.y < 225:
                self.state='room_1'
                player.rect.y = 800

    def room_1(self):
        self.state='room_1'
        controls()
        cck_for_drp_items(room_0_sprites)
        room_1_sprites.update()
        room_1_sprites.draw(screen)
        if player.rect.x > infoObject.current_w/2 - 20 and player.rect.x < infoObject.current_w/2 + 20 and player.rect.y > 810:
            self.state = 'room_0'
            player.rect.y = 235

        

    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        if self.state == 'room_0':
            self.room_0()
        if self.state=='room_1':
            self.room_1()

    
game_state = GameState()

clock=pygame.time.Clock()

while True:
    game_state.state_manager()
    clock.tick(60)
