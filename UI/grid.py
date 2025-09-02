import pygame as pg

class Grid:
    def __init__(self,
                 outer_rect = (100,100,300,300),
                 rows = 3,
                 cols = 3,
                 line_color = None):
        self.rect = pg.Rect(outer_rect)
        self.cols = cols
        self.rows = rows
        self.line_color = line_color
        self.cell_width = self.rect.width/self.cols
        self.cell_height = self.rect.height/self.rows
        
        self.objects = [[None for _ in range(cols)]for _ in range(rows)]

    def add_object(self,obj,row,col,align=None,rel_pos=None):
        if row<self.rows and col < self.cols:
            self.objects[row][col] = obj

        cell_x = self.rect.left + col * self.cell_width
        cell_y = self.rect.top + row * self.cell_height

        if rel_pos is not None:
            x = cell_x + rel_pos[0] * (self.cell_width - obj.rect.width)
            y = cell_y + rel_pos[1] * (self.cell_height - obj.rect.height)
        elif align == "center":
            x = cell_x + (self.cell_width - obj.rect.width) / 2
            y = cell_y + (self.cell_height - obj.rect.height) / 2
        elif align == "left":
            x = cell_x
            y = cell_y + (self.cell_height - obj.rect.height) / 2
        elif align == "right":
            x = cell_x + self.cell_width - obj.rect.width
            y = cell_y + (self.cell_height - obj.rect.height) / 2
        elif align =="bottom":
            x = cell_x + (self.cell_width - obj.rect.width) / 2
            y = cell_y + self.cell_height - obj.rect.height
        else:
            x,y = cell_x,cell_y

        obj.rect.topleft = (x,y)


    def draw(self,surface):
        if self.line_color:
            for c in range(self.cols + 1):
                x = self.rect.left + c * self.cell_width
                pg.draw.line(surface,self.line_color,(x,self.rect.top),(x,self.rect.bottom))
            for r in range(self.rows + 1):
                y = self.rect.top + r * self.cell_height
                pg.draw.line(surface,self.line_color,(self.rect.left,y),(self.rect.right,y))

        for r in range(self.rows):
            for c in range(self.cols):
                obj = self.objects[r][c]
                if obj:
                    obj.draw(surface)

    def update(self):
        for row in self.objects:
            for obj in row:
                if obj:
                    obj.update()

    def handle_events(self,events):
        for row in self.objects:
            for obj in row:
                if obj:
                    obj.handle_events(events)
            