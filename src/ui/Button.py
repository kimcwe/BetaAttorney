import pygame

import constants as const

SMALL = (10, 10)
MEDIUM = (75, 20)

class Button():
    def __init__(self, text=None, coord=(0,0), typeButton=None):
        super().__init__() 
        self.text = text
        self.coord = coord
        self.typeButton = typeButton
            
    def draw(self):
        if self.typeButton == "small":
            button = pygame.Surface(SMALL)
        else:
            button = pygame.Surface(MEDIUM)
            button_image = pygame.image.load("assets/UI/ButtonBlack.png")
            button.set_alpha(100)
            button.blit(button_image, self.coord)
            
            font = pygame.font.SysFont('impact', 40, bold=False)
            button_text = font.render(self.text, True, const.WHITE)
            button.blit(button_text, self.coord)