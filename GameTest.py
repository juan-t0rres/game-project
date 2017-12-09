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
class Zombies(pygame.sprite.Sprite):
    def __init__(self, speed,image_file, location, dx, dy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
        self.x = location[0]
        self.y = location[1]
        self.dx = dx
        self.dy = dy
    def tick(self,x,y):
        if x > self.x:
            self.dx = self.speed
        elif x < self.x:
            self.dx = -self.speed
        if y > self.y:
            self.dy = self.speed
        elif y < self.y:
            self.dy = -self.speed
        self.x+=self.dx
        self.y+=self.dy
    def update(self, location):
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
zSpeed=3
displayx=800
displayy=600
fps=20

gd=pygame.display.set_mode((displayx,displayy))
pygame.display.set_caption("Test")

clock=pygame.time.Clock()
ge=False

zombies = []

x = 300
y = 300
dx=0
dy=0

time=0

ud=False
while not ge:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ge=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx=-block
                dy=0
            elif event.key == pygame.K_RIGHT:
                dx=block
                dy=0
            elif event.key == pygame.K_DOWN:
                dy=block
                dx=0
            elif event.key == pygame.K_UP:
                dy=-block
                dx=0
        else:
            dx = 0
            dy = 0
    time+=1
    y+=dy
    x+=dx
    if time==100:
        zombies.append(Zombies(random.randint(1,6),"Zombie.png",[random.randint(0,800),0],0,0))
        time=1
    for z in zombies:
        z.tick(x,y)
    #print(mapX,mapY)
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
    #print(x,y)
    gd.fill(colours[0])
    gd.blit(Bmap[mapX][mapY].image, Bmap[mapX][mapY].rect)
    pygame.draw.rect(gd,colours[0],[x,y,block,block])
    for z in zombies:
        z.update([z.x,z.y])
        gd.blit(z.image,z.rect)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
