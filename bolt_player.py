from utilities import *

class Player_Bolt:
    def __init__(self, pos):

        self.pos = pos

        self.speed = 500

    def move(self, display, dt):

        self.pos[1] -= self.speed * dt
        pygame.draw.rect(display, (255, 0, 0), (self.pos[0], self.pos[1], 2, 20))