from settings import pg

class Slider:
    def __init__(self,
                 pos = (0,0),
                 size = None,
                 min_val=0,
                 max_val=1,
                 start_val=None,
                 color=(0,200,0)):
        
        if size is None:
            size = (100,20)
        self.rect = pg.Rect(pos,size)
        self.min_val = min_val
        self.max_val = max_val
        self.color = color

        if start_val is None:
            self.value = (min_val + max_val) / 2
        else:
            self.value = max(min_val,min(max_val,start_val))

        self.handle_width = 10
        self.dragging = False

    def handle_events(self, events):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.get_handle_rect().collidepoint(event.pos):
                    self.dragging = True
            elif event.type == pg.MOUSEBUTTONUP:
                self.dragging = False
            elif event.type == pg.MOUSEMOTION and self.dragging:
                self.update_value_from_mouse(event.pos[0])

    def update_value_from_mouse(self, mouse_x):
        relative_x = max(self.rect.x, min(mouse_x,self.rect.x + self.rect.width))
        precent = (relative_x - self.rect.x) / self.rect.width
        self.value = self.min_val + precent * (self.max_val - self.min_val)

    def get_handle_rect(self):
        percent = (self.value - self.min_val) / (self.max_val - self.min_val)
        x = self.rect.x + percent * self.rect.width
        return pg.Rect(x-self.handle_width / 2, self.rect.y, self.handle_width, self.rect.height)
    
    def draw(self,surface):
        pg.draw.rect(surface,(100,100,100),self.rect)
        fill_rect = pg.Rect(self.rect.x,self.rect.y,
                             (self.value - self.min_val)/(self.max_val - self.min_val) * self.rect.width,
                             self.rect.height)
        pg.draw.rect(surface,self.color,fill_rect)
        pg.draw.rect(surface,(255,255,255),self.get_handle_rect())

    def get_value(self):
        return self.value
    
    def set_value(self,val):
        self.value = max(self.min_val,min(self.max_val,val))

    def update(self):
        pass
