import pygame, sys, random

class PaddleA(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.posX = 30
        self.posY = 300
        self.image = pygame.image.load(r"C:\Users\Aldrich Fernandes\Python\Scripts\Projects\Ping Pong\Assets\PaddleA.gif")
        self.rect = self.image.get_rect()
        self.rect.center = [self.posX, self.posY]

    def moveUp(self):
        if self.posY - 50 >= 0:
            self.posY -= 10

    def moveDown(self):
        if self.posY + 50 <= 600:
            self.posY += 10

    def update(self):
        self.rect.center = [self.posX, self.posY]

class PaddleB(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.posX = 770
        self.posY = 300
        self.image = pygame.image.load(r"C:\Users\Aldrich Fernandes\Python\Scripts\Projects\Ping Pong\Assets\PaddleB.gif")
        self.rect = self.image.get_rect()
        self.rect.center = [self.posX, self.posY]

    def moveUp(self):
        if self.posY - 50 >= 0:
            self.posY -= 10

    def moveDown(self):
        if self.posY + 50 <= 600:
            self.posY += 10

    def update(self):
        self.rect.center = [self.posX, self.posY]

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.posX = 400
        self.posY = 300
        
        self.dx = 2
        self.dy = 2

        self.image = pygame.image.load(r"C:\Users\Aldrich Fernandes\Python\Scripts\Projects\Ping Pong\Assets\Ball.gif")
        self.rect = self.image.get_rect()
        self.rect.center = [self.posX, self.posY]
    
    def CollisionCheck(self):
        #Border
        if self.posY < 10:
            self.dy *= -1

        elif self.posY > 590:
            self.dy *= -1
        
        elif self.posX > 790:
            self.posX = 400
            self.posY = 300
            self.dx = 2
            if random.randint(1,10) <= 5:
                self.dx *= -1
        
        elif self.posX < 10:
            self.posX = 400
            self.posY = 300
            self.dx = 2
            if random.randint(1,10) <= 5:
                self.dx *= -1

        #Paddle
        self.PaddleCollision = pygame.sprite.spritecollide(Ball, Paddles, False)
        if len(self.PaddleCollision) > 0:
            self.dx *= -1.2
            self.PaddleCollision.clear()

    def GameOver(self):
        pygame.quit()
        sys.exit()
    
    def update(self):
        self.posX += self.dx
        self.posY += self.dy
        self.rect.center = [self.posX, self.posY]


pygame.init()
screen = pygame.display.set_mode((800,600))
background = pygame.image.load(r"C:\Users\Aldrich Fernandes\Python\Scripts\Projects\Ping Pong\Assets\CityBG.gif")
clock = pygame.time.Clock()

Paddles = pygame.sprite.Group()
PaddleA = PaddleA()
PaddleB = PaddleB()
Paddles.add(PaddleA, PaddleB)

Balls = pygame.sprite.Group()
Ball = Ball()
Balls.add(Ball)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    elif keys[pygame.K_w]:
        PaddleA.moveUp()
    elif keys[pygame.K_s]:
        PaddleA.moveDown()
    elif keys[pygame.K_UP]:
        PaddleB.moveUp()
    elif keys[pygame.K_DOWN]:
        PaddleB.moveDown()

    pygame.display.flip()
    screen.blit(background, (0,0))
    Paddles.draw(screen)
    Balls.draw(screen)
    Ball.CollisionCheck()
    Paddles.update()
    Balls.update()
    clock.tick(60)