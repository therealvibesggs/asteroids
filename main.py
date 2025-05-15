# imports open source pygame library

import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shots import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    update_group = pygame.sprite.Group()
    draw_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Player.containers = (update_group, draw_group)
    Asteroid.containers = (asteroid_group, update_group, draw_group)
    AsteroidField.containers = update_group
    Shot.containers = (shot_group, update_group, draw_group)

    asteroid_field = AsteroidField()

    new_player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT /2)
    fps = 60
    dt = 0
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # refresh player based on movement 
        update_group.update(dt)

        for asteroid in asteroid_group:
            if asteroid.collision_check(new_player):
                sys.exit("Game over!")

            for shot in shot_group:
                if asteroid.collision_check(shot):
                    asteroid.split()
                    shot.kill()

        # draw screen and draw player on screen
        screen.fill("black")
        for item in draw_group:
            item.draw(screen)
        pygame.display.flip()

        # limit the framewrate to 60 FPS
        dt = clock.tick(fps) / 1000


if __name__ == "__main__":
    main()
