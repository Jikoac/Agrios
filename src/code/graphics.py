import pygame as pg

# Initialize pygame
pg.init()

# Get the screen size
screen_info = pg.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h

# Set the desired resolution
desired_resolution = (1920, 1080)

# Calculate the scale factor based on the screen size
scale_factor = min(screen_width / desired_resolution[0], screen_height / desired_resolution[1])

# Calculate the scaled resolution
scaled_resolution = (int(desired_resolution[0] * scale_factor), int(desired_resolution[1] * scale_factor))

# Create the window with the scaled resolution
window = pg.display.set_mode(scaled_resolution, pg.RESIZABLE)
pg.display.set_caption("Pygame Window Resized to Screen Size")

def display(window, source_surface:pg.Surface, dest:tuple[int,int]|None=None, *args, **kwargs):

    if dest==None:
        dest=((1920-source_surface.get_width())/2,(1080-source_surface.get_height())/2)
    # Create a temporary surface with the desired resolution
    temp_surface = pg.Surface(desired_resolution,pg.SRCALPHA)

    # Blit the source surface onto the temporary surface
    temp_surface.blit(source_surface, dest, *args, **kwargs)

    # Scale the temporary surface to the window size
    scaled_surface = pg.transform.scale(temp_surface, scaled_resolution)

    # Blit the scaled surface onto the window
    window.blit(scaled_surface, (0, 0))

    # Load an image (make sure to replace 'your_image.png' with the path to your image file)
if __name__=='__main__':
    image = pg.image.load("C:/Users/grant/Pictures/Miscellaneous/SC Flag Wallpaper.png")
    character=pg.image.load("C:/Users/grant/Documents/Programs/Games/agrios/src/assets/textures/character/__nonefem__.png")

    # Main loop
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        keys=pg.key.get_pressed()

        # Fill the window with a color (optional)
        window.fill((0, 0, 0))

        # Use the display function to blit and scale the image
        display(window, image)
        display(window,character)

        # Update the display
        pg.display.flip()
        if keys[pg.K_q]:
            running=False
    # Quit pygame
    pg.quit()
