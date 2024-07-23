import pygame
import math
from settings import *

class Map:
    def __init__(self, screen):
        self.screen = screen
        self.mini_map_stone_texture = pygame.image.load("textures/stone.png").convert()
        self.mini_map_stone_texture = pygame.transform.scale(self.mini_map_stone_texture, (MINI_MAP_TILE_SIZE, MINI_MAP_TILE_SIZE))

    def draw(self, player):
        for y, row in enumerate(world_map):
            for x, char in enumerate(row):
                if char == '1':
                    self.screen.blit(self.mini_map_stone_texture, (MAP_OFFSET_X + x * MINI_MAP_TILE_SIZE, MAP_OFFSET_Y + y * MINI_MAP_TILE_SIZE))

        mini_player_x = MAP_OFFSET_X + player.pos[0] * MAP_SCALE
        mini_player_y = MAP_OFFSET_Y + player.pos[1] * MAP_SCALE
        pygame.draw.circle(self.screen, (0, 255, 0), (int(mini_player_x), int(mini_player_y)), int(5 * MAP_SCALE))

        dir_x = player.pos[0] + math.cos(player.angle) * TILE_SIZE
        dir_y = player.pos[1] + math.sin(player.angle) * TILE_SIZE
        while True:
            map_x = int(dir_x // TILE_SIZE)
            map_y = int(dir_y // TILE_SIZE)
            if world_map[map_y][map_x] == '1':
                break
            dir_x += math.cos(player.angle)
            dir_y += math.sin(player.angle)
        mini_dir_x = MAP_OFFSET_X + dir_x * MAP_SCALE
        mini_dir_y = MAP_OFFSET_Y + dir_y * MAP_SCALE 
        pygame.draw.line(self.screen, (255, 0, 0), (int(mini_player_x), int(mini_player_y)), (int(mini_dir_x), int(mini_dir_y)), 2)
