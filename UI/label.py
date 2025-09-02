import pygame as pg

class Label:
    def __init__(self,
                 pos=(0,0),
                 size = None,
                 font=None,
                 fontsize=32,
                 text="",
                 text_color=(255,255,255),
                 text_style = None,
                 background_color = None
                 ):
        self.text = text
        self.font = font or pg.font.SysFont(None,fontsize)
        self.fontsize = fontsize
        self.text_color = text_color
        if text_style == "bold":
            self.font.set_bold(True)
        elif text_style == "italic":
            self.font.set_italic(True)
        elif text_style =="strikethrough":
            self.font.set_strikethrough(True)
        elif text_style == "underline":
            self.font.set_underline(True)
        self.rendered_text = self.font.render(self.text,True,self.text_color)
        if size:
            self.rect = pg.FRect(pos,size)
        else:
            self.rect = self.rendered_text.get_rect()
        self.background_color = background_color

    def set_text(self,new_text):
        self.text = new_text
        self.rendered_text = self.font.render(self.text,True,self.text_color)

    def draw(self, surface,pos=None):
        if pos:
            self.rect.topleft = pos

        if self.background_color is not None:
            text_rect = self.rendered_text.get_rect()
            pg.draw.rect(surface, self.background_color, self.rect,border_radius=10)
            surface.blit(self.rendered_text, (
                self.rect.x + (self.rect.width - text_rect.width) / 2,
                self.rect.y + (self.rect.height - text_rect.height) / 2
            ))
        else:
            surface.blit(self.rendered_text, self.rect.topleft)


    def update(self):
        pass

    def handle_events(self,events):
        pass