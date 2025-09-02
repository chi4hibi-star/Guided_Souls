import json
import pygame as pg
from os import walk
from os.path import join

class Settings():
    def __init__(self,save_settings_callback):
        self.save_settings_callback = save_settings_callback
        self.selected_level = -1
        self.load_settings()

    def save_settings(self,new_settings):
        new_settings = {
            "volume": new_settings[0],
            "resolution": new_settings[1],
            "controls": {
                "move_up": new_settings[2],
                "move_left": new_settings[3],
                "move_down": new_settings[4],
                "move_right": new_settings[5],
                "attack": new_settings[6]
            }
        }
        with open("settings.json", "w") as f:
            json.dump(new_settings, f, indent=4)
        self.load_settings()
        self.save_settings_callback()

    def load_settings(self):
        try: 
            with open("settings.json","r") as f:
                self.saved_settings = json.load(f)
        except FileNotFoundError:
            self.saved_settings = {
                "volume": 0.5,
                "resolution": [1280,960],
                "controls": {
                    "move_up": "w",
                    "move_left": "a",
                    "move_down": "s",
                    "move_right": "d",
                    "attack": "mouse_1"
                }
            }