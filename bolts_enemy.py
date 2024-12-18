from utilities import *


class Enemy_Bolt:
    def __init__(self, pos):
        self.pos = [pos[0], pos[1] + rect_size // 2]

    def move(self, display, dt):
        self.pos[1] += player_bolt_speed * dt

        pygame.draw.rect(display, (0, 255, 0), (self.pos[0], self.pos[1], bullet_width, 20))


class Enemy_DR_Bolt:
    def __init__(self, pos):
        self.pos = [pos[0] + 5, pos[1] + rect_size]

    def move(self, display, dt):
        self.pos[1] += player_bolt_speed * dt
        self.pos[0] += .5 * player_bolt_speed * dt

        pygame.draw.line(display, (0, 255, 0), (self.pos[0] + 5, self.pos[1] - 15), (self.pos[0] + 10, self.pos[1]), bullet_width)


class Enemy_DL_Bolt:
    def __init__(self, pos):
        self.pos = [pos[0] - 5, pos[1] + rect_size]

    def move(self, display, dt):
        self.pos[1] += player_bolt_speed * dt
        self.pos[0] -= .5 * player_bolt_speed * dt

        pygame.draw.line(display, (0, 255, 0), (self.pos[0] - 5, self.pos[1] - 15), (self.pos[0] - 10, self.pos[1]), bullet_width)
