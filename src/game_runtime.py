import logging
import pygame
import sys
from pygame.locals import *

import constants as const
import characters.player as mc
import functions.draw_functions as draw

logging.basicConfig(filename="./logs/runtime.log", format='%(asctime)s %(message)s', filemode='w')
log = logging.getLogger()
log.setLevel(logging.INFO)

# pygame setup
pygame.init()

log.info(f"Initializing {const.TITLE} v.{const.VERSION} ...")
log.info(f"Resolution: [{const.RESOLUTION_WIDTH}, {const.RESOLUTION_HEIGHT}], FPS:{const.FRAME_LIMIT}")


pygame.display.set_caption(f"{const.TITLE} v.{const.VERSION}")

fps = pygame.time.Clock()
running = True
game_state = const.START_SCREEN
log.info(f"Loading game state: {game_state}")



P1 = mc.Player()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
            log.info("Quitting game ...")
            sys.exit()

    if game_state == const.START_SCREEN:
       draw.draw_start_menu()
    elif game_state == const.IN_GAME:
        const.SCREEN.fill(const.Colors.WHITE)
        P1.draw(const.SCREEN)
        P1.update()
    
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[MOUSEBUTTONDOWN]:
        log.info(f"{MOUSEBUTTONDOWN} was pressed, changing state to {const.IN_GAME}")
        game_state = const.IN_GAME

    pygame.display.update()
    fps.tick(const.FRAME_LIMIT)  # limits FPS 

