import pygame #---------------------------------------------------- Pygame Package Import
pygame.init() #---------------------------------------------------- Initialising a Game
screen = pygame.display.set_mode((1000, 800)) #-------------------- Game Window Creation     
running = True #--------------------------------------------------- Game Status
pygame.display.set_caption("SpaceInvaders") #---------------------- Title Change
pygame.display.set_icon(pygame.image.load("Pygame/ufo.png")) #----- Icon Change

# Creating the Main Game Element
playerimg = pygame.image.load("Pygame/arcade-game.png") #---------- Protagonist
playerX = 464 #---------------------------------------------------- Player ka initial X Coord.
playerY = 700 #---------------------------------------------------- Player ka initial Y Coord.
playerXchange = 0 #------------------------------------------------ Player Coord. Change
playerYchange = 0 #------------------------------------------------ Player Coord. Change
def player(x, y): #------------------------------------------------ What will the Player Do?
    screen.blit(playerimg, (x, y))
    
# Creating the SideCharacters/Villains/Enemies

# THE MAIN GAME LOOP 
while running: 
    # Stuff that appeares till the end
    screen.fill((70, 70, 128)) #---------------------------------- Setting BGcolor
    player(playerX, playerY) #------------------------------------ Calling in the Protagonist
        
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
    
    # Updating Coordinates
    playerX += playerXchange
    playerY += playerYchange
    # Making sure ship is in boundaries
    if playerX<=0:
        playerX = 0
    elif playerX >= 936:
        playerX = 936
        
    pygame.display.update() 