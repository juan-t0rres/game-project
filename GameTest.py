import pygame
import random

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
class Hero(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
pygame.init()

Bgrass = Background('grass.jpg', [0,0])
Bsand = Background('sand.jpg', [0,0])
Bstone = Background('stone.jpg', [0,0])
Bconcrete = Background('concrete.jpg', [0,0])
mapX=0
mapY=0
Bmap=[[Bsand,Bsand,Bsand],
      [Bstone,Bconcrete,Bgrass],
      [Bstone,Bgrass,Bgrass]]

colours=[(0,0,0),(255,0,0),(0,255,0),(0,0,255),(255,255,255)]
#          W       R          G         B          B

block=10
displayx=800
displayy=600
fps=random.randint(20,60)
gd=pygame.display.set_mode((displayx,displayy))
pygame.display.set_caption("Test")

clock=pygame.time.Clock()
ge=False

x = 300
y = 300
dx=0
dy=0
ud=False
while not ge:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ge=True
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                dx=-block
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                dx=block
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                dy=block
            if (event.key == pygame.K_UP or event.key == pygame.K_w):
                dy=-block
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and dx == -block:
                dx=0
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and dx is block:
                dx=0
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and dy is block:
                dy=0
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and dy == -block:
                dy=0
    y+=dy
    x+=dx
    if(x<0):
        x=displayx-block
        if(mapX>0):
            mapX-=1
        else:
            x=0
    elif(x>=displayx):
        x=0
        if(mapX<2):
            mapX+=1
        else:
            x=displayx-block
    if(y<0):
        y=displayy-block
        if(mapY>0):
            mapY-=1
        else:
            y=0
    elif(y>=displayy):
        y=0
        if(mapY<2):
            mapY+=1
        else:
            y=displayy-block
    print(x,y)
    gd.fill(colours[0])
    gd.blit(Bmap[mapX][mapY].image, Bmap[mapX][mapY].rect)
    pygame.draw.rect(gd,colours[0],[x,y,block,block])
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()
