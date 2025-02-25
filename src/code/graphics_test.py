from graphics import *
from src import src

test_card=create_card(text=src.character.knoughn)

running=True
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
    window.fill((0,0,0))
    display(window,test_card)
    pg.display.flip()
    keys=pg.key.get_pressed()
    if keys[pg.K_q]:
        running=False
pg.quit()