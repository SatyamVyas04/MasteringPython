import sys, pygame, random
pygame.init()

# Window Setup
wnW = int(input("Enter Menu Width: "))
if wnW >=1500:
    wnW = 1500
    
wnH = int(input("Enter Window Height: "))
if wnH >= 750:
    wnH = 750

surface = pygame.display.set_mode((wnW, wnH))
pygame.display.set_caption("CollisionDetection")
clock = pygame.time.Clock()

# Menu Setup
menuW, menuH = wnW, int(wnH/5)
menu = pygame.Surface((menuW, menuH))
menu.fill("Gold")

# Menu Buttons Setup
# Plan: 4 buttons for [Circle Mouse interaction,
#                      Square Mouse interaction, 
#                      Square Square interaction,
#                      Circle Circle interaction] 

running = True
while running:
    surface.fill("White")
    # Menu
    surface.blit(menu, (0, wnH-menuH))
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    





    pygame.display.update()
    clock.tick(60)