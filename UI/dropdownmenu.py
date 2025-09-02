import pygame as pg
from UI.label import Label

class DropdownMenu:
    def __init__(self,
                 pos=(0,0),
                 size = None,
                 options=[],
                 font=None,
                 fontsize=32,
                 selected_index=0,
                 color_inactive=(100,100,100),
                 color_active=(150,150,150),
                 text_color=(0,0,0),
                 background_color=(200,200,200)
                 ):
        self.font=font or pg.font.SysFont(None,fontsize)
        self.text = ""
        self.rendered_text = self.font.render(self.text,True,text_color)
        if size:
            self.rect = pg.Rect(pos,size)
        else:
            self.rect = self.rendered_text.get_rect()
        self.options = options
        self.color_inactive = color_inactive
        self.color_activ = color_active
        self.selected_index = selected_index
        self.text_color = text_color
        self.expanded = False
        self.option_rects = [pg.Rect(self.rect.x,self.rect.y+(i*2+1)*self.rect.height,self.rect.width,self.rect.height)
                             for i in range(len(options))]
        self.background_color = background_color
    
    def handle_events(self,events):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.expanded = not self.expanded
                elif self.expanded:
                    for i, option_rect in enumerate(self.option_rects):
                        if option_rect.collidepoint(event.pos):
                            self.selected_index = i
                            self.expanded = False
                            break
                else:
                    self.expanded = False
            
    def draw(self,surface):
        pg.draw.rect(surface,self.background_color,self.rect)
        self.text = str(self.options[self.selected_index])
        txt_surf = self.font.render(self.text, True,self.text_color)
        surface.blit(txt_surf, (self.rect.x + 5, self.rect.y + (self.rect.height-txt_surf.get_height())/2))

        triangle_pos = (self.rect.x+self.rect.width*0.9,self.rect.y+self.rect.height/2)

        tri_size = self.rect.height * 0.3

        if self.expanded:
            points = [(triangle_pos[0], triangle_pos[1] - tri_size),
                      (triangle_pos[0] - tri_size, triangle_pos[1] + tri_size),
                      (triangle_pos[0] + tri_size, triangle_pos[1] + tri_size)]
            for i,option in enumerate(self.options):
                option_rect = self.option_rects[i]
                pg.draw.rect(surface,self.color_inactive,option_rect)
                option_text = self.font.render(str(option),True,self.text_color)
                surface.blit(option_text,(option_rect.x+5,option_rect.y+(option_rect.height-option_text.get_height())/2))
        else:
            points = [(triangle_pos[0], triangle_pos[1] + tri_size),
                      (triangle_pos[0] - tri_size, triangle_pos[1] - tri_size),
                      (triangle_pos[0] + tri_size, triangle_pos[1] - tri_size)]
            
        pg.draw.polygon(surface,self.text_color,points)

    def update_label_pos(self):
        for i in range(len(self.options)):
            self.option_rects[i].topleft = (
                self.rect.x,
                self.rect.y + (i + 1) * self.rect.height - i
            )

    def update(self):
        pass