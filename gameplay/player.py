from settings import pg
from gameplay.graphic import Graphic

class Player(Graphic):
    def __init__(self,pos,screen_width):
        super().__init__(["sprites","charon"],screen_width,size_divider=1)
        self.image = self.frames["front"][0]
        self.rect = self.image.get_rect(center = pos)

        self.frame_index = 0

        self.can_attack = True
        self.attack_timer = 0
        self.attack_cd = 2000

    def handle_events(self,events):
        pass

    def update(self,dt,direction):
        self.hitbox = pg.mask.from_surface(self.image)
        if direction.y > 0.7:
            self.animate(dt,"front")
        elif direction.y < -0.7:
            self.animate(dt,"back")
        elif direction.x > 0.7:
            self.animate(dt,"right")
        elif direction.x < -0.7:
            self.animate(dt,"left")
        else:
            self.image = self.frames["front"][0]

    def death(self):
        pass

    def draw(self,screen):
        screen.blit(self.image,self.rect)