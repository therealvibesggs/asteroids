import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        random_angle = random.uniform(20, 50)
        A1_velocity = self.velocity.rotate(random_angle)
        A2_velocity = self.velocity.rotate(-random_angle)
        
        A1 = Asteroid(self.position.x, self.position.y, new_radius)
        A2 = Asteroid(self.position.x, self.position.y, new_radius)
        A1.velocity = A1_velocity * 1.2
        A2.velocity = A2_velocity * 1.2


