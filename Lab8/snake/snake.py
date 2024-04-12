import pygame   
from color_palette import *  
import time   
import random   
pygame.init()   

 
WIDTH = 600
HEIGHT = 600
CELL = 30

 
level = 1
score = 0
snake_speed = 5

 
def draw_grid():
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

 
def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]

    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

 
screen = pygame.display.set_mode((HEIGHT, WIDTH))

 
class Point:
    def __init__(self, x, y):   
        self.x = x
        self.y = y

    def __str__(self):   
        return f"{self.x}, {self.y}"

 
class Snake:
    def __init__(self):  
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]  
        self.dx = 1  
        self.dy = 0   

    def move(self):  
        for i in range(len(self.body) - 1, 0, -1):  
            self.body[i].x = self.body[i - 1].x   
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx   
        self.body[0].y += self.dy

         
        if self.body[0].x == -1 or self.body[0].x == 20 or self.body[0].y == -1 or self.body[0].y == 20:
            return False

    def draw(self):   
        head = self.body[0]   
        pygame.draw.rect(screen, colorGREEN, (head.x * CELL, head.y * CELL, CELL, CELL))  
        for segment in self.body[1:]:   
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))  

    def check_collision(self, food):   
        head = self.body[0]   
        if head.x == food.pos.x and head.y == food.pos.y:   
            print("Got food!")  
            self.body.append(Point(head.x, head.y))   
            pygame.display.update()  
            food.change_pos()  
 
class Food:
    def __init__(self):   
        self.pos = Point(random.randrange(0, 19), random.randrange(0, 19))   

    def generate_new_position(self):   
        new_pos = Point(random.randrange(0, 19), random.randrange(0, 19))   
        while new_pos in snake.body:   
            new_pos = Point(random.randrange(0, 19), random.randrange(0, 19))
        return new_pos   
    def change_pos(self):   
        global score   
        self.pos = self.generate_new_position()   
        score += 1  

    def draw(self):   
        pygame.draw.rect(screen, colorRED, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))  
 
clock = pygame.time.Clock()

 
food = Food()   
snake = Snake()   

 
font = pygame.font.SysFont("Verdana", 60)
game__over = font.render("Game Over", True, colorBLACK)

 
done = False
while not done:   
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:   
            done = True   
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_RIGHT and snake.dx != -1:   
                snake.dx = 1   
                snake.dy = 0
            elif event.key == pygame.K_LEFT and snake.dx != 1:  
                snake.dx = -1  
                snake.dy = 0
            elif event.key == pygame.K_DOWN and snake.dy != -1:   
                snake.dx = 0   
                snake.dy = 1
            elif event.key == pygame.K_UP and snake.dy != 1:   
                snake.dx = 0   
                snake.dy = -1
    
    draw_grid_chess()  

    font = pygame.font.SysFont(None, 25)   
    text = font.render("Score: " + str(score) + "   Level: " + str(level), True, colorBLACK)  
    screen.blit(text, (10, 10))   

    if snake.move() == False:   
        done = True  
        screen.fill(colorRED)   
        screen.blit(game__over, (125, 225))  
        
        pygame.display.update()   
        time.sleep(2)  

    snake.check_collision(food)   

    if score > level * 3:   
        level += 1   
        snake_speed += 3   

    snake.draw()  
    food.draw()  

    pygame.display.flip()   
    clock.tick(snake_speed)   