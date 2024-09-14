from kivy.uix.textinput import Texture
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
sky = Sky(texture = 'sky_sun')
scene.fog_density = .8
scene.fog_density =(50,200)

world = WorldEdit()
world.generate_world()

# cube = Entity(model='cube', texture = "grass", scale=1, collider='box')
# cube.position = (0,2,3)
#Honda = Entity(model='Asets\\Honda\\scene',scale = 1,collider='box')
#Honda.position =(0,5,0)
#ground = Entity(model ='quad',texture='grass',scale = 64,
                #position=(-2,0,0),texture_scale = (4,4),collider='box')



camera.clip_plane_far = 20 
window.fullscreen = True
app.run()


