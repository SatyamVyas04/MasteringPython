import pygame #---------------------------------------------------- Pygame Package Import
import random
pygame.init() #---------------------------------------------------- Initialising a Game
screen = pygame.display.set_mode((1000, 800)) #-------------------- Game Window Creation     
running = True #--------------------------------------------------- Game Status
pygame.display.set_caption("SpaceInvaders") #---------------------- Title Change
pygame.display.set_icon(pygame.image.load("Pygame/ufo.png")) #----- Icon Change
back = pygame.image.load("Pygame/background.png")

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
enemy1X = random.randint(0, 1000) #-------------------------------- enemy1 ka initial X Coord.
enemy1Y = random.randint(0, 200) #--------------------------------- enemy1 ka initial Y Coord.
enemy1Xchange = 0.5 #---------------------------------------------- enemy1 Coord. Change
enemy1Ychange = 0.03 #--------------------------------------------- enemy1 Coord. Change
def enemy1(x, y): #------------------------------------------------ What will the enemy1 Do?
    screen.blit(enemy1img, (x, y))

# Creating Player Bullet
playerbulletimg = pygame.image.load("Pygame/bullet.png") #--------- ProtagonistBullet
bullet_state = "NotFired"
playerbulletX = 0 #------------------------------------------------ PlayerBullet ka initial X Coord.
playerbulletY = 0 #------------------------------------------------ PlayerBullet ka initial Y Coord.
playerbulletXchange = 0 #------------------------------------------ PlayerBullet Coord. Change
playerbulletYchange = -1 #--------------------------------------- PlayerBullet Coord. Change
def playerbullet(x, y): #------------------------------------------ What will the PlayerBullet Do?
    global bullet_state
    bullet_state = "Fired"
    screen.blit(playerbulletimg, (x, y))
    
# THE MAIN GAME LOOP 
while running:
    # Stuff that appeares till the end
    screen.blit(back, (0, 0)) #------------------------------------------- Setting BG
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
            if event.key == pygame.K_SPACE:
                if bullet_state == "NotFired":
                    playerbullet(playerX + 24, playerY)
                    playerbulletX = playerX+24
                    playerbulletY = playerY
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
        
    # Updating Bullet Coordinates
    if playerbulletY <=0:
        bullet_state = "NotFired"
    if bullet_state == "Fired":
        playerbullet(playerbulletX, playerbulletY)
        playerbulletX += playerbulletXchange
        playerbulletY += playerbulletYchange
        
    # Collision Detection
    enemy1rect = pygame.Rect(0, 0, 64, 64)
    enemy1rect.topleft = (enemy1X, enemy1Y)
    bulletrect = pygame.Rect(0, 0, 16, 16)
    bulletrect.topleft = (playerbulletX, playerbulletY)
    collide = bulletrect.colliderect(enemy1rect)
    if collide:
        enemy1X = random.randint(0, 1000)
        enemy1Y = random.randint(0, 200)
        bullet_state = "NotFired"
    pygame.display.update() 