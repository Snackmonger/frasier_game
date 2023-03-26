import pygame
import os
import sys
import spritesheet

# Pygame tutorial from youtube channel "Coding with Russ"
# Learn how to extract sprites from a sheet, rather than
# loading the frames as individual images. 

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Spritesheet Lesson")


sprite_sheet_image = pygame.image.load(os.path.join("Assets", "doux.png")).convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)


BACKGROUND = (50, 50, 50)
BLACK = (0,0,0)

def get_image(sheet, frame, width, height, scale, colour):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0,0), ((frame*width),0, width, height))
    # Blit the spritesheet, but only the frame specified by the frame
    # width multiplier.
    image=pygame.transform.scale(image, (width * scale, height*scale))
    # Note that scaling requires us to specify the target pixels to scale to,
    # so we added a scale to the function attributes, and multiply the sprite
    # height and width by the scale.
    image.set_colorkey(colour)
    # set_colorkey() allows us to define which colour serves as transparent when
    # placed on the screen.
    return image

frame_0 = sprite_sheet.get_image(0, 24, 24, 3, BLACK)
frame_1 = sprite_sheet.get_image(1, 24, 24, 3, BLACK)
frame_2 = sprite_sheet.get_image(2, 24, 24, 3, BLACK)

run = True
while run:

    SCREEN.fill(BACKGROUND)

    # Display frame image
    SCREEN.blit(frame_0, (0,0))
    SCREEN.blit(frame_1, (100,0))
    SCREEN.blit(frame_2, (270, 0))

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()