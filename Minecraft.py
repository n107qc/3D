
from ursina import *
from ursina import Default, camera
from ursina.prefabs.sky import Sky
from ursina.prefabs.first_person_controller import FirstPersonController
from numpy import floor

import os
app = Ursina()
from Settings import*
from Models import Block, WorldEdit



p = FirstPersonController()
p.x = CHUNKSIZE/2
p.z = CHUNKSIZE/2
p.y = 10
p.gravity = 0.5
sky = Sky(texture = 'sky_sun')
scene.fog_density = .8
scene.fog_density =(50,200)

world = WorldEdit(p)
world.generate_world()

def input(key):
    p.gravity = 0.5

# cube = Entity(model='cube', texture = "grass", scale=1, collider='box')
# cube.position = (0,2,3)
#Honda = Entity(model='Asets\\Honda\\scene',scale = 1,collider='box')
#Honda.position =(0,5,0)
#ground = Entity(model ='quad',texture='grass',scale = 64,
                #position=(-2,0,0),texture_scale = (4,4),collider='box')




window.fullscreen = True
app.run()


