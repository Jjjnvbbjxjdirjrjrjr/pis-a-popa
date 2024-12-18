import pygame





class Tube:
    def __init__(self):
        self.x = 700
        self.y = 0
        self.width = 50
        self.length = 300


    def display(self, screen):
        pygame.draw.rect(screen,(200,30,15),(self.x,self.y,self.width,self.length))


    def move(self):
        self.x += 1





















































































