import os
from ursina import load_texture
MAPSIZE = 10
BASE_DIR = os.getcwd()
IMG_DIR = os.path.join(BASE_DIR, 'Asets\Textures')
block_textures = []

file_list = os.listdir(IMG_DIR)
for image in file_list:
    texture = load_texture('Asets\Textures' + os.sep + image)
    block_textures.append(texture)


