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
class Projectile:
    xMove = 0
    yMove = 0
    x = 10
    y = 10
    def __init__(self,y,e, et):#boneless
        if(et==0):
            self.xMove = 2
            self.yMove = 0
        if (et == 1):
            self.xMove = -2
            self.yMove = 0
        if (et == 3):
            self.xMove = 0
            self.yMove = -2
        if (et == 4):
            self.xMove = 0
            self.yMove = 2
        self.x = y
        self.y = e

    def tick(self):
        self.x += self.xMove
        self.y += self.yMove

    def render(self,gd):
        blue = (0, 255, 0)
        pygame.draw.circle(gd, blue, [self.x,self.y], 5, 5)
class projectTileList:
    list = []
    def add(self, other):
        self.list.append(other)
    def tick(self):
        for x in self.list:
            x.tick()


    def render(self,gd):
        for x in self.list:
            x.render(gd)


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
fps=120

gd=pygame.display.set_mode((displayx,displayy))
pygame.display.set_caption("Test")

clock=pygame.time.Clock()
ge=False

x = 300
y = 300
dx=0
dy=0
ud=False


proj = projectTileList()

lastPressed = "right"
while not ge:
    proj.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ge=True
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                dx=-block
                lastPressed = "left"
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                dx=block
                lastPressed = "right"
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                dy=block
                lastPressed = "down"
            if (event.key == pygame.K_UP or event.key == pygame.K_w):
                dy=-block
                lastPressed = "up"
            elif (event.key == pygame.K_SPACE):
                if (lastPressed == "right"):
                    proj.add(Projectile(x, y, 0))
                if (lastPressed == "left"):
                    proj.add(Projectile(x, y, 1))
                if (lastPressed == "up"):
                    proj.add(Projectile(x, y, 3))
                if (lastPressed == "down"):
                    proj.add(Projectile(x, y, 4))
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
    #(mapX,mapY)

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
   # print(x,y)
    gd.fill(colours[0])
    gd.blit(Bmap[mapX][mapY].image, Bmap[mapX][mapY].rect)
    pygame.draw.rect(gd,colours[0],[x,y,block,block])
    proj.render(gd)
    pygame.display.update()

    clock.tick(fps)







pygame.quit()
quit()
