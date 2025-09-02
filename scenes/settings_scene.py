from scenes.base_scene import BaseScene
from UI.slider import Slider
from UI.button import Button
from UI.dropdownmenu import DropdownMenu
from UI.inputfield import InputField
from UI.label import Label
from UI.grid import Grid

class SettingsScene(BaseScene):
    def __init__(self,settings,switch_scene_callback,save_settings_callback):
        super().__init__()
        self.save_settings_callback = save_settings_callback
        self.settings = settings
        window_width, window_height = self.settings.saved_settings["resolution"]
        
        self.headline_label = Label(text="Settings",fontsize=int(window_height * 0.16))
        self.headline_pos = (window_width / 2 - self.headline_label.rect.width / 2, 
                             window_height * 0.1 - self.headline_label.rect.height / 2)

        self.grid = Grid(outer_rect=(0,window_height*0.2,window_width,window_height*0.6),rows=8,cols=2)

        self.grid_slider_input = Grid(outer_rect=(0,0,self.grid.cell_width,self.grid.cell_height),rows=1,cols=2)

        self.grid_button = Grid(outer_rect=(0,window_height*0.8,window_width,window_height*0.2),
                                rows = 1, cols = 2)

        rect_height = self.grid_slider_input.cell_height*0.6

        grid_fontsize = int(window_height*0.05)

        self.volume_label = Label(text="Volume: ",fontsize=grid_fontsize)
        self.volume_slider = Slider(size=(self.grid_slider_input.cell_width*0.8,rect_height),max_val=100,
                                    start_val=self.settings.saved_settings["volume"]*100)
        self.volume_input = InputField(size=(self.grid_slider_input.cell_width*0.3,rect_height),input_type="numbers",
                                       fontsize=grid_fontsize,start_text="50",linked_element=self.volume_slider)
        self.volume_input.link_to(self.volume_slider)
        
        resolution_options = [[2560,1440],[2240,1260],[1920,1080],[1600,900],[1280,720],[960,540],[640,360]]

        self.resolution_label = Label(text="Resolution: ",fontsize=grid_fontsize)
        self.resolution_dropdown = DropdownMenu(size=(self.grid_slider_input.cell_width*0.7,rect_height),
                                                options=resolution_options,
                                                selected_index=resolution_options.index(self.settings.saved_settings["resolution"]),
                                                fontsize=grid_fontsize)

        self.controls_label = Label(text="Controls",text_style="underline",fontsize=grid_fontsize)

        inputField_size = (self.grid.cell_width * 0.4, rect_height)

        self.controls_label_up = Label(text="Move Up: ",fontsize=grid_fontsize)
        self.controls_input_up = InputField(size=inputField_size,fontsize=grid_fontsize,input_type="key",
                                            start_text=self.settings.saved_settings["controls"]["move_up"])

        self.controls_label_down = Label(text="Move Down: ",fontsize=grid_fontsize)
        self.controls_input_down = InputField(size=inputField_size,fontsize=grid_fontsize,input_type="key",
                                            start_text=self.settings.saved_settings["controls"]["move_down"])

        self.controls_label_left = Label(text="Move Left: ",fontsize=grid_fontsize)
        self.controls_input_left = InputField(size=inputField_size,fontsize=grid_fontsize,input_type="key",
                                            start_text=self.settings.saved_settings["controls"]["move_left"])

        self.controls_label_right = Label(text="Move Right",fontsize=grid_fontsize)
        self.controls_input_right = InputField(size=inputField_size,fontsize=grid_fontsize,input_type="key",
                                            start_text=self.settings.saved_settings["controls"]["move_right"])

        self.controls_label_attack = Label(text="Attack: ",fontsize=grid_fontsize)
        self.controls_input_attack = InputField(size=inputField_size,fontsize=grid_fontsize,input_type="key",
                                            start_text=self.settings.saved_settings["controls"]["attack"])

        button_fontsize = int(window_height*0.1)
        button_size = (self.grid_button.cell_width * 0.22, self.grid_button.cell_height*0.6)

        self.save_button = Button("Save",callback=self.save,size=button_size,fontsize=button_fontsize)
        self.exit_button = Button("Back",callback=lambda: switch_scene_callback("main_menu"),size=button_size,fontsize=button_fontsize)

        self.grid.add_object(obj=self.volume_label,row=0,col=0,rel_pos=(0.75,0.5))
        self.grid.add_object(obj=self.grid_slider_input,row=0,col=1,align="right")
        self.grid_slider_input.add_object(obj=self.volume_slider,row=0,col=0,align="center")
        self.grid_slider_input.add_object(obj=self.volume_input,row=0,col=1,align="left")
        
        self.grid.add_object(obj=self.resolution_label,row=1,col=0,rel_pos=(0.75,0.5))
        self.grid.add_object(obj=self.resolution_dropdown,row=1,col=1,rel_pos=(0.08,0.5))
        self.resolution_dropdown.update_label_pos()

        self.grid.add_object(obj=self.controls_label,row=2,col=0,rel_pos=(0.75,0.5))

        self.grid.add_object(obj=self.controls_label_up,row=3,col=0,rel_pos=(0.75,0.5))
        self.grid.add_object(obj=self.controls_input_up,row=3,col=1,rel_pos=(0.08,0.5))

        self.grid.add_object(obj=self.controls_label_down,row=4,col=0,rel_pos=(0.75,0.5))
        self.grid.add_object(obj=self.controls_input_down,row=4,col=1,rel_pos=(0.08,0.5))

        self.grid.add_object(obj=self.controls_label_left,row=5,col=0,rel_pos=(0.75,0.5))
        self.grid.add_object(obj=self.controls_input_left,row=5,col=1,rel_pos=(0.08,0.5))

        self.grid.add_object(obj=self.controls_label_right,row=6,col=0,rel_pos=(0.75,0.5))
        self.grid.add_object(obj=self.controls_input_right,row=6,col=1,rel_pos=(0.08,0.5))

        self.grid.add_object(obj=self.controls_label_attack,row=7,col=0,rel_pos=(0.75,0.5))
        self.grid.add_object(obj=self.controls_input_attack,row=7,col=1,rel_pos=(0.08,0.5))

        self.grid_button.add_object(obj=self.save_button,row=0,col=0,rel_pos=(0.75,0.5))
        self.grid_button.add_object(obj=self.exit_button,row=0,col=1,rel_pos=(0.08,0.5))

    def save(self):
        new_settings = [float(self.volume_input.text),
                        self.resolution_dropdown.options[self.resolution_dropdown.selected_index],
                        self.controls_input_up.text,
                        self.controls_input_left.text,
                        self.controls_input_down.text,
                        self.controls_input_right.text,
                        self.controls_input_attack.text]
        self.settings.save_settings(new_settings)
        self.save_settings_callback()
        return 

    def handle_events(self, events):
        self.grid.handle_events(events)
        self.grid_button.handle_events(events)
    
    def update(self):
        self.grid.update()
        self.grid_button.update()
        self.grid_slider_input.update()
    
    def draw(self,screen):
        screen.fill((30,30,30))
        self.headline_label.draw(screen, self.headline_pos)
        self.grid.draw(screen)
        self.grid_button.draw(screen)
        self.resolution_dropdown.draw(screen)