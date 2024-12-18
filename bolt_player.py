from utilities import *


class Player_Bolt:
    def __init__(self, pos):
        self.pos = pos
        self.speed = 500

    def move(self, display, dt):
        self.pos[1] -= self.speed * dt

        pygame.draw.rect(display, (0, 255, 0), (self.pos[0], self.pos[1], 1, 20))


class Player_DR_Bolt:
    def __init__(self, pos):
        self.pos = [pos[0] + 5, pos[1] + 20]
        self.speed = 500

    def move(self, display, dt):
        self.pos[1] -= self.speed * dt
        self.pos[0] += .5 * self.speed * dt

        pygame.draw.line(display, (0, 255, 0), (self.pos[0] + 5, self.pos[1] - 15), (self.pos[0], self.pos[1]))


class Player_DL_Bolt:
    def __init__(self, pos):
        self.pos = [pos[0] - 5, pos[1] + 20]
        self.speed = 500

    def move(self, display, dt):
        self.pos[1] -= self.speed * dt
        self.pos[0] -= .5 * self.speed * dt

        pygame.draw.line(display, (0, 255, 0), (self.pos[0] - 5, self.pos[1] - 15), (self.pos[0], self.pos[1]))
