import sys, pygame, random
pygame.init()

# Window Setup
wnW = 700
wnH = 700
surface = pygame.display.set_mode((wnW, wnH))
pygame.display.set_caption("CollisionDetection")
clock = pygame.time.Clock()

# Menu Setup
menuW, menuH = wnW, int(wnH/5)
padding = 0.1*menuH
sidepadding = 3.6*padding
menu = pygame.Surface((menuW, menuH))
menu.fill("Gold")
menu_TL_Y = wnH - menuH
surface.blit(menu, (0, menu_TL_Y))

# Buttons Setup
bH = bW = 0.8*menuH
pygame.draw.rect(surface, "blue", pygame.Rect(sidepadding, menu_TL_Y+padding, bW, bH))
pygame.draw.rect(surface, "blue", pygame.Rect(2*sidepadding+bW, menu_TL_Y+padding, bW, bH))
pygame.draw.rect(surface, "blue", pygame.Rect(3*sidepadding+2*bW, menu_TL_Y+padding, bW, bH))
pygame.draw.rect(surface, "blue", pygame.Rect(4*sidepadding+3*bW, menu_TL_Y+padding, bW, bH))

running = True
while running:
    # Collision Mechanism
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)