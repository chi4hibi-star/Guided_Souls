from settings import pg
from gameplay.enemy import EnemyElemental

class EnemyWater(EnemyElemental):
    def __init__(self,pos,screen_width):
        super().__init__(pos, screen_width, "water", 2)
        self.speed = 90

#bewegung fehlt
    def update(self,dt,direction):
        self.hitbox = pg.mask.from_surface(self.image)
        if self.is_dying is False:
            self.animate(dt,"basic")
        else:
            self.animate(dt,"decay",False)