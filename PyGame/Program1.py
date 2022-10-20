import pygame
pygame.init() #--------------------------------------------- Initialising a Game
screen = pygame.display.set_mode((1000, 800)) #------------- Game Window Creation     
running = True #-------------------------------------------- Game Status
pygame.display.set_caption("SpaceInvaders") #--------------- Title Changes
pygame.display.set_icon(pygame.image.load("Pygame/ufo.png")) #----- Icon Changes

# THE MAIN GAME LOOP 
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            
