from scenes.base_scene import BaseScene
from UI.label import Label
from UI.grid import Grid
from UI.button import Button

class LevelSelectionScene(BaseScene):
    def __init__(self,settings,switch_scene_callback):
        super().__init__()
        self.switch_scene_callback = switch_scene_callback
        self.settings = settings
        window_width, window_height = self.settings.saved_settings["resolution"]
        
        self.headline_label = Label(text="Level Selection",fontsize=int(window_height * 0.16))
        self.headline_pos = (window_width / 2 - self.headline_label.rect.width / 2, 
                             window_height * 0.1 - self.headline_label.rect.height / 2)
        
        self.grid = Grid(outer_rect=(0,window_height*0.2,window_width,window_height*0.6),rows=2,cols=5)
        
        button_size = (self.grid.cell_width * 0.7, self.grid.cell_height*0.8)
        button_fontsize = int(window_height*0.1)

        for i in range(10):
            button = Button(text=f"Level {i+1}",callback=lambda: self.set_level_and_start(i),size=button_size,fontsize=button_fontsize)
            self.grid.add_object(obj=button,row=int(i/5),col=int(i%5),align="center")
        
        self.button_back = Button(text="Back",pos=(window_width*0.4,window_height*0.85),size=(window_width*0.2,window_height*0.1),
                                  fontsize=button_fontsize,callback=lambda: switch_scene_callback("main_menu"))

    def set_level_and_start(self,level):
        self.settings.selected_level = level
        self.switch_scene_callback("game_play")

    def handle_events(self,events):
        self.grid.handle_events(events)
        self.button_back.handle_events(events)
    
    def update(self):
        self.grid.update()
        self.button_back.update()
    
    def draw(self,screen):
        screen.fill((30,30,30))
        self.headline_label.draw(screen,self.headline_pos)
        self.grid.draw(screen)
        self.button_back.draw(screen)