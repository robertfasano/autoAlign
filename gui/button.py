import pygame

class IconButton:
    def __init__(self, context, path, x, y, function=None):
        self.x, self.y = x, y
        self.function = function
        self.img = pygame.image.load(path)
        w, h = self.img.get_size()
        context.screen.blit(self.img, (x-w/2, y-w/2))

    def is_clicked(self, pos):
        x, y = pos
        w, h = self.img.get_size()
        return self.x-w/2 <= x <= self.x+w/2 and self.y-h/2 <= y <= self.y+h/2

class Button:
    def __init__(self, context, text, x, y, h, w, c, function=None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.context = context
        self.text = text
        self.function = function
        self.label = Label(self.context, text, x, y, 42, c)

        self.rect = pygame.Rect(x, y, w, h)
        self.rect.center = (x, y)
        pygame.draw.rect(self.context.screen, blue, self.rect ,3)

    def is_clicked(self, pos):
        ''' Returns True if the passed position tuple is inside the button. '''
        x, y = pos
        return self.x-self.w/2 <= x <= self.x+self.w/2 and self.y-self.h/2 <= y <= self.y+self.h/2
