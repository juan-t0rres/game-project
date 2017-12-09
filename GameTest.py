import pygame
import random
pygame.init()
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
class Hero(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("character.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
    def update(self,location):
        self.rect.left, self.rect.top = location
class Projectile:
    xMove = 0
    yMove = 0
    x = 10
    y = 10
    def __init__(self,y,e, et):#boneless
        if(et==0):
            self.xMove = 20
            self.yMove = 0
        if (et == 1):
            self.xMove = -20
            self.yMove = 0
        if (et == 3):
            self.xMove = 0
            self.yMove = -20
        if (et == 4):
            self.xMove = 0
            self.yMove = 20
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
        self.update([self.x,self.y])
    def update(self, location):
        self.rect.left, self.rect.top = location


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
fps=60

gameDisplay=pygame.display.set_mode((displayx, displayy))
pygame.display.set_caption("Test")

gameClock=pygame.time.Clock()
gameOver=False

x = displayx//2
y = displayy//2
dx=0
dy=0

zombies = []
time=0

proj = projectTileList()
lastPressed = 0

while not gameOver:
    proj.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver=True
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                dx=-block
                lastPressed = 1
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                dx=block
                lastPressed = 0
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                dy=block
                lastPressed = 4
            if (event.key == pygame.K_UP or event.key == pygame.K_w):
                dy=-block
                lastPressed = 3
            if (event.key == pygame.K_SPACE):
                proj.add(Projectile(x, y, lastPressed))
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and dx == -block:
                dx=0
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and dx is block:
                dx=0
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and dy is block:
                dy=0
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and dy == -block:
                dy=0
    time+=1
    y+=dy
    x+=dx
    if time==100:
        zombies.append(Zombies(random.randint(1,6),"Zombie.png",[random.randint(0,800),0],0,0))
        time=1
    for z in zombies:
        z.tick(x,y)
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
    gameDisplay.fill(colours[0])
    gameDisplay.blit(Bmap[mapX][mapY].image, Bmap[mapX][mapY].rect)
    pygame.draw.rect(gameDisplay, colours[0], [x, y, block, block])
    proj.render(gameDisplay)
    for z in zombies:
        gameDisplay.blit(z.image,z.rect)
    pygame.display.update()
    gameClock.tick(fps)
pygame.quit()
quit()
