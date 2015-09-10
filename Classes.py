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

import pygame

pygame.init()

WHITE    = ( 255, 255, 255 )
BLACK    = (   0,   0,   0 )
GREEN    = (   0, 255,  31 )
RED      = (  255,  0,   0 )
BLUE     = (    0,  0, 255 )
DARKBLUE = (    7,  0,  63 )
YELLOW   = ( 245, 255,  68 )

screen_size = (700, 500)
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("Rocket Blaster")



class Rocket(pygame.sprite.Sprite):

    health = 10
    change_x = 0
    score = 0

    def __init__(self, filename, x, y):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(YELLOW)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def healthBar(self):

        pygame.draw.rect(screen, RED, [self.rect.x + 5, self.rect.y + 90, 50, 5])
        if self.health >= 0:
            pygame.draw.rect(screen, GREEN, [self.rect.x + 5, self.rect.y + 90, 5 * self.health, 5])

    def loseHealth(self, hit):
        self.health -= hit

    def move(self, movement_x):
        self.change_x += movement_x

    def update(self):

        # Rocket movement and x_axis limiting
        self.rect.x += self.change_x
        if self.rect.x <= 55:
            self.rect.x = 55
        if self.rect.x >= 585:
            self.rect.x = 585



class Missile(pygame.sprite.Sprite):

    def __init__(self, filename, x, y):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(YELLOW)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y -= 3



class Meteor(pygame.sprite.Sprite):

    def __init__(self, filename, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(YELLOW)

        self.rect = self.image.get_rect()
        self.speed_meteor = speed

    def update(self):
        self.rect.y += self.speed_meteor



class Coin(pygame.sprite.Sprite):

    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(YELLOW)

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 2