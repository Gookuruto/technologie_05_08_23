import pygame

from configuration import *
from pygame_classes.spritesheet import SpriteSheet
from sprites import *


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.terrain_sheet = SpriteSheet('img/images/terrain.png')
        self.player_sheet = SpriteSheet('img/images/cats.png')

        self.running = True
        self.block_collided = False

        self.create_tile_map()


    def create_tile_map(self):
        for i,row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self,j,i)
                if column == 'P':
                    self.player = Player(self,j,i)
                if column == "B":
                    Block(self,j,i)

    def update(self):
        self.all_sprites.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)

        pygame.display.update()

    def main(self):
        while self.running:
            self.events()
            self.update()
            self.draw()


if __name__ == "__main__":
    g = Game()
    g.main()
