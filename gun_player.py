from utilities import *
from bolt_player import Player_Bolt, Player_DR_Bolt, Player_DL_Bolt
from timer import Timer


class Player_Gun:
    def __init__(self):
        self.bolts = []
        self.dr_bolts = []
        self.dl_bolts = []
        self.shot = False

        self.timers = {
            'reload_timer': Timer(100)
        }

    def shoot(self, pos, display, dt):
        if self.shot and not self.timers['reload_timer'].active:
            self.bolts.append(Player_Bolt(pos))
            self.dr_bolts.append(Player_DR_Bolt(pos))
            self.dl_bolts.append(Player_DL_Bolt(pos))
            self.timers['reload_timer'].activate()

        self.update_timers()

        if self.bolts:
            for bolt in self.bolts:
                bolt.move(display, dt)
            self.bolts = [bolt for bolt in self.bolts if bolt.pos[1] >= -100]

        if self.dr_bolts:
            for bolt in self.dr_bolts:
                bolt.move(display, dt)
            self.dr_bolts = [bolt for bolt in self.dr_bolts if bolt.pos[1] >= -100 and bolt.pos[0] <= screen_width + 100]

        if self.dl_bolts:
            for bolt in self.dl_bolts:
                bolt.move(display, dt)
            self.dl_bolts = [bolt for bolt in self.dl_bolts if bolt.pos[1] >= -100 and bolt.pos[0] >= -100]

    def input(self):
        keys = pygame.key.get_pressed()
        self.shot = keys[pygame.K_SPACE]

    def update_timers(self):
        for timer in self.timers.values():
            if timer.active:
                timer.update()
