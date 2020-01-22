import sys, pygame
import time
import os
os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"

from context import Context
from label import Label
from button import Button, IconButton

pygame.init()
context = Context()

def func1():
    print('Executing item 1')

icon_spacing = 90
IconButton(context, "./icons/play.png", 50, 46, func1)
IconButton(context, "./icons/stop.png", 50+icon_spacing, 50, func1)
IconButton(context, "./icons/save.png", 50+2*icon_spacing, 50, func1)
IconButton(context, "./icons/load.png", 50+3*icon_spacing, 53, func1)
IconButton(context, "./icons/settings.png", 50+4*icon_spacing, 50, func1)

Label(context, 'Status: Ready.', 30, 90, 50, context.black, centered=False)
Label(context, 'Transmission: 0.0 V', 30, 132, 50, context.black, centered=False)

from parametric import Parameter
x = Parameter('x', 0)
y = Parameter('y', 0)

from parameter_widget import IncrementLabel
IncrementLabel(context, 'X', x, 30, 180)
IncrementLabel(context, 'Y', y, 30, 245)

# While loop to manage touch screen inputs
while 1:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
            context.on_click(pos)

#ensure there is always a safe way to end the program if the touch screen fails
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
    pygame.display.update()
