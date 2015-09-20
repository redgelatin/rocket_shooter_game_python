#-------------------------------------------------------------------------------
# Name:        main.py
# Purpose:     Main function to run game
#
# Author:      Red Gelatin
#
# Created:     06-09-2015
# Copyright:   (c) Red Gelatin
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from classes import *
import random

game_over = False

clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
coin_list = pygame.sprite.Group()
meteor_list = pygame.sprite.Group()
missile_list = pygame.sprite.Group()

background_image_path = "assets/background.png"

backgroundImageOne = pygame.image.load(background_image_path)
backgroundImageOne_position = [0, 0]

backgroundImageTwo = pygame.image.load(background_image_path)
backgroundImageTwo_position = [0, -560]

#Shoutout to Jacob LaVallee, owner of http://uncopyrightedmusic.net
background_music_path = "assets/background_music.ogg"
background_music = pygame.mixer.Sound(background_music_path)

player = Rocket("assets/rocket.png", 320, 390)
all_sprites.add(player)

score = 0
font = pygame.font.SysFont("monospace", 40)

# Game Loop
while not game_over:
    background_music.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                player.move(-2)

            elif event.key == pygame.K_RIGHT:
                player.move(2)

            if event.key == pygame.K_SPACE and player.ammo > 0:
                player.ammo -= 1
                missile = Missile("assets/missile.png", player.rect.x+22, player.rect.y-35)
                missile_list.add(missile)
                all_sprites.add(missile)


        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                player.move(2)

            elif event.key == pygame.K_RIGHT:
                player.move(-2)

    meteorspawn_intervalOne = random.randrange(0,400)
    meteorspawn_intervalTwo = random.randrange(0,400)
    coinspawn_intervalOne = random.randrange(0,300)
    coinspawn_intervalTwo = random.randrange(0,300)

    if meteorspawn_intervalOne == meteorspawn_intervalTwo:

        for i in range(random.randrange(3,6)):

            meteor = Meteor("assets/meteor.png", random.randrange(1,5))
            meteor.rect.x = random.randint(55,585)
            meteor.rect.y = random.randint(-400,-70)
            meteor_list.add(meteor)
            all_sprites.add(meteor)

    if coinspawn_intervalOne == coinspawn_intervalTwo:

        for i in range(random.randrange(1,4)):

            coin = Coin("assets/coin.png")
            coin.rect.x = random.randint(55, 585)
            coin.rect.y = random.randint(-100,-70)

            for meteor in meteor_list:
                if coin.rect.x != meteor.rect.x and coin.rect.x != meteor.rect.y and coin.rect.x >= 55 and coin.rect.x <= 617:
                    coin_list.add(coin)
                    all_sprites.add(coin)

                else:
                    coin.kill()

    all_sprites.update()

    screen.fill(DARKBLUE)

    screen.blit(backgroundImageOne, backgroundImageOne_position)
    screen.blit(backgroundImageTwo, backgroundImageTwo_position)

    if backgroundImageOne_position[1] < 560:
        backgroundImageOne_position[1] += 0.5
    if backgroundImageOne_position[1] >= 560:
        backgroundImageOne_position[1] = -560

    if backgroundImageTwo_position[1] < 560:
        backgroundImageTwo_position[1] += 0.5
    if backgroundImageTwo_position[1] >= 560:
        backgroundImageTwo_position[1] = -560

    for missile in missile_list:

        # Destroy missile off-screen
        if missile.rect.y <= -40:
            missile.kill()

        for meteor in meteor_list:
            #If the existing missile hits any existing meteor, remove from all Sprite groups
            if missile.rect.y <= meteor.rect.y + 50 and meteor.rect.x - 5 <= missile.rect.x <= meteor.rect.x + 60:
                meteor.kill()
                missile.kill()

    #Player and meteor detection
    meteor_hit_list = pygame.sprite.spritecollide(player, meteor_list, True)
    coin_hit_list = pygame.sprite.spritecollide(player, coin_list, True)

    #If player colides with meteor, player will lose health
    if len(meteor_hit_list) > 0:
        player.loseHealth(len(meteor_hit_list))

    #Increase score if player collides with coin
    if len(coin_hit_list) > 0:
        score += len(coin_hit_list)

    player.healthBar()

    if player.ammo < 10:
        player.ammo += 0.01

    player.shotsFired()

    display_score = font.render(str(score), 1, WHITE)
    screen.blit(display_score, (5, 5))

    all_sprites.draw(screen)
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()