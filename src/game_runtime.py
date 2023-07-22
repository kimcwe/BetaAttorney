import logging
import pygame
import sys
from pygame.locals import *

import constants as const
from characters import Player
from functions import draw_functions
from ui import Button

logging.basicConfig(filename="./logs/runtime.log", format='%(asctime)s %(message)s', filemode='w')
log = logging.getLogger()
log.setLevel(logging.INFO)

def main():
    pygame.init()

    log.info(f"Initializing {const.TITLE} v.{const.VERSION} ...")
    log.info(f"Resolution: [{const.RESOLUTION_WIDTH}, {const.RESOLUTION_HEIGHT}], FPS:{const.FRAME_LIMIT}")


    pygame.display.set_caption(f"{const.TITLE} v.{const.VERSION}")

    fps = pygame.time.Clock()
    running = True
    game_state = const.START_SCREEN
    log.info(f"Loading game state: {game_state}")
    
    default_bg = pygame.Surface(const.SCREEN.get_size())
    default_bg = default_bg.convert()
    default_bg.fill(const.BLACK)
    const.SCREEN.blit(default_bg, (0,0))

    P1 = Player.Player()
    
    while running:
        # cursor_pos = pygame.mouse.get_pos()
        # pressed = pygame.mouse.get_pressed()[0]
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
                log.info("Quitting game ...")
                sys.exit()
                
            elif event.type == KEYDOWN:
                if game_state == const.START_SCREEN:
                    if event.key == K_KP_ENTER:
                        game_state = const.IN_GAME
                        log.info(f"Loading game state: {game_state}")
            elif event.type == MOUSEBUTTONDOWN:
                log.info(f"mouse button clicked at pos: {event.pos}")
                button = Button.Button("test button", (500,300), 'm')
                button.draw()
                logging.info(f"Drawing button")

        if game_state == const.START_SCREEN:
            draw_functions.draw_start_menu()
        elif game_state == const.IN_GAME:
            const.SCREEN.blit(default_bg, (0,0))
            P1.draw(const.SCREEN)
            P1.update()
        

        pygame.display.update()
        fps.tick(const.FRAME_LIMIT)

if __name__ == '__main__': main()