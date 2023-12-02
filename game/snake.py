import time

import pygame

pygame.init()
dis_width = 400
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.update()
pygame.display.set_caption("Snake from Edureka")
game_over = False
blue = (0, 0, 255)
red = (255, 0, 0)
x = dis_width / 2
y = dis_height / 2
x_change = 0
y_change = 0
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -10
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = 10
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = -10
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = 10
    if x >= dis_width or x < 0 or y >= dis_height or y < 0:
        if x >= dis_width:
            x = 0
        if x < 0:
            x = dis_width
        if y >= dis_height:
            y = 0
        if y < 0:
            y = dis_height
    x += x_change
    y += y_change
    dis.fill((255, 255, 255))
    pygame.draw.rect(dis, blue, [x, y, 10, 10])
    pygame.display.update()
    clock.tick(60)

font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 2, dis_height / 2])


message("You lost", red)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()
