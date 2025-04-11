import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    
    def draw(self, surface):
        pygame.draw.circle(surface, color='white',(self.x, self.y), 2)

    def update(self, dt):
        self.x += self.velocity * dt
        self.y += self.velocity * dt
        