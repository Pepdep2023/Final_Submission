# 1. Identify key functionality
    #player movement
    #collision detection
    #scoring 
    #Gameover condition
    #sound effects


import unittest
import pygame
import random
import math

class TestGame(unittest.TestCase):

   def setUp(self):
       pygame.init()
       self.screen = pygame.display.set_mode((800, 600))
       self.player_X = 370
       self.player_Y = 523
       self.player_Xchange = 0
       self.bullet_X = 0
       self.bullet_Y = 500
       self.bullet_Xchange = 0
       self.bullet_Ychange = 3
       self.bullet_state = "rest"
       self.score_val = 0
       self.invader_X = []
       self.invader_Y = []
       self.invader_Xchange = []
       self.invader_Ychange = []
       self.no_of_invaders = 8
       for num in range(self.no_of_invaders):
           self.invader_X.append(random.randint(64, 737))
           self.invader_Y.append(random.randint(30, 180))
           self.invader_Xchange.append(1.2)
           self.invader_Ychange.append(50)

   def test_player_movement(self):
       pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT))
       for event in pygame.event.get():
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                  self.player_Xchange = -1.7
           if event.type == pygame.KEYUP:
               self.player_Xchange = 0
       self.player_X += self.player_Xchange
       self.assertLess(self.player_X, 370)

   def isCollision(bullet_X, invader_X, bullet_Y, invader_Y):
    distance = math.sqrt(math.pow(bullet_X - invader_X, 2) + math.pow(bullet_Y - invader_Y, 2))
    return distance <= 27

   def test_collision_detection(self):
       self.assertTrue(isCollision(self.bullet_X, self.invader_X[0], self.bullet_Y, self.invader_Y[0]))
       self.invader_X[0] = 800
       self.assertFalse(isCollision(self.bullet_X, self.invader_X[0], self.bullet_Y, self.invader_Y[0]))

   def test_scoring(self):
       isCollision(self.bullet_X, self.invader_X[0], self.bullet_Y, self.invader_Y[0])
       self.assertEqual(self.score_val, 1)
       self.score_val = 0
       self.invader_X[0] = 800
       isCollision(self.bullet_X, self.invader_X[0], self.bullet_Y, self.invader_Y[0])
       self.assertEqual(self.score_val, 0)

   def test_game_over_condition(self):
       # Simulate a game over condition
       self.invader_Y[0] = 900
       self.player_X = 750

       # Run the game loop
       self.game_loop()

       # Check if the game over function was called
       self.assertTrue(self.game_over_called)

       

if __name__ == '__main__':
   unittest.main()

      