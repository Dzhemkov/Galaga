from utilities import *
from player import Player
from gun_player import Player_Gun


class Galaga:
    def __init__(self):
        pygame.init()

        screen_width = 800
        screen_height = 600

        self.display = pygame.display.set_mode((screen_width, screen_height))

        pygame.display.set_caption('GALAGA')
        self.clock = pygame.time.Clock()

        self.rect_size = 30
        self.rect_x = screen_width // 2 - self.rect_size // 2
        self.rect_y = screen_height - (screen_height // 10)

        self.player = Player([self.rect_x, self.rect_y])
        self.player_gun = Player_Gun()

    def run(self):

        while True:
            dt = self.clock.tick() / 1000
            self.display.fill((0, 0, 0))

            self.player.move(self.display, dt)
            self.player.input()

            self.player_gun.shoot([self.player.pos[0] + (self.rect_size // 2), self.rect_y - self.rect_size], self.display, dt)
            self.player_gun.input()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


if __name__ == '__main__':
    game = Galaga()
    game.run()
