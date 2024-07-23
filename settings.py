import math

# Game settings
WIDTH, HEIGHT = 1920, 1080
HALF_WIDTH, HALF_HEIGHT = WIDTH // 2, HEIGHT // 2
TILE_SIZE = 498
MAP_SCALE = 0.05
MINI_MAP_TILE_SIZE = int(TILE_SIZE * MAP_SCALE)
MAP_OFFSET_X = WIDTH - 12 * MINI_MAP_TILE_SIZE - 10
MAP_OFFSET_Y = 10
FOV = math.pi / 2
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
MAX_DEPTH = 8000
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 1.5 * DIST * TILE_SIZE
SCALE = WIDTH // NUM_RAYS
SPEED = 30
MOUSE_SENSITIVITY_X = 0.003
MOUSE_SENSITIVITY_Y = 0.003
MAX_PITCH = math.pi / 8

"""
0 - empty
1 - stone
"""
world_map = [
    "111111111111",
    "100000000001",
    "100000000001",
    "100000010001",
    "100011110101",
    "100010000001",
    "111111111111"
]

world_map = [list(row) for row in world_map]
map_width = len(world_map[0])
map_height = len(world_map)
