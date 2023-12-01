#Import neccesary libraries, pygame for the game itself, sys for work with variables, random for random values
import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Variables that we use for the game
SPEED = 5
SCORE = 0
COINSCORE = 0
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
#Loading background
background = pygame.image.load("AnimatedStreet.png")
 
#Create a white screen with set width and height
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)

#Naming the screen
pygame.display.set_caption("Game")
 
#Create an object of enemy
class Enemy(pygame.sprite.Sprite):
      #Enemy's methods, moving down
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        #If enemy hits the bottom, it will add points
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
#Create object of player
class Player(pygame.sprite.Sprite):
    #Player's methods, moving
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        Player.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        #Does not let car out of bounds
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

#Create object of coin
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
    #Coin's methods, moving coin
    def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
collectables = pygame.sprite.Group()
collectables.add(C1)
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    #Render display
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    coinscores = font_small.render(str(COINSCORE), True, BLACK)
    DISPLAYSURF.blit(coinscores, (370, 10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy. Ends the game with displaying red screen and "GAME OVER" message
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()   
               
    # To be run if the player collides with a coin. Adding more score to COINSCORE and kill coin
    if pygame.sprite.spritecollide(P1, collectables, True):
        for entity in collectables:
            entity.kill() 
        COINSCORE += 1

    # Check if C1 is not alive, then add it to the collectables group
    if not C1.alive():
        # Set C1's position to a new location
        C1.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
        collectables.add(C1)

    # Draw all sprites onto the screen and update their positions
    for entity in collectables:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
        
    pygame.display.update()
    FramePerSec.tick(FPS)