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

#Import files
from Classes import *

#Loop until the user clicks the close button
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Create group to contain all sprites
all_sprites = pygame.sprite.Group()
coin_list = pygame.sprite.Group()
meteor_list = pygame.sprite.Group()
missile_list = pygame.sprite.Group()

#Access background and set positions
backgroundImageOne = pygame.image.load("background.png")
backgroundImageOne_position = [0, 0]
backgroundImageTwo = pygame.image.load("background.png")
backgroundImageTwo_position = [0, -560]

#Create player
player = Rocket("rocket.png", 320, 390)
all_sprites.add(player)

score = 0
myfont = pygame.font.SysFont("monospace", 15)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            #Move right/left
            if event.key == pygame.K_LEFT:
                player.move(-2)
            elif event.key == pygame.K_RIGHT:
                player.move(2)
            #Shoot missile
            if event.key == pygame.K_SPACE:
                missile = Missile("missile.png", player.rect.x+22, player.rect.y-35)
                missile_list.add(missile)
                all_sprites.add(missile)

        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.move(2)
            elif event.key == pygame.K_RIGHT:
                player.move(-2)

    #Spawn meteors
    #Set two variables that generate random integers
    #Lower integer range to generate meteors and coins more often
    meteorspawn_intervalOne = random.randrange(0,400)
    meteorspawn_intervalTwo = random.randrange(0,400)
    coinspawn_intervalOne = random.randrange(0,300)
    coinspawn_intervalTwo = random.randrange(0,300)

    #If both variables are equal, meteors will spawn
    #This generates meteors at random intervals
    if meteorspawn_intervalOne == meteorspawn_intervalTwo:
        #Generate random 3-5 meteors
        print "Meteors Spawned"
        for i in range(random.randrange(3,6)):
            #Create meteor and spawn at random locations
            meteor = Meteor("meteor.png", random.randrange(1,5))
            meteor.rect.x = random.randint(55,585)
            meteor.rect.y = random.randint(-400,-70)
            #Add to lists
            meteor_list.add(meteor)
            all_sprites.add(meteor)

    #If both variables are equal, coins will spawn
    #This generates coins at random intervals
    if coinspawn_intervalOne == coinspawn_intervalTwo:
        #Generate random 1-3 coins
        for i in range(random.randrange(1,4)):
            #Create coins and spawn at random locations
            coin = Coin("coin.png")
            coin.rect.x = random.randint(55, 585)
            coin.rect.y = random.randint(-100,-70)
            #Try to keep coins and meteors apart
            for meteor in meteor_list:
                #Keep coin if coin spawned at a small distance from meteor
                if coin.rect.x != meteor.rect.x and coin.rect.x != meteor.rect.y and coin.rect.x >= 55 and coin.rect.x <= 617:
                    coin_list.add(coin)
                    all_sprites.add(coin)
                    #print "Coins spawned"
                #Destroy coins if they spawned near meteor
                else:
                    coin.kill()

    #Update the sprites
    all_sprites.update()

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(DARKBLUE)

    # Copy image to screen:
    screen.blit(backgroundImageOne, backgroundImageOne_position)
    screen.blit(backgroundImageTwo, backgroundImageTwo_position)

    #Use two sprites for the background
    #When one reaches y = -600 on the screen the other will be on screen
    #This creates a continuous effect that the boat is moving
    #Sprite 1
    if backgroundImageOne_position[1] < 560:
        backgroundImageOne_position[1] += 0.5
    if backgroundImageOne_position[1] >= 560:
        backgroundImageOne_position[1] = -560
    #Sprite 2
    if backgroundImageTwo_position[1] < 560:
        backgroundImageTwo_position[1] += 0.5
    if backgroundImageTwo_position[1] >= 560:
        backgroundImageTwo_position[1] = -560

    #Missile and meteor collision
    #Check every existing missile
    for missile in missile_list:
        #Check every existing meteor
        if missile.rect.y <= -40:
            #Destroy missile when it goes off screen
            missile.kill()
        for meteor in meteor_list:
            #If the existing missile hits any existing meteor, remove from all Sprite groups
            if missile.rect.y <= meteor.rect.y+50 and meteor.rect.x-5 <= missile.rect.x <= meteor.rect.x+60:
                meteor.kill()
                missile.kill()

    #Player and meteor detection
    meteor_hit_list = pygame.sprite.spritecollide(player, meteor_list, True)
    coin_hit_list = pygame.sprite.spritecollide(player, coin_list, True)

    #If player colides with meteor, player will lose health
    if len(meteor_hit_list) > 0:
        player.losehealth(len(meteor_hit_list))

    #Increase score if player collides with coin
    if len(coin_hit_list) > 0:
        score += len(coin_hit_list)

    #Create healthbar underneath rocket
    player.healthbar()

    #Display score underneath rocket
    label = myfont.render(str(score), 1, WHITE)
    screen.blit(label, (player.rect.x+5, player.rect.y+95))

    # Draw all the spites
    all_sprites.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()

