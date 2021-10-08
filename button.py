from ursina import *

class MyButton(Button):
    def __init__(self, text='', **kwargs):
        super().__init__(
            parent = scene,
            model = 'cube',
            texture = 'brick',
            color = color.blue,
            highlight_color = color.red,
            pressed_color = color.lime
        )

    def input(self, key):
        if self.hovered:
            if key == ("left mouse down"):
                print("button pressed")
