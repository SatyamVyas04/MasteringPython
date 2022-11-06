import sys, pygame, random
pygame.init()

# Window Setup
wnW = 1000
wnH = 700
surface = pygame.display.set_mode((wnW, wnH), pygame.RESIZABLE)
pygame.display.set_caption("CollisionDetection")
clock = pygame.time.Clock()

# Menu Buttons Setup
# Plan: 4 buttons for [Circle Mouse interaction,
#                      Square Mouse interaction, 
#                      Square Square interaction,
#                      Circle Circle interaction] 

running = True
while running:
    surface.fill("White")
    # Resize Check:
    wnW, wnH = surface.get_size()
    # Menu Setup
    menuW, menuH = wnW, int(wnH/5)
    menu = pygame.Surface((menuW, menuH))
    menu.fill("Gold")
    menu_TL_Y = wnH - menuH
    surface.blit(menu, (0, menu_TL_Y))
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    





    pygame.display.update()
    clock.tick(60)