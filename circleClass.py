import pygame

class Circle:
    def __init__(self, x, y, color, radius, borderWidth):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.borderWidth = borderWidth

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius, self.borderWidth)