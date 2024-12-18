from utilities import *
from player import Player
from gun_player import Player_Gun
from gun_enemy import Enemy_Gun
from level import Level
from enemy import Enemy


class Galaga:
    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('GALAGA')
        self.clock = pygame.time.Clock()

        current_stage = Level()

        self.player = Player()
        self.player_gun = Player_Gun()

        self.enemy = Enemy()
        self.enemy_gun = Enemy_Gun()

    def run(self):

        while True:
            dt = self.clock.tick() / 1000
            self.display.fill((0, 0, 0))

            self.player.move(self.display, dt)
            self.player.input()

            self.player_gun.shoot([self.player.pos[0] + (rect_size // 2), self.player.pos[1]], self.display, dt)
            self.player_gun.input()

            self.enemy.move(self.display, dt)
            self.enemy.update()

            self.enemy_gun.shoot([self.enemy.pos[0] + (rect_size // 2), self.enemy.pos[1]], self.display, dt)
            #self.enemy_gun.input()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


if __name__ == '__main__':
    game = Galaga()
    game.run()
