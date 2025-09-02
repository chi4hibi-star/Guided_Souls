from scenes.base_scene import BaseScene
from UI.button import Button
from UI.grid import Grid

class MainMenuScene(BaseScene):
    def __init__(self,settings,switch_scene_callback):
        super().__init__()
        window_width,window_height = settings.saved_settings["resolution"]

        self.grid = Grid(outer_rect=(0,window_height*0.2,window_width,window_height*0.6),
                         rows=4,cols=1)
        
        button_fontsize = int(window_height*0.1)
        button_size = (self.grid.cell_width*0.2,self.grid.cell_height*0.8)

        self.button_play = Button(text="Play",size=button_size,fontsize=button_fontsize,
                                  callback=lambda: switch_scene_callback("level_selection"))
        self.button_settings = Button(text="Settings",size=button_size,fontsize=button_fontsize,
                                      callback=lambda: switch_scene_callback("settings"))
        self.button_statistics = Button(text="Statistics",size=button_size,fontsize=button_fontsize,
                                        callback=lambda:switch_scene_callback("statistics"))
        self.button_quit = Button(text="Quit",size=button_size,fontsize=button_fontsize,
                                  callback=lambda:switch_scene_callback("quit"))

        self.grid.add_object(obj=self.button_play,row=0,col=0,align="center")
        self.grid.add_object(obj=self.button_settings,row=1,col=0,align="center")
        self.grid.add_object(obj=self.button_statistics,row=2,col=0,align="center")
        self.grid.add_object(obj=self.button_quit,row=3,col=0,align="center")
        
    def handle_events(self,events):
        self.grid.handle_events(events)

    def update(self):
        pass

    def draw(self,screen):
        screen.fill((30,30,30))
        self.grid.draw(screen)