from settings import pg
from gameplay.graphic import Graphic

class EnemyElemental(Graphic):
    def __init__(self,pos,screen_width,type,size_divider):
        super().__init__(["sprites","enemies",*type],screen_width,size_divider)
        self.image = self.frames["basic"][0]
        self.rect = self.image.get_frect(center = pos)

        self.frame_index = 0

        self.can_attack = True
        self.attack_timer = 0
        self.attack_cd = 500
        self.is_dying = False

    def handle_events(self,events):
        pass

    def death(self):
        pass

    def draw(self,screen):
        screen.blit(self.image,self.rect)