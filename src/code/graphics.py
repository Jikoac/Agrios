import pygame as pg
from data_handling import path

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
pg.display.set_caption("Αγριος")

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
