import pygame as pg
from pygame.locals import *


class Soldier(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y, img_path, scale, _speed):
        pg.sprite.Sprite.__init__(self)
        img = pg.image.load(img_path)
        self.speed = _speed
        self.image = pg.transform.scale(img, (int(img.get_width() * scale),
                                              int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

    def move(self, moving_left, moving_right):
        dx = dy = 0
        if moving_right:
            dx = self.speed
        if moving_left:
            # if speed <=0.5  left movement refuse to work , why ?
            # if speed <=0.4 left and right movements refuse to work , why ?
            dx = -self.speed

        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        screen.blit(self.image, self.rect)


# Initialization
pg.init()
screen = pg.display.set_mode((600, 400))
pg.display.set_caption("Platformer")
clock = pg.time.Clock()
FPS = 60

run = True
player = Soldier(pos_x=50, pos_y=50,
                 img_path="img/player/Idle/0.png", scale=2, _speed=0.6)

moving_left = moving_right = False
# Game loop
while run:

    clock.tick(FPS)
    screen.fill((255, 255, 255))  # draw_bg(BG)

    for event in pg.event.get():
        if event.type == QUIT:
            run = False
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
        elif event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False
    player.draw()
    player.move(moving_left, moving_right)
    pg.display.update()

pg.quit()
sys.exit()
