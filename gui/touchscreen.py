import evdev

class Touchscreen:
    def __init__(self, addr, width=320, height=240):
        self.width, self.height = width, height
        self.device = evdev.InputDevice(addr)

    @staticmethod
    def parse_events(dev):
        pos = [None, None]
        sync_counter = 0
        for event in dev.read_loop():
            #print(evdev.categorize(event))
            if event.code == 0 and event.type == 0:
                sync_counter += 1
            if sync_counter >= 2 and None not in pos:
                break
            if event.type == evdev.ecodes.EV_ABS:
                if event.code == 0:
                    pos[0] = event.value
                elif event.code == 1:
                    pos[1] = event.value

        return pos

    @staticmethod
    def to_coords(pos, height):
        ''' Converts an [X, Y] position from evdev coordinates to pygame coordinates.
            For a 320x240 display, Evdev coordinates are specified as:
                * Top left: (240, 0)
                * Bottom left: (0, 0)
                * Top right: (240, 320)
                * Bottom right): (0, 320)
            Pygame coordinates are conventional computer graphics coordinates with
            the origin at the upper left corner.
        '''
        return [pos[1], height-pos[0]]

    def position(self):
        raw_position = Touchscreen.parse_events(self.device)
        coords = Touchscreen.to_coords(raw_position, self.height)
        return coords

if __name__ == '__main__':
    dev = Touchscreen('/dev/input/event0')
    while True:
        pos = dev.position()
        print(pos)
