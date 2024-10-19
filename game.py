import pygame
import sys
import math 

# Constants
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

pygame.init()

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Raycasting")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    
    pygame.display.flip()
    clock.tick(60)