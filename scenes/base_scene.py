class BaseScene:
    def __init__(self):
        self.next_scene = None
    
    def handle_events(self,events):
        raise NotImplementedError
    
    def update(self):
        raise NotImplementedError
    
    def draw(self):
        raise NotImplementedError