from settings import pg
from sprites.graphic import Graphic

class Player():
    def __init__(self,pos,sprites):
        self.frames = sprites
        print(sprites)
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

    def draw(self,screen):
        screen.blit(self.image,self.rect)

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
    
    def death(self):
        pass