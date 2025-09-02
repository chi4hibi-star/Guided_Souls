from settings import pg
from gameplay.graphic import Graphic

class souls(Graphic):
    def __init__(self, screen_width):
        super().__init__(["sprites","souls"],screen_width,size_divider=2)