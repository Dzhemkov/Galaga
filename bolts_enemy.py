from utilities import *


class Enemy_Bolt:
    def __init__(self, pos):
        self.pos = [pos[0], pos[1] + rect_size // 2]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], bullet_width, 20)

    def move(self, display, dt):
        self.pos[1] += enemy_bolt_speed * dt

        self.rect = pygame.Rect(self.pos[0], self.pos[1], bullet_width, 20)

        pygame.draw.rect(display, (255, 0, 255), (self.pos[0], self.pos[1], bullet_width, 20))


class Enemy_DR_Bolt:
    def __init__(self, pos):
        self.pos = [pos[0] + 5, pos[1] + rect_size]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 10, 20)

    def move(self, display, dt):
        self.pos[1] += enemy_bolt_speed * dt
        self.pos[0] += .5 * enemy_bolt_speed * dt

        self.rect = pygame.Rect(self.pos[0], self.pos[1], 10, 20)

        pygame.draw.line(display, (255, 0, 255), (self.pos[0] + 5, self.pos[1] - 15), (self.pos[0] + 10, self.pos[1]), bullet_width)


class Enemy_DL_Bolt:
    def __init__(self, pos):
        self.pos = [pos[0] - 5, pos[1] + rect_size]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 10, 20)

    def move(self, display, dt):
        self.pos[1] += enemy_bolt_speed * dt
        self.pos[0] -= .5 * enemy_bolt_speed * dt

        self.rect = pygame.Rect(self.pos[0], self.pos[1], 10, 20)

        pygame.draw.line(display, (255, 0, 255), (self.pos[0] - 5, self.pos[1] - 15), (self.pos[0] - 10, self.pos[1]), bullet_width)
