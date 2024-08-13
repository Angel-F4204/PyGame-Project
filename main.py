import pygame
import random
import math
from pygame import mixer
#intialize the pygame
pygame.init()

#creating the screen:             X      Y
screen = pygame.display.set_mode((800, 600))


#background
background = pygame.image.load("background5.jpeg")

#background sound
mixer.music.load("background.wav")
mixer.music.play(-1)
#title and icon
pygame.display.set_caption("Milind World")
icon = pygame.image.load("chair.png")
pygame.display.set_icon(icon)

#player 
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0


#enemy
enemyImg = []
enemyX =[]
enemyY =[]
enemyX_change = []
enemyY_change = [] 
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("ghost.png"))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150)) 
    enemyX_change.append(0.1)
    enemyY_change.append(40)

#ready u cant see the bullet on the screen 
#fire - the bullet is currently moving 


#bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"

# font
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)

textX = 10
textY = 10

#game over text
over_font = pygame.font.Font('freesansbold.ttf',64)

def show_score(x,y):
    score = font.render("Score : "+ str(score_value), True, (255,255,255))
    screen.blit(score,(x,y))


def game_over_text():
    over_text = over_font .render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))


#blit means to draw on our game window
def player(x,y):
    screen.blit(playerImg,(x, y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x, y))


def fire_bullet(x,y):
    global bullet_state 
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16 , y+10))


def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance <27:
        return True
    else:
        return False
# the Game loop
running = True
while running:

    screen.fill((0,0,0))#rgb this line does not work yet we need next line
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #if a keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -0.6
               #d print("A is pressed")


            if event.key == pygame.K_d:
                playerX_change = 0.6
               # print("D is pressed")
                
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready": #checking if the bullet is on the screen
                   bullet_sound = mixer.Sound("laser.wav")
                   bullet_sound.play()
                    #get current x coordinate of the sapaceship
                   bulletX = playerX #bullet is not moving with the space ship

                   fire_bullet(bulletX, bulletY)
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0

    #checking for boundaries of spaceship no out of bounds
    playerX += playerX_change

    if playerX <=0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736


#enemy movment
    for i in range(num_of_enemies):

        #game pver
        if enemyY[i] >600: 
            for j in range(num_of_enemies):
                enemyY[j] =2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]

        if enemyX[i] <=0:
            enemyX_change[i] = .5
            enemyY[i] += enemyY_change[i] #this is making the enemy move further down
        elif enemyX[i] >= 736:
            enemyX_change[i] = -.5
            enemyY[i] += enemyY_change[i]

        #collision
        collison = isCollision(enemyX[i],enemyY[i], bulletX, bulletY)
        if collison:
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            bulletY= 480
            bullet_state ="ready"
            score_value+=10
            
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)
        
        enemy(enemyX[i],enemyY[i],i)
    


    #bullet movement

    if bulletY<=0:
        bulletY = 480 
        bullet_state = "ready" #able to shoot multiple bullets

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY) #need to make sure the bullet is constantly updating 
        bulletY -= bulletY_change

   

    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()