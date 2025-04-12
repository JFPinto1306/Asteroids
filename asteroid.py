import pygame
from circleshape import CircleShape
import random 
from constants import *

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    
    def draw(self, surface):
        pygame.draw.circle(surface, 'white',(self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(20,50)
        #self.velocity = pygame.Vector2(0, 0)
        rand_dir_1 = self.velocity.rotate(rand_angle)
        rand_dir_2 = self.velocity.rotate(-rand_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid1.velocity = rand_dir_1
        asteroid2 = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid2.velocity = rand_dir_2
        #Asteroid(new_radius, self.position, rand_dir_2)
        
          
        

        