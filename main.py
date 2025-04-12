
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys
from shot import *

def main():

    pygame.init()

    # Starting a Clock Object
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = updatable, drawable
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    
    
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
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_colision(shot):
                    shot.kill()
                    asteroid.split()
                    break
            if asteroid.check_colision(player):
                print("Game Over")
                sys.exit()
                
            
        pygame.display.flip()

        dt = clock.tick(60)/1000
        

if __name__=="__main__":
    main()
