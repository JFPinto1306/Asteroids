
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():

    pygame.init()

    # Starting a Clock Object
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = updatable, drawable
    AsteroidField.containers = updatable
    
    
    asteroidfield = AsteroidField()
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2, radius=PLAYER_RADIUS)

    
    dt = 0        

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

          
        updatable.update(dt)

        screen.fill("black")
        
        for drawer in drawable:
            drawer.draw(screen)
        
        
        pygame.display.flip()

        dt = clock.tick(60)/1000
        

if __name__=="__main__":
    main()
