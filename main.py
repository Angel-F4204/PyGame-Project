import pygame
import random
import math
#intialize the pygame
pygame.init()

#creating the screen:             X      Y
screen = pygame.display.set_mode((800, 600))


#background
background = pygame.image.load("background5.jpeg")
 
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
enemyImg = pygame.image.load("ghost.png")
enemyX = random.randint(0,735)
enemyY = random.randint(50,150)
enemyX_change = 0.1
enemyY_change = 40

#ready u cant see the bullet on the screen 
#fire - the bullet is currently moving 


#bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.3
bullet_state = "ready"

score = 0

#blit means to draw on our game window
def player(x,y):
    screen.blit(playerImg,(x, y))

def enemy(x,y):
    screen.blit(enemyImg,(x, y))


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
                playerX_change = -0.3
               #d print("A is pressed")


            if event.key == pygame.K_d:
                playerX_change = 0.3
               # print("D is pressed")
                
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready": #checking if the bullet is on the screen
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


    enemyX += enemyX_change

    if enemyX <=0:
        enemyX_change = 0.1
        enemyY += enemyY_change #this is making the enemy move further down
    elif enemyX >= 736:
        enemyX_change = -0.1
        enemyY += enemyY_change


    #bullet movement

    if bulletY<=0:
        bulletY = 480 
        bullet_state = "ready" #able to shoot multiple bullets

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY) #need to make sure the bullet is constantly updating 
        bulletY -= bulletY_change

    #collision
    collison = isCollision(enemyX,enemyY, bulletX, bulletY)
    if collison:
        bulletY= 480
        bullet_state ="ready"
        score+=10
        print(score)
        enemyX = random.randint(0,735)
        enemyY = random.randint(50,150)



    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()