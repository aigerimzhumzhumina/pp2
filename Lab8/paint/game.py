import sys, pygame 
from pygame.locals import *
pygame.init() 
screen = pygame.display.set_mode((1000,600))
screen.fill((255, 255, 255))
brush = pygame.image.load(r"Lab8\paint\brush.png")
brush = pygame.transform.scale(brush,(128,128))
pygame.display.update()
clock = pygame.time.Clock()
z = 0

while 1:
    clock.tick(60)
    x,y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            z = 1 
        elif event.type == MOUSEBUTTONUP:
            z = 0
        if z == 1:
            screen.blit(brush, (x-64,y-64))
            pygame.display.update()
