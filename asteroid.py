import pygame
import random
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=20)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        splitangle = random.uniform(20,50)
        newvel1 = pygame.math.Vector2.rotate(self.velocity, splitangle)
        newvel2 = pygame.math.Vector2.rotate(self.velocity, -splitangle)
        radnew = self.radius - ASTEROID_MIN_RADIUS
        A1 = Asteroid(self.position.x, self.position.y, radnew)
        A2 = Asteroid(self.position.x, self.position.y, radnew)
        A1.velocity = newvel1*1.2
        A2.velocity = newvel2*1.2