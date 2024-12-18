from utilities import *


class Player:
    def __init__(self):

        self.pos = [rect_x, rect_y]
        #self.rect = self.image.get_frect(topleft=pos)
        self.direction = vector()
        self.speed = 500

    def move(self, display, dt):

        self.pos[0] += self.direction.x * self.speed * dt

        pygame.draw.rect(display, (0, 0, 255), (self.pos[0], self.pos[1], rect_size, rect_size))

    def input(self):
        keys = pygame.key.get_pressed()
        input_vector = vector(0, 0)

        if keys[pygame.K_a]:
            if self.pos[0] > 0:
                input_vector.x -= 1
        if keys[pygame.K_d]:
            if self.pos[0] + 30 < 800:
                input_vector.x += 1

        self.direction.x = input_vector.normalize().x if input_vector else input_vector.x
