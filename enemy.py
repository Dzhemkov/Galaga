from utilities import *


class Enemy:
    def __init__(self):
        self.pos = [e_pos_x, e_pos_y]
        # self.rect = self.image.get_frect(topleft=pos)
        self.direction = vector()
        self.speed = 200

        self.move_right = True
        self.move_left = False


    def move(self, display, dt):
        self.pos[0] += self.direction.x * self.speed * dt

        pygame.draw.rect(display, (255, 0, 0), (self.pos[0], self.pos[1], rect_size, rect_size))


    def update(self):
        input_vector = vector(0, 0)

        if self.move_right and self.pos[0] + rect_size < 800 - rect_size:
            input_vector.x += 1
        else:
            self.move_right = False
            self.move_left = True

        if self.move_left and self.pos[0] > rect_size:
            input_vector.x -= 1
        else:
            self.move_right = True
            self.move_left = False

        self.direction.x = input_vector.normalize().x if input_vector else input_vector.x