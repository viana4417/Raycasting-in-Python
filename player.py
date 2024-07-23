import pygame
import math
from settings import *

class Player:
    def __init__(self, pos):
        self.pos = pos
        self.angle = 0
        self.pitch = 0

    def move(self):
        keys = pygame.key.get_pressed()
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        
        if keys[pygame.K_w]:
            self.pos[0] += SPEED * cos_a
            self.pos[1] += SPEED * sin_a
        if keys[pygame.K_s]:
            self.pos[0] -= SPEED * cos_a
            self.pos[1] -= SPEED * sin_a
        if keys[pygame.K_a]:
            self.pos[0] += SPEED * sin_a
            self.pos[1] -= SPEED * cos_a
        if keys[pygame.K_d]:
            self.pos[0] -= SPEED * sin_a
            self.pos[1] += SPEED * cos_a

    def handle_mouse(self):
        mouse_dx, mouse_dy = pygame.mouse.get_rel()
        self.angle += mouse_dx * MOUSE_SENSITIVITY_X
        self.pitch += mouse_dy * MOUSE_SENSITIVITY_Y
        self.pitch = max(-MAX_PITCH, min(MAX_PITCH, self.pitch))

    def draw_crosshair(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), (HALF_WIDTH, HALF_HEIGHT), 3)
        pygame.draw.circle(screen, (255, 255, 255), (HALF_WIDTH, HALF_HEIGHT), 2)
