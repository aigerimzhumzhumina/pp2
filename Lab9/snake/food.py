import pygame
from random import randrange
from game_object import GameObject 
from game_object import Point 

class Food(GameObject):
    def __init__(self, tile_width):
        super().__init__([Point(20, 20)], (0, 255, 0), tile_width)

        self.parameters = [[(0, 120, 0), 3], [(0, 255, 0), 1]]
        self.cur = randrange(0, 2)

        self.color = self.parameters[self.cur][0]
        self.weight = self.parameters[self.cur][1]

        self.timer = 50
    

    def can_eat(self, head_location):
        result = None
        for point in self.points:
            if point.X == head_location.X and point.Y == head_location.Y:
                result = point
                break
        return result

    def change_pos(self):
        self.points.pop(0)
        self.points.append(Point(randrange(0, 15) * self.tile_width, randrange(0, 20) * self.tile_width))

        self.cur = randrange(0, 2)

        self.color = self.parameters[self.cur][0]
        self.weight = self.parameters[self.cur][1]

    
    def time_out(self):
        self.timer -= 1

        if self.timer <= 0:
            self.change_pos()
            self.timer = 50
            
    