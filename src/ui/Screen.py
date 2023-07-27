import pygame
import constants as const

class Screen():
    def __init__(self):
        super().__init__() 
        self.surface = pygame.display.set_mode((const.RESOLUTION_WIDTH, const.RESOLUTION_HEIGHT))
        self.surface.fill(const.BLUE)
            
    def draw_image(self, image, image_coord = (0,0), fill = None):
        if fill != None:
            self.surface.fill(fill)
        self.surface.blit(image, image_coord)
            
    def draw_text(self, surface, text = None, text_coord = (0,0), text_color = const.WHITE, text_size = 40, text_bold = False):
        font = pygame.font.SysFont(const.TEXT_FONT, text_size, bold=text_bold)
        start_button_text = font.render(text, True, const.WHITE)
        
    def get_screen(self):
        return self.surface