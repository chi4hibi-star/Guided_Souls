#from settings import pg
from sprites.graphic import Graphic

class Ground(Graphic):
    def __init__(self,screen_size):
        self.screen_width,self.screen_height = screen_size
        super().__init__(["sprites","ground","2.png"],self.screen_width,single=True,size_divider=5)

        self.image_width,self.image_height = self.image.get_size()
        tiles_x = int(self.screen_width/self.image_width)+2
        tiles_y = int(self.screen_height/self.image_height)+2
        offset_x = -(tiles_x * self.image_width - self.screen_width) // 2
        offset_y = -(tiles_y * self.image_height - self.screen_height) // 2

        self.grounds_pos = [[(offset_x + ix * self.image_width, offset_y + iy * self.image_height) 
                             for iy in range(tiles_y)] for ix in range(tiles_x)]


    def handle_events(self,events):
        pass

    def update(self,dt,movement):
        delta = (-movement.x * dt, -movement.y * dt)
        for col_index, col in enumerate(self.grounds_pos):
            for row_index, (x, y) in enumerate(col):
                new_x = x + delta[0]
                new_y = y + delta[1]
                
                if new_x < -self.image_width * 1.1:
                    new_x += self.image_width * len(self.grounds_pos)
                elif new_x > self.screen_width + self.image_width * 0.1:
                    new_x -= self.image_width * len(self.grounds_pos)
                if new_y < -self.image_height * 1.1:
                    new_y += self.image_height * len(self.grounds_pos[0])
                elif new_y > self.screen_height + self.image_height * 0.1:
                    new_y -= self.image_height * len(self.grounds_pos[0])
                self.grounds_pos[col_index][row_index] = (new_x, new_y)

    def draw(self,screen):
        for col in self.grounds_pos:
            for pos in col:
                screen.blit(self.image,pos)
