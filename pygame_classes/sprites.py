import math

import pygame
from configuration import *


class Player(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites

        super().__init__(self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE

        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.animationCounter = 1

        self.image = self.game.player_sheet.get_image(0, 0, 32, 32)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.direction = "right"

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT]:
            self.x_change -= PLAYER_STEPS
            self.direction = "left"
        if pressed_keys[pygame.K_RIGHT]:
            self.x_change += PLAYER_STEPS
            self.direction = "right"
        if pressed_keys[pygame.K_UP]:
            self.y_change -= PLAYER_STEPS
            self.direction = 'up'
        if pressed_keys[pygame.K_DOWN]:
            self.y_change += PLAYER_STEPS
            self.direction = 'down'

    def update(self) -> None:
        self.move()
        self.animiation()
        self.collide_blocks()
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        self.x_change = 0
        self.y_change = 0

    def collide_blocks(self):
        collideBlock = pygame.sprite.spritecollide(self, self.game.blocks, False)

        if collideBlock:
            if self.y_change != 0:
                self.y_change *= -1
            if self.x_change != 0:
                self.x_change *= -1

    def animiation(self):
        down_animation = [self.game.player_sheet.get_image(0, 0, self.width, self.height),
                          self.game.player_sheet.get_image(32, 0, self.width, self.height),
                          self.game.player_sheet.get_image(64, 0, self.width, self.height)
                          ]
        left_animation = [self.game.player_sheet.get_image(0, 32, self.width, self.height),
                          self.game.player_sheet.get_image(32, 32, self.width, self.height),
                          self.game.player_sheet.get_image(64, 32, self.width, self.height)
                          ]

        right_animation = [self.game.player_sheet.get_image(0, 64, self.width, self.height),
                           self.game.player_sheet.get_image(32, 64, self.width, self.height),
                           self.game.player_sheet.get_image(64, 64, self.width, self.height)
                           ]

        up_animation = [self.game.player_sheet.get_image(0, 96, self.width, self.height),
                        self.game.player_sheet.get_image(32, 96, self.width, self.height),
                        self.game.player_sheet.get_image(64, 96, self.width, self.height)
                        ]
        if self.direction == "down":
            if self.y_change == 0:
                self.image = down_animation[0]
            else:
                self.image = down_animation[math.floor(self.animationCounter)]
                self.animationCounter += 0.2
                if self.animationCounter >= 3:
                    self.animationCounter = 0

        if self.direction == "up":
            if self.y_change == 0:
                self.image = up_animation[0]
            else:
                self.image = up_animation[math.floor(self.animationCounter)]
                self.animationCounter += 0.2
                if self.animationCounter >= 3:
                    self.animationCounter = 0

        if self.direction == "right":
            if self.y_change == 0:
                self.image = right_animation[0]
            else:
                self.image = right_animation[math.floor(self.animationCounter)]
                self.animationCounter += 0.2
                if self.animationCounter >= 3:
                    self.animationCounter = 0

        if self.direction == "left":
            if self.y_change == 0:
                self.image = left_animation[0]
            else:
                self.image = left_animation[math.floor(self.animationCounter)]
                self.animationCounter += 0.2
                if self.animationCounter >= 3:
                    self.animationCounter = 0


class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE

        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_sheet.get_image(447, 353, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCKS_LAYER
        self.groups = self.game.all_sprites, self.game.blocks

        super(Block, self).__init__(self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE

        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_sheet.get_image(991, 541, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

# class Milk(pygame.sprite.Sprite):
#     def __init__(self, game, x, y):
#         self.game = game
#         self._layer = GROUND_LAYER
#         self.groups = self.game.all_sprites
#         pygame.sprite.Sprite.__init__(self, self.groups)
#
#         self.x = x * TILESIZE
#         self.y = y * TILESIZE
#
#         self.width = TILESIZE
#         self.height = TILESIZE
#
#         self.image = self.game.terrain_sheet.get_image(580, 420, self.width, self.height)
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y
