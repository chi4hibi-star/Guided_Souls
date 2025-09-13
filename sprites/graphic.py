import pygame as pg
from os.path import join, basename
from os import walk

#move graphics load on game start and recall and override on resolutions settings change and save
#einmal laden immer nutzen, nicht für jede neue instanz neu berechnen.
class Graphic(pg.sprite.Sprite):
    def __init__(self,path,screen_width,single=False,size_divider=2):
        base_screen_width = 320
        scale = max(1,(screen_width // base_screen_width)-size_divider)

        base_path = join(*path)
        if single:
            self.image = self.pixel_scale(pg.image.load(join(base_path)),scale)
            self.rect = self.image.get_rect(center = (0,0))
        else:
            for folder_path,sub_folders,file_names in walk(base_path):
                if folder_path == base_path:
                    self.frames = {key: None for key in sub_folders}
                else:
                    state = basename(folder_path)
                    images = [pg.image.load(join(folder_path,f"{i}.png")).convert_alpha() for i in range(len(file_names))]
                    scaled_image = [self.pixel_scale(image,scale) for image in images]
                    self.frames[state] = scaled_image

    def pixel_scale(self,image,scale):
        image_width,image_height = image.get_size()
        new_image = pg.Surface((image_width * scale, image_height * scale), pg.SRCALPHA)
        for x in range(image_width):
                for y in range(image_height):
                    color = image.get_at((x, y))
                    for dx in range(scale):
                        for dy in range(scale):
                            new_image.set_at((x * scale + dx, y * scale + dy), color)
        return new_image
    
    def animate(self,dt,state,endless=True):
        if endless:
            self.frame_index += dt * 1.5
            self.image = self.frames[state][int(self.frame_index % len(self.frames[state]))]
        else:
            self.frame_index += dt * 1.5
            if self.frame_index < len(self.frames[state]):
                self.image = self.frames[state][int(self.frame_index)]
            else:
                self.death()