  #Add the link as a comment-References:

#My first draft CAP2pygame: https://github.com/Pepdep2023/CAP2-Space-shooter#cap2-space-shooter

#Youtube: https://www.youtube.com/watch?v=FfWpgLFMI7w
#         https://www.youtube.com/@CodingWithRuss
#         https://www.youtube.com/@TechWithTim
#         https://youtube.com/@CodingWithRuss?si=OnxJaOigTpM_2FJu

# Articles
# Google Search: https://www.geeksforgeeks.org/pygame-tutorial/
#                https://oop-fall2016.readthedocs.io/en/latest/week1.html
#                https://copyassignment.com/complete-pygame-tutorial-and-projects/


#Importing necessary module
import pygame
import random
import math
from pygame import mixer
import unittest

#Initializing pygame
pygame.init()

# Creating screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

#Caption and Icon
pygame.display.set_caption("Space Shooter")

# Score
score_val = 0
scoreX = 5
scoreY = 5
font = pygame.font.Font('freesansbold.ttf', 20)

#Game over
game_over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Points: " + str(score_val),
                        True, (255,255,255))
    screen.blit(score, (x , y ))
 
def game_over():
    game_over_text = game_over_font.render("GAME OVER",
                                           True, (255,255,255))
    screen.blit(game_over_text, (190, 250))
 
# Background Sound
mixer.music.load('background.wav')
mixer.music.play(-1)

#Player 
playerImage = pygame.image.load('ufo.png')
playerImage = pygame.transform.scale(playerImage,(40,50))
player_X = 370
player_Y = 523
player_Xchange = 0

#Enemy
invaderImage = []
invader_X = []
invader_Y = []
invader_Xchange = []
invader_Ychange = []
no_of_invaders = 8

for num in range(no_of_invaders):
    invaderImage.append(pygame.image.load('final-boss.png'))
    invader_X.append(random.randint(64, 737))
    invader_Y.append(random.randint(30, 180))
    invader_Xchange.append(1.2)
    invader_Ychange.append(50)

# Bullet
# rest - bullet is not moving
# fire - bullet is moving
bulletImage = pygame.image.load('bullet.png')
bullet_X = 0
bullet_Y = 500
bullet_Xchange = 0
bullet_Ychange = 3
bullet_state = "rest"

# Collision 
def isCollision(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x1 - x2,2)) +
                         (math.pow(y1 - y2,2)))
    if distance <= 50:
        return True
    else:
        return False

def player(x, y):
    screen.blit(playerImage, (x - 16, y + 10))

def invader(x, y, i):
    screen.blit(invaderImage[i], (x, y))

def bullet(x, y):
    global bullet_state
    screen.blit(bulletImage, (x, y))
    bullet_state = "fire"


#Game loop
running = True
while running:

    #Screen fill(RGB)
    screen.fill((0, 255, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
  

  # Controlling the player movement from the arrow keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_Xchange = -1.7
            if event.key == pygame.K_RIGHT:
                player_Xchange = 1.7
            if event.key == pygame.K_SPACE:
               
             player_Xchange = 0

              # Fixing the change of direction of bullet
             if bullet_state == "rest":
                    bullet_X = player_X
                    bullet(bullet_X, bullet_Y)
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
    if event.type == pygame.KEYUP:
            player_Xchange = 0

    # adding the change in the player position
    player_X += player_Xchange
    for i in range(no_of_invaders):
        invader_X[i] += invader_Xchange[i]

  # restricting the spaceship so that
    # it doesn't go out of screen
    if player_X <= 16:
        player_X = 16
    elif player_X >= 750:
        player_X = 750    

        # bullet movement
    if bullet_Y <= 0:
        bullet_Y = 600
        bullet_state = "rest"
    if bullet_state == "fire":
        bullet(bullet_X, bullet_Y)
        bullet_Y -= bullet_Ychange

# movement of the invader
    for i in range(no_of_invaders):
         
        if invader_Y[i] >= 900:
            if abs(player_X-invader_X[i]) < 80:
                for j in range(no_of_invaders):
                    invader_Y[j] = 2000
                    explosion_sound = mixer.Sound('explosion.wav')
                    explosion_sound.play()
                game_over()
                break
 
        if invader_X[i] >= 735 or invader_X[i] <= 0:
            invader_Xchange[i] *= -1
            invader_Y[i] += invader_Ychange[i]



# Collision
    collision = isCollision(bullet_X, invader_X[i],
                                bullet_Y, invader_Y[i])
    if collision:
            score_val += 1
            bullet_Y = 600
            bullet_state = "rest"
            invader_X[i] = random.randint(64, 736)
            invader_Y[i] = random.randint(30, 200)
            invader_Xchange[i] *= -1
 
    invader(invader_X[i], invader_Y[i], i)
        


    player(player_X, player_Y)
    show_score(scoreX, scoreY)
    pygame.display.update() 
