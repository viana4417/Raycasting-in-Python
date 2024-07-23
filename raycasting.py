import pygame
import math
from settings import *

class Raycaster:
    def __init__(self, screen, player):
        self.screen = screen
        self.player = player
        self.stone_texture = pygame.image.load("textures/stone.png").convert()
        self.stone_texture = pygame.transform.scale(self.stone_texture, (TILE_SIZE, TILE_SIZE))

    def draw_background(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, WIDTH, HALF_HEIGHT - int(self.player.pitch * HEIGHT / FOV)))
        pygame.draw.rect(self.screen, (100, 100, 100), (0, HALF_HEIGHT - int(self.player.pitch * HEIGHT / FOV), WIDTH, HEIGHT))

    def cast_rays(self):
        start_x, start_y = self.player.pos
        sin_a = [math.sin(self.player.angle - HALF_FOV + ray * DELTA_ANGLE) for ray in range(NUM_RAYS)]
        cos_a = [math.cos(self.player.angle - HALF_FOV + ray * DELTA_ANGLE) for ray in range(NUM_RAYS)]
        
        for ray in range(NUM_RAYS):
            cur_angle = self.player.angle - HALF_FOV + ray * DELTA_ANGLE
            depth_v, texture_v = float('inf'), 0
            depth_h, texture_h = float('inf'), 0

            if cos_a[ray] != 0:
                x_v, dx = (start_x // TILE_SIZE) * TILE_SIZE + TILE_SIZE, TILE_SIZE
                if cos_a[ray] < 0:
                    x_v, dx = (start_x // TILE_SIZE) * TILE_SIZE - 0.0001, -TILE_SIZE
                y_v = start_y + (x_v - start_x) * sin_a[ray] / cos_a[ray]
                for _ in range(MAX_DEPTH):
                    map_x, map_y = int(x_v // TILE_SIZE), int(y_v // TILE_SIZE)
                    if 0 <= map_x < map_width and 0 <= map_y < map_height:
                        if world_map[map_y][map_x] == '1':
                            depth_v = (x_v - start_x) / cos_a[ray]
                            texture_v = int((y_v % TILE_SIZE) * TILE_SIZE / TILE_SIZE)
                            break
                    else:
                        break
                    x_v += dx
                    y_v += dx * sin_a[ray] / cos_a[ray]

            if sin_a[ray] != 0:
                y_h, dy = (start_y // TILE_SIZE) * TILE_SIZE + TILE_SIZE, TILE_SIZE
                if sin_a[ray] < 0:
                    y_h, dy = (start_y // TILE_SIZE) * TILE_SIZE - 0.0001, -TILE_SIZE
                x_h = start_x + (y_h - start_y) * cos_a[ray] / sin_a[ray]
                for _ in range(MAX_DEPTH):
                    map_x, map_y = int(x_h // TILE_SIZE), int(y_h // TILE_SIZE)
                    if 0 <= map_x < map_width and 0 <= map_y < map_height:
                        if world_map[map_y][map_x] == '1':
                            depth_h = (y_h - start_y) / sin_a[ray]
                            texture_h = int((x_h % TILE_SIZE) * TILE_SIZE / TILE_SIZE)
                            break
                    else:
                        break
                    y_h += dy
                    x_h += dy * cos_a[ray] / sin_a[ray]

            if depth_v < depth_h:
                depth, texture_x = depth_v, texture_v
            else:
                depth, texture_x = depth_h, texture_h

            depth *= math.cos(self.player.angle - cur_angle)

            if depth < 0.1:
                depth = 0.1

            proj_height = PROJ_COEFF / (depth + 0.0001)
            proj_height *= 1 / math.cos(self.player.pitch)

            wall_column = pygame.Surface((SCALE, TILE_SIZE))
            wall_column.blit(self.stone_texture, (0, 0), (texture_x, 0, SCALE, TILE_SIZE))
            wall_column = pygame.transform.scale(wall_column, (SCALE, int(proj_height)))
            self.screen.blit(wall_column, (ray * SCALE, HALF_HEIGHT - proj_height // 2 - int(self.player.pitch * HEIGHT / FOV)))
