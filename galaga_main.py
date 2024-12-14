from utilities import *
from player import Player


class Galaga:
    def __init__(self):
        pygame.init()

        screen_width = 800
        screen_height = 600

        self.display = pygame.display.set_mode((screen_width, screen_height))

        pygame.display.set_caption('GALAGA')
        self.clock = pygame.time.Clock()

        rect_width = 30
        rect_height = 30
        rect_x = screen_width // 2 - rect_width // 2
        rect_y = screen_height - (screen_height // 10)

        self.player = Player([rect_x, rect_y])

    def run(self):

        while True:
            dt = self.clock.tick() / 1000
            self.display.fill((0, 0, 0))

            self.player.move(self.display, dt)
            self.player.input()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


if __name__ == '__main__':
    game = Galaga()
    game.run()
