from ursina import *

class Cube(Entity):
    def __init__(self, add_to_scene_entities=True, **kwargs):
        super().__init__(
            model = 'cube',
            color = color.white,
            texture = 'white_cube',
            rotation = Vec3(45,45,45)
        )