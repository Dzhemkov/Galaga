from utilities import *
from bolt_player import Player_Bolt
from timer import Timer

class Player_Gun:
    def __init__(self):
        self.bolts = []
        self.shot = False

        self.timers = {
            'reload_timer': Timer(100)
        }

    def shoot(self, pos, display, dt):
        if self.shot and not self.timers['reload_timer'].active:
            self.bolts.append(Player_Bolt(pos))
            self.timers['reload_timer'].activate()
            self.shot = False

        self.update_timers()

        if self.bolts:
            for bolt in self.bolts:
                bolt.move(display, dt)
            self.bolts = [bolt for bolt in self.bolts if bolt.pos[1] >= -100]

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.shot = True

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()
