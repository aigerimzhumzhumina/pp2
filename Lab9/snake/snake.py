import pygame
import random
from game_object import GameObject 
from worm import Worm
from food import Food
from wall import Wall

def create_background(screen, width, height):
        colors = [(255, 255, 255), (212, 212, 212)]
        tile_width = 20
        y = 0
        while y < height:
                x = 0
                while x < width:
                        row = y // tile_width
                        col = x // tile_width
                        pygame.draw.rect(screen, colors[(row + col) % 2],pygame.Rect(x, y, tile_width, tile_width))
                        x += tile_width
                y += tile_width

done = False


pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

# Score and level
speed = 5
SCORE = 0
LEVEL = 1

worm = Worm(20)
food = Food(20)
wall = Wall(20)

while not done:
        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
            else:
                filtered_events.append(event)

        worm.process_input(filtered_events)
        worm.move()

        food.time_out()

        # check for wall collision
        pos = wall.can_hit(worm.points[0])
        if pos != None or worm.points[0].X < 0 or worm.points[0].X >= 400 or worm.points[0].Y < 0 or worm.points[0].Y >= 300:
              done = True
              break


        pos = food.can_eat(worm.points[0])
        if(pos != None):
            SCORE += food.weight
            worm.increase(pos)
            for i in range(food.weight - 1):
                pos.X += 1
                worm.increase(pos)
        
            food.change_pos()
            
            if len(worm.points) > 5:
                wall.next_level()
                worm.next_level()
                speed += 5
                LEVEL = (LEVEL + 1) % 2

        create_background(screen, 400, 300)
        
        food.draw(screen)
        wall.draw(screen)
        worm.draw(screen)
        
        pygame.display.flip()
        clock.tick(speed)