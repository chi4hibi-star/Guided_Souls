import pygame as pg
from os.path import join, basename, relpath
from os import walk, sep

class Graphics_Loader():
    def __init__(self,base_path = "sprites"):
        self.graphics = {}
        for folder_path, _, file_names in walk(base_path):
            rel_path = relpath(folder_path,base_path)
            parts = [] if rel_path == "." else rel_path.split(sep)

            for p in parts:
                self.graphics = self.graphics.setdefault(p,{})

            for f in file_names:
                if f.lower().endswith(".png"):
                    file_path = join(folder_path,f)
                    self.graphics[f] = pg.image.load(file_path).convert_alpha()

    def pixel_scale(self,image,scale):
        image_width, image_height = image.get_size()
        new_image = pg.Surface((image_width * scale, image_height * scale), pg.SRCALPHA)
        for x in range(image_width):
            for y in range(image_height):
                color = image.get_at((x,y))
                for dx in range(scale):
                    for dy in range(scale):
                        new_image.set_at((x * scale + dx, y * scale + dy),color)
        return new_image
    
    def scale_all(self, scale):
        def recurse(d):
            for k, v in d.items():
                if isinstance(v, dict):
                    recurse(v)
                elif isinstance(v,pg.Surface):
                    d[k] = self.pixel_scale(v, scale)
        recurse(self.graphics)