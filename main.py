import pygame
from settings import *
from player import Player
from raycasting import Raycaster
from map import Map

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    player = Player([577, 606])
    raycaster = Raycaster(screen, player)
    world_map = Map(screen)

    pygame.mouse.set_visible(False)
    pygame.event.set_grab(True)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        raycaster.draw_background()
        raycaster.cast_rays()
        world_map.draw(player)
        player.draw_crosshair(screen)
        player.move()
        player.handle_mouse()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
