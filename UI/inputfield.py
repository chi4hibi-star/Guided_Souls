import pygame as pg

class InputField:
    def __init__(self,
                 pos = (0,0),
                 size = None,
                 font = None,
                 fontsize = 32,
                 input_type ="all",
                 color_active=(200,200,200),
                 color_inactive=(100,100,100),
                 start_text = None,
                 text_color=(0,0,0),
                 linked_element=None
                 ):
        
        self.input_type = input_type
        self.color_active = color_active
        self.color_inactive = color_inactive
        self.text_color = text_color
        self.font = font or pg.font.SysFont(None,fontsize)
        self.text = start_text or ""
        self.rendered_text = self.font.render(self.text,True,self.text_color)
        if size:
            self.rect = pg.Rect(pos,size)
        else:
            self.rect = self.rendered_text.get_rect()
        self.active = False
        self.select_all_on_next_draw = False
        self.linked_element = linked_element

    def handle_events(self, events):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                was_active = self.active
                self.active = self.rect.collidepoint(event.pos)
                if self.active and not was_active:
                    self.await_key_input = self.input_type == "key"
                    self.select_all_on_next_draw = True
                    return

            if self.active and (event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN):
                if self.select_all_on_next_draw:
                    self.text = ""
                    self.select_all_on_next_draw = False

                if self.input_type == "key" and getattr(self, "await_key_input", False):
                    if event.type == pg.MOUSEBUTTONDOWN:
                        mouse_names = {1: "MOUSE_LEFT", 2: "MOUSE_MIDDLE", 3: "MOUSE_RIGHT"}
                        self.text = mouse_names.get(event.button, f"MOUSE_{event.button}")
                    elif event.type == pg.KEYDOWN:
                        self.text = pg.key.name(event.key)
                    self._update_linked_from_text()
                    self.active = False
                    self.await_key_input = False
                    return

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_BACKSPACE:
                        self.text = self.text[:-1]
                    elif event.key == pg.K_RETURN:
                        self._update_linked_from_text()
                    else:
                        char = event.unicode
                        if self.input_type == "numbers" and (char.isdigit() or char == "."):
                            self.text += char
                        elif self.input_type == "letters" and char.isalpha():
                            self.text += char
                        elif self.input_type == "all" and char.isalnum():
                            self.text += char




    def _update_linked_from_text(self):
        if self.linked_element:
            try:
                value = float(self.text) if self.input_type == "numbers" else self.text
                self.linked_element.set_value(value)
            except ValueError:
                pass

    
    def sync_from_linked(self):
        if self.linked_element:
            val = self.linked_element.get_value()
            if isinstance(val, float):
                self.text = f"{val:.2f}"
            else:
                self.text = str(val)

    def link_to(self,other):
        self.linked_element = other

    def draw(self,surface):
        if self.active:
            color = self.color_active
        else:
            color = self.color_inactive
        pg.draw.rect(surface,color,self.rect, border_radius=5)
        txt_surf = self.font.render(self.text, True,self.text_color)
        surface.blit(txt_surf, (self.rect.x + 5, self.rect.y + (self.rect.height-txt_surf.get_height())/2+2))

    def update(self):
        if not self.active:
          self.sync_from_linked()