import pygame

TITLE = "BetaAttorney"
VERSION = "0.0.0"

RESOLUTION_WIDTH = 1280
RESOLUTION_HEIGHT = 720
FRAME_LIMIT = 30

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)

SCREEN = pygame.display.set_mode((RESOLUTION_WIDTH, RESOLUTION_HEIGHT))
SCREEN.fill(GREY)

START_SCREEN = "start_screen"
IN_GAME = "in_game"
END_SCREEN = "end_screen"