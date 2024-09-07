from kivy.uix.textinput import Texture
from ursina import *
from ursina import Default, camera
from ursina.prefabs.sky import Sky
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise
from numpy import floor
from ursina.shaders import basic_lighting_shader
import os
app = Ursina()


MAPSIZE = 10
BASE_DIR = os.getcwd()
IMG_DIR = os.path.join(BASE_DIR, 'Asets\Textures')
block_textures = []

file_list = os.listdir(IMG_DIR)
for image in file_list:
    texture = load_texture('Asets\Textures' + os.sep + image)
    block_textures.append(texture)
   

print(block_textures)

print(file_list)

class Block(Button):
    id = 1

    def __init__(self,pos, **kwargs):
        super().__init__(
            parent=scene,
            model='cube',
            texture=block_textures[Block.id],
            scale = 1,
            collider='box',
            position = pos,
            color=color.color(0,0,random.uniform(0,9,1)),
            highlight_colour=color.gray,
            shader=basic_lighting_shader,
            **kwargs)

    def input(self,key):
        if self.hovered:
            d = self.distance_to(p)
            if key == 'left mouse down' and d<3:
                destroy(self) 
            if key == 'right mouse down' and d<3:
                block = Block(self.position+mouse.normal)
        if key == "scroll up":
            Block.id+1
            if len(block_textures)<=Block.id:
                Block.id = 0
        if key == "scroll down":
            Block.id-1
            if Block.id:
                Block.id = len(block_textures)-1
      
        
            






p = FirstPersonController()
block=Block((0,2,2))
sky = Sky(texture = 'sky_sun')
scene.fog_density = .8
scene.fog_density =(50,200)

# cube = Entity(model='cube', texture = "grass", scale=1, collider='box')
# cube.position = (0,2,3)
Honda = Entity(model='Asets\\Honda\\scene',scale = 1,collider='box')
Honda.position =(0,5,0)
#ground = Entity(model ='quad',texture='grass',scale = 64,
                #position=(-2,0,0),texture_scale = (4,4),collider='box')


noise = PerlinNoise(octaves=2, seed=4522)
for x in range(-10,10):
    for z in range(-10,10):
        y = floor(noise([x/24, z/24])*6)
        block = Block((x,0,))
 
app.run()

