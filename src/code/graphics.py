import pygame as pg
from data_handling import path,os

#★•*⁎⁕◊◈⁺₊⊹⋇

pg.init()
font=pg.font.SysFont('Noto Sans',25)

def render_text(text:str='',color=(255,255,255),font_data=None):
    text=str(text).replace('★','⁕')
    font_data = font_data or ('Noto Sans',25)
    font=pg.font.SysFont(*font_data)
    lines = text.split('\n')

    max_width = max(font.size(line)[0] for line in lines)
    total_height = sum(font.size(line)[1] for line in lines)
    text_surface = pg.Surface((max_width, total_height), pg.SRCALPHA)

    y_offset = 0
    for line in lines:
        line_surface = font.render(line, True, color)
        text_surface.blit(line_surface, (0, y_offset))
        y_offset += font.size(line)[1]
    
    return text_surface

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

def display_image(window, source_surface:pg.Surface, dest:tuple[int,int]|None=None, *args, **kwargs):

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

def create_card(card_texture:str='card',display_texture:str='character/__none__',text:str=None,text_color=(255,255,255),font_data=None) -> pg.Surface:
    card=pg.image.load(os.path.join(path,'assets','textures','misc',card_texture)+'.png')
    icon=pg.image.load(os.path.join(path,'assets','textures',display_texture)+'.png')
    card.blit(icon,(7,7))
    if text:
        rendered_text=render_text(text,text_color,font_data)
        card.blit(rendered_text,((379-rendered_text.get_width())/2,379))
    return card

def resize(image:pg.Surface,scale:int=1):
    return pg.transform.scale(image,(round(image.get_width()*scale),round(image.get_height()*scale)))

def display(*image_path,pos=None,center=True):
    image = pg.image.load(os.path.join(path,'assets','textures',*image_path)+'.png') if type(image_path[0])==str else image_path[0]
    if pos and center:
        pos=list(pos)
        pos[0]-=image.get_width()/2
        pos[1]-=image.get_height()/2
    display_image(window,image,pos)