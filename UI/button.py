from settings import pg

class Button:
    def __init__(
            self,
            text='Button',
            pos=(0,0),
            size = None,
            font = None,
            fontsize = 32,
            callback = lambda:None,
            base_color = (70,70,200),
            hover_color =(100,100,240),
            text_color = (180,180,180),
            pressed_text_color = (255,255,255)
            ):
        self.text = text
        self.text_color = text_color
        self.font = font or pg.font.SysFont(None,fontsize)
        self.rendered_text = self.font.render(self.text,True,self.text_color)
        if size:
            self.rect = pg.Rect(pos,size)
        else:
            self.rect = self.rendered_text.get_rect()
        self.callback = callback
        self.base_color = base_color
        self.hover_color = hover_color
        self.pressed_text_color = pressed_text_color
        self.is_pressed = False

    def draw(self,screen,pos=None):
        if pos:
            self.rect.topleft = pos
        mouse_pos = pg.mouse.get_pos()
        hovering = self.rect.collidepoint(mouse_pos)
        if hovering:
            color = self.hover_color
        else:
            color = self.base_color
        if hovering and self.is_pressed:
            text_color = self.pressed_text_color
        else:
            text_color = self.text_color
        pg.draw.rect(screen,color,self.rect,border_radius=10)

        text_surf = self.font.render(self.text,True,text_color)
        text_rect = text_surf.get_rect(center = self.rect.center)
        screen.blit(text_surf,(
                self.rect.x + (self.rect.width - text_rect.width) / 2,
                self.rect.y + (self.rect.height - text_rect.height) / 2))

    def handle_events(self,event):
        for event in event:
            if event.type == pg.MOUSEBUTTONDOWN:
                self.is_pressed = self.rect.collidepoint(event.pos)
            if event.type == pg.MOUSEBUTTONUP:
                if self.is_pressed and self.rect.collidepoint(event.pos):
                    self.callback()
                self.is_pressed = False

    def update(self):
        pass