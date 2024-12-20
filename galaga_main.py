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
        self.spaceship = pygame.image.load(os.path.join("Sprites", "player.png"))
        self.enemy1 = pygame.image.load(os.path.join("Sprites", "enemy1.png"))

        self.player = Player(self.spaceship)
        self.player_gun = Player_Gun()

        self.enemy = Enemy(self.enemy1)
        self.enemy_gun = Enemy_Gun()

    def run(self):

        while True:
            dt = self.clock.tick() / 1000

            self.display.fill((0, 0, 0))

            self.enemy.check_collision(self.display, self.player_gun.bolts, self.player_gun.dr_bolts, self.player_gun.dl_bolts)
            self.player.check_collision(self.display, self.enemy_gun.bolts, self.enemy_gun.dr_bolts, self.enemy_gun.dl_bolts)

            self.player.move(self.display, dt)
            self.player.input()

            self.player_gun.shoot([self.player.pos[0] + (rect_size // 2), self.player.pos[1]], self.display, dt)
            self.player_gun.input()

            self.enemy.move(self.display, dt)
            self.enemy.update()

            self.enemy_gun.shoot([self.enemy.pos[0] + (rect_size // 2), self.enemy.pos[1]], self.display, dt)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


if __name__ == '__main__':
    game = Galaga()
    game.run()
