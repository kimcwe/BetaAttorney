import pygame

import constants as const

SMALL = (10, 10)
MEDIUM = (75, 20)

class Button(pygame.sprite.Sprite):
    def __init__(self, surface):
        super().__init__() 
        self.surface = surface
        self.button_image = pygame.image.load("assets/UI/ButtonBlack.png").convert_alpha()
        self.rect = self.button_image.get_rect()
            
    def draw(self, text="", coord=(0,0), typeButton=None):
        if typeButton == "small":
            pass
        else:
            button = self.surface
            button.blit(self.button_image, coord)
            
            font = pygame.font.SysFont(const.BUTTON_FONT, 30, True)
            button_text = font.render(text, True, const.WHITE)
            button.blit(button_text, (coord[0] + 15, coord[1] + 25))
        
    def get_button_image(self):
        return self.button_image
    
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()
        if self.rect.collidepoint(mouse_pos):
            if mouse_buttons[MOUSEBUTTONDOWN]:
                print('button clicked')
                pass
            else:
                print('hovering')
                pass
