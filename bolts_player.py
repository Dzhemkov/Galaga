from utilities import *


class Player_Bolt:
    def __init__(self, pos):
        self.pos = [pos[0], pos[1]]

        self.rect = pygame.Rect(self.pos[0], self.pos[1], bullet_width, 20)

        #self.bolt1 = pygame.image.load(os.path.join("Sprites", "bolt1.png"))

    def move(self, display, dt):
        self.pos[1] -= player_bolt_speed * dt

        self.rect = pygame.Rect(self.pos[0], self.pos[1], bullet_width, 20)

        pygame.draw.rect(display, (0, 255, 0), (self.pos[0], self.pos[1], bullet_width, 20))
        #display.blit(self.bolt1, (self.pos[0], self.pos[1]))


class Player_DR_Bolt:
    def __init__(self, pos):
        self.pos = [pos[0] + 5, pos[1] + rect_size // 2]

        self.rect = pygame.Rect(self.pos[0], self.pos[1], 10, 20)


    def move(self, display, dt):
        self.pos[1] -= player_bolt_speed * dt
        self.pos[0] += .5 * player_bolt_speed * dt

        self.rect = pygame.Rect(self.pos[0], self.pos[1], 10, 20)

        pygame.draw.line(display, (0, 255, 0), (self.pos[0] + 5, self.pos[1] - 15), (self.pos[0], self.pos[1]), bullet_width)


class Player_DL_Bolt:
    def __init__(self, pos):
        self.pos = [pos[0] - 5, pos[1] + rect_size // 2]

        self.rect = pygame.Rect(self.pos[0], self.pos[1], 10, 20)

        #self.bolt1dl = pygame.image.load(os.path.join("Sprites", "bolt1dl.png"))

    def move(self, display, dt):
        self.pos[1] -= player_bolt_speed * dt
        self.pos[0] -= .5 * player_bolt_speed * dt

        self.rect = pygame.Rect(self.pos[0], self.pos[1], 10, 20)

        pygame.draw.line(display, (0, 255, 0), (self.pos[0] - 5, self.pos[1] - 15), (self.pos[0], self.pos[1]), bullet_width)
        #display.blit(self.bolt1dl, (self.pos[0], self.pos[1]))

