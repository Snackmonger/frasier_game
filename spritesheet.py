import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image
        '''
        The user must define an image in pygame:

            sprite_sheet_image = pygame.image.load(os.path.join("Assets", "doux.png")).convert_alpha()
            # Defining a variable to represent the whole image.

            sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
            # Defiining an instance of the SpriteSheet class,
            # using sprite_sheet_image as the image data.

        Then the user can call the methods of the class:

            frame_0 = sprite_sheet.get_frame(0, 24, 24, 3, BLACK)
            anim_1 = sprite_sheet.define_animation([1,2,3,4,5], 24, 24, 3, BLACK)
        '''

    def get_frame(self, frame_number, width, height, scale, colour):
        '''
        Return a single frame of a spritesheet.
        Define the width and height of the frame, as well as
        a scale multiplier and a transparency colour.
        '''

        extrated_frame = pygame.Surface((width, height)).convert_alpha()
        # Define a frame as a pygame surface with width & heght. 

        extracted_frame.blit(self.sheet, (0,0), ((frame_number*width), 0, width, height))
        # Blit spritesheet self.sheet onto the frame, and blit it
        # onto the frame surface at (0,0), but blit only a 
        # (selection of the source sheet, beginning at position 
        # ((frame# * width), 0) and ending at postion (total width, total height))

        extracted_frame = pygame.transform.scale(frame_number, (width*scale, height*scale))
        # Rescale the frame by whatever factor is specified in the method call.

        extracted_frame.set_colorkey(colour)
        # Define which colour will be treated as transparent.

        return extracted_frame


    def define_animation(self, frame_order, width, height, scale, colour):
        '''
        This is a simple method to use the get_frame method above
        to assemble an array of images for use in an animation.

        The user must specify the order of the frames in a list/tuple:
        frame_order = [1,4,5,6,8]. Other variables are passed to the 
        get_frame method.
        '''

        animation = []
        for frame in frame_order:
            animation.append(self.get_frame(frame_order(frame), width, height, scale, colour))

        return animation
        
