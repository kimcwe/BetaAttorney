import logging
import pygame
import sys
from pygame.locals import *

import constants as const
from characters import Player
from ui import Button
from ui import Screen


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
    
    screen = Screen.Screen()
    P1 = Player.Player()
    
    print(pygame.font.get_fonts())
    
    image_background_title = pygame.image.load("assets/background/BackgroundTitle.png")
    screen.draw_image(image_background_title, (0,0))
    image_logo = pygame.image.load("assets/background/Logo.png")
    screen.draw_image(image_logo,  (const.RESOLUTION_WIDTH/2 - image_logo.get_width()/2, const.RESOLUTION_HEIGHT/2 - image_logo.get_height() + 150))
    
    while running:
        # cursor_pos = pygame.mouse.get_pos()
        # pressed = pygame.mouse.get_pressed()[0]
        screen_surface = screen.get_screen()
        if game_state == const.START_SCREEN:
            button = Button.Button(screen_surface)
            button.draw("NEW GAME", (const.RESOLUTION_WIDTH/2 - image_logo.get_width()/2,300), 'm')
        elif game_state == const.IN_GAME:
            # const.SCREEN.blit(default_bg, (0,0))
            # P1.draw(const.SCREEN)
            # P1.update()
            pass
        
        
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
                
 
        pygame.display.update()
        fps.tick(const.FRAME_LIMIT)

if __name__ == '__main__': main()