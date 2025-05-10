# imports open source pygame library

import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    new_player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT /2)
    fps = 60
    dt = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        new_player.update(dt)

        screen.fill("black")
        new_player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(fps) / 1000


if __name__ == "__main__":
    main()
