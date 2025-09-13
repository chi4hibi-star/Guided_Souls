import pygame as pg
from os.path import join, basename, relpath
from os import walk, sep

class Graphics_Loader():
    def __init__(self, base_path="sprites"):
        self.graphics = {}
        for folder, _, files in walk(base_path):
            rel_path = relpath(folder, base_path)
            parts = [] if rel_path == "." else rel_path.split(sep)

            current = self.graphics
            for p in parts[:-1]:
                current = current.setdefault(p, {})
            
            if parts:  # wenn Unterordner existiert
                last_part = parts[-1]
                png_files = sorted(f for f in files if f.lower().endswith(".png"))
                if png_files:
                    current[last_part] = [pg.image.load(join(folder, f)).convert_alpha() for f in png_files]
                else:
                    current.setdefault(last_part, {})
            else:  # base_path selbst
                png_files = sorted(f for f in files if f.lower().endswith(".png"))
                if png_files:
                    self.graphics = [pg.image.load(join(folder, f)).convert_alpha() for f in png_files]


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
    
    def scale_all(self, resolution):
        scale = max(1,(resolution[0] // 320)-2)
        def recurse(directory):
            for index, sub_directory_or_item in directory.items():
                if isinstance(sub_directory_or_item, dict):
                    recurse(sub_directory_or_item)
                elif isinstance(sub_directory_or_item,pg.Surface):
                    directory[index] = self.pixel_scale(sub_directory_or_item, scale)
        recurse(self.graphics)