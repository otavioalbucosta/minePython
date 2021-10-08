from typing import ForwardRef
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from sky import Sky

app = Ursina()
from voxel import Voxel
from hand import Hand
        
voxel = Voxel()
sky = Sky()
hand = Hand()

for z in range(8):
    for x in range(8):
        voxel = Voxel(pos=(x,0,z))
player = FirstPersonController()
app.run()