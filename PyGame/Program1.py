import pygame #---------------------------------------------------- Pygame Package Import
import random
pygame.init() #---------------------------------------------------- Initialising a Game
screen = pygame.display.set_mode((1000, 800)) #-------------------- Game Window Creation     
running = True #--------------------------------------------------- Game Status
pygame.display.set_caption("SpaceInvaders") #---------------------- Title Change
pygame.display.set_icon(pygame.image.load("Pygame/ufo.png")) #----- Icon Change

# Creating the Main Game Element
playerimg = pygame.image.load("Pygame/protagonist.png") #---------- Protagonist
playerX = 464 #---------------------------------------------------- Player ka initial X Coord.
playerY = 700 #---------------------------------------------------- Player ka initial Y Coord.
playerXchange = 0 #------------------------------------------------ Player Coord. Change
playerYchange = 0 #----    ---------------------------------------- Player Coord. Change
def player(x, y): #------------------------------------------------ What will the Player Do?
    screen.blit(playerimg, (x, y))
    
# Creating the SideCharacters/Villains/Enemies    
enemy1img = pygame.image.load("Pygame/enemy1.png") #--------------- enemy1
enemy1img = pygame.transform.scale(enemy1img, (64, 64))   #-------- enemy1 Img rescaled
enemy1X = random.randint(0, 1000) #---------------------------------------------------- enemy1 ka initial X Coord.
enemy1Y = random.randint(0, 200) #------------------------------------------------------ enemy1 ka initial Y Coord.
enemy1Xchange = 0.5 #------------------------------------------------ enemy1 Coord. Change
enemy1Ychange = 0.03 #------------------------------------------------ enemy1 Coord. Change
def enemy1(x, y): #------------------------------------------------ What will the enemy1 Do?
    screen.blit(enemy1img, (x, y))
    
# THE MAIN GAME LOOP 
while running:
    # Stuff that appeares till the end
    screen.fill((70, 70, 128)) #---------------------------------- Setting BGcolor
    player(playerX, playerY) #------------------------------------ Calling in the Protagonist
    enemy1(enemy1X, enemy1Y) #------------------------------------ Calling in the Enemy
    # For different Keyboard Interupts, Mouse Clicks, Close or other events,
    # make cases inside For loop below to do specific tasks based on input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXchange = -1
            if event.key == pygame.K_RIGHT:
                playerXchange = 1
            if event.key == pygame.K_UP:
                playerYchange = -1
            if event.key == pygame.K_DOWN:
                playerYchange = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXchange = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerYchange = 0
    
    # Updating Player Coordinates
    playerX += playerXchange
    playerY += playerYchange
    # Making sure Player is in boundaries
    if playerX<=0:
        playerX = 0
    elif playerX >= 936:
        playerX = 936
    if playerY>=736:
        playerY = 736
    elif playerY <= 300:
        playerY = 300
    
    # Updating Enemy Coordinates
    enemy1X += enemy1Xchange
    enemy1Y += enemy1Ychange
    # Making sure Enemy is in boundaries
    if enemy1X<=0:
        enemy1X = 0
        enemy1Xchange = 0.5
    elif enemy1X >= 936:
        enemy1X = 936
        enemy1Xchange = -0.5
        
        
    pygame.display.update() 