import pygame

class Context:
    white   = (255, 255, 255)
    red     = (255,   0,   0)
    green   = (  0, 255,   0)
    blue    = (  0,   0, 255)
    black   = (  0,   0,   0)
    cyan    = ( 50, 255, 255)
    magenta = (255,   0, 255)
    yellow  = (255, 255,   0)
    orange  = (255, 127,   0)

    def __init__(self, width=480, height=320, background_color='white'):
        self.background_color = getattr(self, background_color)
        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill(self.background_color)

        self.widgets = []

    def add_widget(self, widget):
        ''' Adds a clickable widget to be handled in the application loop. '''
        self.widgets.append(widget)

    def on_click(self, pos):
        for widget in self.widgets:
            if widget.is_clicked(pos):
                if widget.function is not None:
                    widget.function()
