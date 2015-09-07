#-------------------------------------------------------------------------------
# Name:        Sprite classes
# Purpose:     File which will contain all classes for sprites
#
# Author:      Red Gelatin
#
# Created:     06-09-2015
# Copyright:   (c) Red Gelatin
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Import libraries and initialize pygame
import pygame
import random

pygame.init()
#Define Colours
WHITE    = ( 255, 255, 255)
BLACK    = (   0,   0,   0)
GREEN    = (   0, 255,  31)
RED      = (  255,  0,   0)
BLUE     = (    0,  0, 255)
DARKBLUE = (    7,  0,  63)
YELLOW   = ( 245, 255,  68)

#Set screen size
size = (700, 500)
screen = pygame.display.set_mode(size)
#Set name of window
pygame.display.set_caption("Rocket Blaster")

#Class for user-controlled Rocket
class Rocket(pygame.sprite.Sprite):
    #Attribues
    #Contains variables such as health, movement
    health = 10
    change_x = 0
    score = 0

    #Methods
    def __init__(self, filename, x, y):
        #Call the parent class
        pygame.sprite.Sprite.__init__(self)
        #Get the image and set background transparent
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(YELLOW)
        #Get the rectangular area that contains dimensions of the image
        self.rect = self.image.get_rect()
        #Set the location of the sprite
        self.rect.x = x
        self.rect.y = y

    #Display healthbar
    def healthbar(self):
        #Position of rectangles follow position of sprite
        pygame.draw.rect(screen,RED, [self.rect.x+5, self.rect.y+90, 50,5])
        if self.health >= 0:
            pygame.draw.rect(screen,GREEN, [self.rect.x+5, self.rect.y+90, 5*self.health,5])

    #Health function
    def losehealth(self, hit):
        self.health -= hit

    #Movement function
    def move(self, movement_x):
        self.change_x += movement_x

    #Update position of sprite
    def update(self):
        #Movement of rocket in the x-axis
        self.rect.x += self.change_x
        #Keep rocket with in a limited range in the x-axis
        #Set the rect.x of the rocket at a specific point if it reaches it
        if self.rect.x <= 55:
            self.rect.x = 55
        if self.rect.x >= 585:
            self.rect.x = 585

#Class for missile produced by rocket
class Missile(pygame.sprite.Sprite):

    #Methods
    def __init__(self, filename, x , y):
        #Call the parent class
        pygame.sprite.Sprite.__init__(self)
        #Get the image and set the background transparent
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(YELLOW)
        #Get the rectangular area that contains the dimentions of the image
        self.rect = self.image.get_rect()
        #set the location of the sprite
        self.rect.x = x
        self.rect.y = y

    #Update the movement of missiles
    def update(self):
        self.rect.y -= 3

#Class for Meteors
class Meteor(pygame.sprite.Sprite):

    #Methods
    def __init__(self, filename, speed):
        #Call the parent class
        pygame.sprite.Sprite.__init__(self)
        #Get the image and set the background transparent
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(YELLOW)
        #Get the rectangular area that contains the dimentions of the image
        self.rect = self.image.get_rect()
        #Set random speed for each meteor
        self.speed_meteor = speed

    #Update movement of meteors
    def update(self):
        self.rect.y += self.speed_meteor

#Class for Coins
class Coin(pygame.sprite.Sprite):

    #Methods
    def __init__(self, filename):
        #Call the parent class
        pygame.sprite.Sprite.__init__(self)
        #Get the image and set the background transparent
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(YELLOW)
        #Get the rectangular area that contains the dimentions of the image
        self.rect = self.image.get_rect()

    #Update movement of meteors
    def update(self):
        self.rect.y += 2


