import sys
sys.path.append('/home/pi/.local/lib/python3.7/site-packages')
import pygame
import time
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--dev", help="Development mode", action="store_true")
args = parser.parse_args()

if not args.dev:
    os.environ["SDL_FBDEV"] = "/dev/fb1"
    os.environ["SDL_MOUSEDEV"] = "/dev/input/event0"
    os.environ["SDL_MOUSEDRV"] = "TSLIB"
    os.environ["SDL_VIDEODRIVER"] = "fbcon"
from context import Context
from label import Label
from button import Button, IconButton

if not args.dev:
    from touchscreen import Touchscreen
    touchscreen = Touchscreen('/dev/input/event0')

pygame.init()
if not args.dev:
    pygame.mouse.set_visible(False)

context = Context()

def func1():
    print('Executing item 1')

icon_spacing = 90
IconButton(context, "./icons/play.png", 50, 46, func1)
IconButton(context, "./icons/stop.png", 50+icon_spacing, 50, func1)
IconButton(context, "./icons/save.png", 50+2*icon_spacing, 50, func1)
IconButton(context, "./icons/load.png", 50+3*icon_spacing, 53, func1)
IconButton(context, "./icons/settings.png", 50+4*icon_spacing, 50, func1)

Label(context, 'Status: Ready.', 30, 90, 40, context.black, centered=False)
Label(context, 'Transmission: 0.0 V', 30, 120, 40, context.black, centered=False)

from parametric import Parameter
x = Parameter('x', 0)
y = Parameter('y', 0)

from parameter_widget import IncrementLabel
IncrementLabel(context, 'X', x, 30, 230)
IncrementLabel(context, 'Y', y, 30, 330)

pygame.display.update()

''' Touchscreen/mouse loops '''
if not args.dev:
    while True:
        pos = touchscreen.position()
        print(pos)
        context.on_click(pos)
        pygame.display.update()

elif args.dev:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                context.on_click(pos)
                print(pos)
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   sys.exit()
        pygame.display.update()
