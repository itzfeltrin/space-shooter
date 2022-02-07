import pygame
import os

# from models.Player import Player
from lib.constants import BLACK, BLUE, FPS, GREEN, HEIGHT, RED, WIDTH
from models.Mob import Mob
from models.Player import Player


# initialize pygame and create window
pygame.init()
pygame.mixer.init()  # for sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# set up asset folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'assets')
player_img = pygame.image.load(
    os.path.join(img_folder, 'p1_jump.png')).convert()


all_sprites = pygame.sprite.Group()
player = Player()
mobs = pygame.sprite.Group()
all_sprites.add(player)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

# Game Loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)

    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Render (draw)
    screen.fill(BLUE)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
