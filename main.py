from settings import *
from scenes.main_menu_scene import MainMenuScene
from scenes.settings_scene import SettingsScene
from scenes.statistics_scene import StatisticsScene
from scenes.gameplay_scene import GamePlayScene
from scenes.level_selection import LevelSelectionScene
from sprites.graphics_loader import Graphics_Loader

class Game():
    def __init__(self):
        pg.init()
        self.settings = Settings(self.save_settings_callback)
        self.new_scenes()
        pg.display.set_caption('Guided Souls')

        self.running = True
        
        self.current_scene = self.main_menu_scene

    def run(self):
        while self.running:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    self.running = False
                
            if self.current_scene:
                self.current_scene.handle_events(events)
                self.current_scene.update()
                self.current_scene.draw(self.display_surface)
                pg.display.flip()
        pg.quit()

    def switch_scene(self,new_scene_name):
        if new_scene_name == "game_play":
            self.current_scene = self.game_play_scene
        elif new_scene_name == "level_selection":
            self.current_scene = self.level_selection
        elif new_scene_name == "settings":
            self.current_scene = self.settings_scene
        elif new_scene_name == "statistics":
            self.current_scene = self.statitics_scene
        elif new_scene_name == "main_menu":
            self.current_scene = self.main_menu_scene
        elif new_scene_name == "quit":
            self.running = False

    def save_settings_callback(self):
        del self.graphics_loader
        del self.main_menu_scene
        del self.settings_scene
        del self.statitics_scene
        del self.level_selection
        del self.game_play_scene
        del self.display_surface
        self.new_scenes()
        self.current_scene = self.settings_scene

    def new_scenes(self):
        self.display_surface = pg.display.set_mode(self.settings.saved_settings["resolution"])
        self.graphics_loader = Graphics_Loader()
        self.graphics_loader.scale_all(self.settings.saved_settings["resolution"])
        self.main_menu_scene = MainMenuScene(self.settings,switch_scene_callback=self.switch_scene)
        self.settings_scene = SettingsScene(self.settings,switch_scene_callback=self.switch_scene,
                                            save_settings_callback=self.save_settings_callback)
        self.statitics_scene = StatisticsScene()
        self.level_selection = LevelSelectionScene(self.settings,switch_scene_callback=self.switch_scene)
        self.game_play_scene = GamePlayScene(self.settings,self.graphics_loader.graphics,switch_scene_callback = self.switch_scene)

if __name__ =='__main__':
    game = Game()
    game.run()