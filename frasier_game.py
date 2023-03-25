import pygame
import os 
import sys

pygame.font.init()
pygame.display.set_caption("Crane Boys Mystery")

WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

TILE_SIZE = 50, 50
PLAYER_VELOCITY = 5
FPS = 60

# FRASIER_FONT = pygame.font.SysFont("korinna", 40)
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'frasier_test_bg.png')), (WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (153, 0, 153)
ORANGE = (255, 128, 0)

PLAYER_WIDTH, PLAYER_HEIGHT = 50, 150
player = pygame.Rect(700, 300, PLAYER_WIDTH, PLAYER_HEIGHT)
PLAYER_IMAGE = pygame.image.load(os.path.join('Assets', 'frasier_crane.png'))
PLAYER = pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))





clock = pygame.time.Clock()

def main_loop():
    clock.tick(FPS)

    for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit        

    keys_pressed = pygame.key.get_pressed()
    player_handle_movement(keys_pressed, player)

    draw_window(player)



def player_handle_movement(keys_pressed, player):
    if keys_pressed[pygame.K_LEFT] and player.x - PLAYER_VELOCITY > 0:  # LEFT
        player.x -= PLAYER_VELOCITY
    if keys_pressed[pygame.K_RIGHT] and player.x + PLAYER_VELOCITY + player.width < WIDTH:  # RIGHT
        player.x += PLAYER_VELOCITY
    if keys_pressed[pygame.K_DOWN] and player.y + PLAYER_VELOCITY + player.height < HEIGHT - 15:  # DOWN
        player.y += PLAYER_VELOCITY
    if keys_pressed[pygame.K_UP] and player.y + PLAYER_VELOCITY > 10:  # UP
        player.y -= PLAYER_VELOCITY



def draw_window(player):
    WINDOW.blit(BACKGROUND, (0, 0))
    WINDOW.blit(PLAYER, (player.x, player.y))
    pygame.display.update()
