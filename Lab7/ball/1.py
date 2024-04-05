import pygame
pygame.init()
screen = pygame.display.set_mode((200, 200))
x = 100  # x and y are coordinates of the center
y = 100
up_limit = 25
down_limit = 175
left_limit = 25
right_limit = 175
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, 'Red', (x, y), 25)
    pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] :
        x += 20
        x = min(x, right_limit)
    if keys[pygame.K_LEFT] :
        x -= 20
        x = max(x, left_limit)
    if keys[pygame.K_DOWN] :
        y += 20
        y = min(y,down_limit)
    if keys[pygame.K_UP] :
        y -= 20
        y = max(y, up_limit)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    clock.tick(60)