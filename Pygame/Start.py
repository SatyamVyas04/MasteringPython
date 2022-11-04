import sys, pygame
# Basic Layout for any program
pygame.init()
screen = pygame.display.set_mode((750, 350))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()