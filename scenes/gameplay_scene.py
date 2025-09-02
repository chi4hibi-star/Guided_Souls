from scenes.base_scene import BaseScene
from settings import pg
from gameplay.player import Player
from gameplay.enemy_controller import EnemyController
from gameplay.ground import Ground

class GamePlayScene(BaseScene):
    def __init__(self,settings,switch_scene_callback):
        self.settings = settings
        self.switch_scene_backback = switch_scene_callback

        window_width, window_height = self.settings.saved_settings["resolution"]
        self.clock = pg.time.Clock()
        self.dt = self.clock.tick(50) / 1000.0

        self.player = Player(pos=(window_width/2, window_height/2),screen_width=window_width)
        #self.enemy_controller = EnemyController(pos=(window_width/2,window_height/2),screen_width=window_width)
        self.ground = Ground((window_width,window_height))

        self.player_direction = pg.math.Vector2()
        self.player_speed = 80
        self.move = False

    def handle_events(self, events):
        keys = pg.key.get_pressed()
        self.player_direction.x = (int(keys[pg.key.key_code(self.settings.saved_settings["controls"]["move_right"])])
                             - int(keys[pg.key.key_code(self.settings.saved_settings["controls"]["move_left"])]))
        self.player_direction.y = (int(keys[pg.key.key_code(self.settings.saved_settings["controls"]["move_down"])])
                             - int(keys[pg.key.key_code(self.settings.saved_settings["controls"]["move_up"])]))
        self.player_direction = self.player_direction.normalize() if self.player_direction else self.player_direction

    def update(self):
        print(self.dt)
        self.player.update(self.dt,self.player_direction)
        self.ground.update(self.dt,self.player_direction*self.player_speed)
        #self.enemies.update()
        #self.objects.update()
    
    def draw(self,screen):
        screen.fill((30,30,30))
        self.ground.draw(screen)
        #self.enemy_water.draw(screen)
        self.player.draw(screen)