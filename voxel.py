from ursina import *

class Voxel(Button):
    grass_texture = load_texture('assets/grass_block.png')
    stone_texture = load_texture('assets/stone_block.png')
    brick_texture = load_texture('assets/brick_block.png')
    dirt_texture = load_texture('assets/dirt_block.png')
    block_pick = grass_texture

    def __init__(self, text='', pos = (0,0,0), texture = 'assets/grass_block.png'):
        
        
        super().__init__(
            parent = scene,
            position = pos,
            model = 'assets/block',
            origin_y = 0.5,
            texture = texture,
            color = color.color(random.uniform(0.9,1),0,random.uniform(0.9,1)),
            highlight_color = color.lime,
            scale = 0.5
        )
    def update(self):
        if held_keys['1']: self.block_pick = self.grass_texture
        if held_keys['2']: self.block_pick = self.stone_texture
        if held_keys['3']: self.block_pick = self.brick_texture
        if held_keys['4']: self.block_pick = self.dirt_texture

    def input(self,key):
        if self.hovered:
            if key == 'right mouse down':
                voxel = Voxel(pos= self.position + mouse.normal, texture=self.block_pick)
            if key == 'left mouse down':
                destroy(self)