from utilities import *
from player import Player
from gun_player import Player_Gun
from level import Level


class Galaga:
    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('GALAGA')
        self.clock = pygame.time.Clock()

        current_stage = Level()

        self.player = Player()
        self.player_gun = Player_Gun()

    def run(self):

        while True:
            dt = self.clock.tick() / 1000
            self.display.fill((0, 0, 0))

            self.player.move(self.display, dt)
            self.player.input()

            self.player_gun.shoot([self.player.pos[0] + (rect_size // 2), rect_y], self.display, dt)
            self.player_gun.input()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


if __name__ == '__main__':
    game = Galaga()
    game.run()
