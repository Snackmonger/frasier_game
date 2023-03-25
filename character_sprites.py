import pygame, os, sys

# Learning to animate sprites in pygame with 
# Clear Code Youtube Channel lesson

class CharacterSprite(pygame.sprite.Sprite):
    def __init__(self, SPRITE_X, SPRITE_Y) -> None:
        super().__init__()
        self.is_animating = False
        self.sprites = []
        # Create an array with the list of frames in the animation
        self.sprites.append(pygame.image.load(os.path.join('Assets', "attack_1.png")))
        self.sprites.append(pygame.image.load(os.path.join('Assets', "attack_2.png")))
        self.sprites.append(pygame.image.load(os.path.join('Assets', "attack_3.png")))
        self.sprites.append(pygame.image.load(os.path.join('Assets', "attack_4.png")))
        self.sprites.append(pygame.image.load(os.path.join('Assets', "attack_5.png")))
        self.sprites.append(pygame.image.load(os.path.join('Assets', "attack_6.png")))
        self.sprites.append(pygame.image.load(os.path.join('Assets', "attack_7.png")))
        self.sprites.append(pygame.image.load(os.path.join('Assets', "attack_8.png")))
        self.sprites.append(pygame.image.load(os.path.join('Assets', "attack_9.png")))
        self.sprites.append(pygame.image.load(os.path.join('Assets', "attack_10.png")))
        # Create an associated counter to track which frame we are on.
        self.current_sprite=0
        # The 'image' variable will be equal to the array at whatever index
        # the counter is currently set.
        self.image = self.sprites[self.current_sprite]
        # The rect will be drawn according to the size of whichever
        # frame is currently being played.
        self.rect=self.image.get_rect()
        # Decide the orientation of the image on the screen.
        self.rect.topleft = [SPRITE_X, SPRITE_Y]

    def animate(self):
        self.is_animating = True


    def update(self, speed):
        if self.is_animating == True:
            # For every frame, increase the counter 
            # by whatever the specified speed is
            self.current_sprite += speed
        
            if self.current_sprite >= len(self.sprites):
                self.current_sprite=0
                # If the animation reaches the end, 
                # reset to the beginning.

                self.is_animating = False
                # Reset the animation flag until the
                # user triggers it again.
        
            # Set the image to the current 
            # frame in the array of frames.
            self.image = self.sprites[int(self.current_sprite)]


# General Setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Animation Test File")

# Creating the sprites and groups
frog = CharacterSprite(10, 10)
moving_sprites = pygame.sprite.Group()
moving_sprites.add(frog)

# Main Game Loop
while True:

    # Enable the window close button.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            frog.animate()



    # Drawing
    SCREEN.fill((0,0,0))
    moving_sprites.draw(SCREEN)
    moving_sprites.update(0.25)
    pygame.display.flip()
    clock.tick(60)









