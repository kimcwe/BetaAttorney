import pygame

import constants as const

def draw_start_menu():
    titleBackground = pygame.image.load("assets/background/BackgroundTitle.png")
    font = pygame.font.SysFont('impact', 40, bold=False)
    start_button = pygame.image.load("assets/UI/ButtonBlack.png")
    start_button_text = font.render('Start', True, const.WHITE)
    logo = pygame.image.load("assets/background/Logo.png")
    const.SCREEN.blit(titleBackground, (0,0))
    const.SCREEN.blit(start_button, (const.RESOLUTION_WIDTH/2 - start_button.get_width()/2, const.RESOLUTION_HEIGHT/2 + logo.get_height()/2 - 15))
    const.SCREEN.blit(logo, (const.RESOLUTION_WIDTH/2 - logo.get_width()/2, const.RESOLUTION_HEIGHT/2 - logo.get_height() + 150))
    const.SCREEN.blit(start_button_text, (const.RESOLUTION_WIDTH/2 - start_button_text.get_width()/2, const.RESOLUTION_HEIGHT/2 + logo.get_height()/2))


