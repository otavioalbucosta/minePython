from ursina import *

class Hand(Entity):
    punch_audio = Audio('assets/punch_sound', loop = False, autoplay = False)
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'assets/arm',
            texture = 'assets/arm_texture.png',
            scale = 0.2,
            rotation = Vec3(150,-10,0),
            position = Vec2(0.6,-0.6)
        )

    def update(self):
        if held_keys['left mouse'] or held_keys['right mouse']:
            self.punch_audio.play()
            self.active()
        else:
            self.passive()

    def active(self):
        self.rotation = Vec3(160,-10,0)
        self.position = Vec2(0.3,-0.5)
    def passive(self):
        self.rotation = Vec3(150,-10,0)
        self.position = Vec2(0.6,-0.6)

    