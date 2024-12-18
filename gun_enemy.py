from utilities import *
from bolts_enemy import Enemy_Bolt, Enemy_DR_Bolt, Enemy_DL_Bolt
from timer import Timer


class Enemy_Gun:
    def __init__(self):
        self.bolts = []
        self.dr_bolts = []
        self.dl_bolts = []
        self.shot = True
        self.level = 2

        self.timers = {
            'reload_timer': Timer(500)
        }

    def shoot(self, pos, display, dt):
        if self.shot and not self.timers['reload_timer'].active:
            self.bolts.append(Enemy_Bolt(pos))
            if self.level >= 2:
                self.dr_bolts.append(Enemy_DR_Bolt(pos))
                self.dl_bolts.append(Enemy_DL_Bolt(pos))
            self.timers['reload_timer'].activate()

        self.update_timers()

        if self.bolts:
            for bolt in self.bolts:
                bolt.move(display, dt)
            self.bolts = [bolt for bolt in self.bolts if bolt.pos[1] <= screen_height + 100]

        if self.dr_bolts:
            for bolt in self.dr_bolts:
                bolt.move(display, dt)
            self.dr_bolts = [bolt for bolt in self.dr_bolts if bolt.pos[1] <= screen_height + 100 and bolt.pos[0] <= screen_width + 100]

        if self.dl_bolts:
            for bolt in self.dl_bolts:
                bolt.move(display, dt)
            self.dl_bolts = [bolt for bolt in self.dl_bolts if bolt.pos[1] <= screen_height + 100 and bolt.pos[0] >= -100]

    def update_timers(self):
        for timer in self.timers.values():
            if timer.active:
                timer.update()
