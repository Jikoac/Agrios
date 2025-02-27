from graphics import *
from classes import game,player
from src import src

def wait(time):
    pg.time.delay(round(time*1000))

class game(game):
    def display(game):
        display('misc','table')
        display(resize(create_card(text=player(src.character.knoughn)),0.75),pos=(1060,290)) #Next example player to take turn
        display(resize(create_card(text=player(src.character.xzaeon)),0.75),pos=(1410,290)) #Example player
        display(resize(create_card(display_texture='character/__nonefem__',text=player(src.character.hecate)),0.75),pos=(1760,290)) #Example player
        display(create_card(display_texture='character/__nonefem__',text=player(src.character.mage_goddess_netherbane,src.equipment.knight_armor),font_data=('Noto Sans',20)),pos=(240,640)) #Example player taking turn
        item_x=550
        for item in [src.action.attack,src.action.rest]: #Example deck for player
            display(resize(create_card(text=item),0.5),pos=(item_x,800))
            item_x+=200
        pg.display.flip()

main_game=game()

if __name__ == '__main__':
    for _ in range(4):
        game.players.append(src.character.random())
    main_game.display()
    wait(5)