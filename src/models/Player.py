from pygame import sprite, Surface

from lib.constants import GREEN, HEIGHT, WIDTH


class Player(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0
