from utilities import *


class Enemy:
    def __init__(self, image):
        self.image = image
        self.pos = [e_pos_x, e_pos_y]
        self.rect = self.image.get_frect(topleft=self.pos)
        self.direction = vector()
        self.speed = 200

        self.move_right = True
        self.move_left = False

    def move(self, display, dt):
        self.pos[0] += self.direction.x * self.speed * dt

        self.rect = self.image.get_frect(topleft=self.pos)

        #pygame.draw.rect(display, (255, 0, 0), (self.pos[0], self.pos[1], rect_size, rect_size))
        display.blit(self.image, (self.pos[0], self.pos[1]))

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

    def check_collision(self, display, bolts, dr_bolts, dl_bolts):

        bolts = bolts + dr_bolts + dl_bolts

        for bolt in bolts:
            if bolt.rect.colliderect(self.rect):
                display.fill((0, 255, 0))
