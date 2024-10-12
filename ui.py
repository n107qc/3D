from ursina import*
from ursina import Default, camera

Text.default_font = 'Asets/Shrift/F77MinecraftRegular-0VYv.ttf'

class MenuButton(Button):
    def __init__(self, text,action,x,y, parent):
        super().__init__(text=text,on_click=action,x = x, y = y,
                         parent = parent,
                         texture = 'Asets/Textures/oak.png'
                         scale = (0.6,0.1),
                         origin=(0,0)
                         ignore_paused = True,
                         color=color.color(0,0, random.uniform(0.9, 1)),
                         highlight_color=color.gray,
                         pressed_scale=1.05,
                         )
                         

class Menu(Entity):
    def __init__(self, game, **kwargs):
        super().__init__(parent=camera.ui, ignore_paused=True, **kwargs)
        game.menu = self
        self.bg = Sprite(texture='Asets\\BG\\bg.jpg', parent = self,z=1, color=color.white,scale=0.35)
        self.title = Text(text = 'Ursina^_^Craft',scale = 5, parent = self,origin=(0,0),x = 0,y = 0.4)
        self.music = Audio('Asets\\Sounds\\StockTune-Echoes Through Trees_1728725398.mp3'),volume = 0.3,loop=True,autoplay=True)


        MenuButton('Нова гра',game.generate_world,0,15,self)
        MenuButton('Завантажити гру',game.load_game,0,0,self)
        MenuButton('Збереги',application.save_game,0,-0.15,self)
        MenuButton('Вийти',application.quit,0,-0.3,self)
   
    def input(self,key):
        if key =='escape':
            self.menu.toggele_menu()

    def toggle_menu(self):
            application.paused = not application.paused
            self.enabled =   application.paused
            self.visible =  self.visible
            mouse.locked = not mouse.locked
            mouse.visible = not mouse.visible
if __name__ == '__main__':
    app = Ursina()
    menu = Menu(app)
    app.run()