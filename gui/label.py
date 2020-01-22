import pygame

class Label:
    def __init__(self, context, text, x, y, fontsize, color, centered=True, justify=None):
        self.context = context
        self.text = text
        self.color = color
        self.font=pygame.font.Font(None,fontsize)
        self.text_surface=self.font.render(str(text), 1, (color))
        self.surface = pygame.surface.Surface(self.text_surface.get_size())

        if centered:
            self.rect = self.text_surface.get_rect(center=(x, y))
        else:
            self.rect = (x, y)
        self.text_rect = (0, 0)

        self.draw()

    def draw(self):
        self.surface.fill(self.context.background_color)
        self.surface.blit(self.text_surface, self.text_rect)
        self.context.screen.blit(self.surface, self.rect)

    def update(self, text):
        self.text = text
        self.text_surface = self.font.render(str(self.text), 1, (self.color))
        self.draw()
