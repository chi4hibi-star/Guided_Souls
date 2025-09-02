from settings import pg
from random import choice, uniform
from gameplay.enemy_water import EnemyWater
from gameplay.enemy_air import EnemyAir
from gameplay.enemy_earth import EnemyEarth
from gameplay.enemy_fire import EnemyFire

class EnemyController():
    def __init__(self,screen_size,level,gameplay_scene,player_speed):
        self.gameplay_scene = gameplay_scene
        spawn_width = 5*player_speed
        spawn_offset = player_speed

        self.spawn_top = [-spawn_offset,-spawn_width*5-spawn_offset,]
        
        self.enemy_selection = ["earth", "fire", "wind", "water"]
        enemy_level_distribution = [
            [100,0,0,0], #1
            [0,100,0,0], #2
            [0,0,100,0], #3
            [0,0,0,100], #4
            [0,50,50,0], #5
            [60,0,40,0], #6
            [50,0,0,50], #7
            [40,30,30,0], #8
            [0,40,30,30], #9
            [25,25,25,25], #10
        ]
        self.enemy_distribution = enemy_level_distribution[level]
        self.enemies = []

        self.timer = 0
        self.cd = 2000

    def update(self,time):
        time_interval = 30000 #5 min
        if time < time_interval:
            self.cd = 2000
        elif time < time_interval * 2:
            self.cd = 1800
        elif time < time_interval * 3:
            self.cd = 1600
        elif time < time_interval * 4:
            self.cd = 1400
        elif time < time_interval * 5:
            self.cd = 1200
        elif time < time_interval * 6:
            self.cd = 1000

        if time - self.timer >= self.cd:
            self.timer = time
            #spawn enemy according to distribution
            pos_box = uniform([0,1,2,3])
            if pos_box == 0:
                pos = pg.math.Vector2(uniform(),uniform())
            elif pos_box == 1:
                pos = pg.math.Vector2(uniform(),uniform())
            elif pos_box == 2:
                pos = pg.math.Vector2(uniform(),uniform())
            else:
                pos = pg.math.Vector2(uniform(),uniform())

            selected_enemy = choice(self.enemy_selection,weights=self.enemy_distribution,k=1)
            if selected_enemy == "earth":
                self.enemies.append(EnemyEarth())