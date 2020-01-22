from label import Label
from button import IconButton

class IncrementLabel:
    step = 10

    def __init__(self, context, text, parameter, x, y):
        ''' A visual display for displaying and incrementing parametric.Parameter
            values in fixed steps.
        '''
        x *= context.xscale
        y *= context.yscale
        self.parameter = parameter
        fontsize = 80
        Label(context, text, int(x), int(y), fontsize, context.black, centered=False)
        button_x = int(x+90)
        button_y = int(y+26)
        context.add_widget(IconButton(context, "./icons/remove-circle.png", button_x, button_y, self.minus_x))
        self.value = Label(context, '+200.0', int(x+130), int(y), fontsize, context.black, centered=False)
        context.add_widget(IconButton(context, "./icons/add-circle.png", int(x+340),int( y+26), self.plus_x))
        self.update(self.parameter.value)

    def minus_x(self):
        self.update(str(float(self.value.text)-self.step))

    def plus_x(self):
        self.update(str(float(self.value.text)+self.step))

    def update(self, text):
        text = '{:>+{w}.{p}f}'.format(float(text), w=5, p=1)
        self.parameter(float(text))
        index=-1
        self.value.update(text)
        print(self.parameter)
