import pygame

import constants as const

SMALL = (10, 10)
MEDIUM = (75, 20)

class Button():
    def __init__(self, surface):
        super().__init__() 
        self.surface = surface
            
    def draw(self, text="", coord=(0,0), typeButton=None):
        if typeButton == "small":
            button = pygame.Surface(SMALL)
        else:
            button = self.surface
            button_image = pygame.image.load("assets/UI/ButtonBlack.png").convert_alpha()
            button.blit(button_image, coord)
            
            font = pygame.font.SysFont(const.BUTTON_FONT, 30, True)
            button_text = font.render(text, True, const.WHITE)
            button.blit(button_text, (coord[0], coord[1]))
        return button_image
            
