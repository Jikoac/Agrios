from graphics import *
from classes import game,player
from src import src

def wait(time):
    pg.time.delay(round(time*1000))

class game(game):
    def display(self,index=0):
        player_count=len(self.players)
        display('misc','table')
        for i in range(player_count-1):
            i+=1
            current_player=self.players[(index+i)%player_count]
            display(resize(create_card(display_texture=f'character/{current_player.texture}',text=current_player),0.75),pos=(2110-i*350,290))
        main_player=self.players[index]
        display(create_card(display_texture=f'character/{main_player.texture}',text=main_player,font_data=('Noto Sans',20)),pos=(240,640)) 
        item_x=550
        for item in main_player.deck: #Example deck for player
            display(resize(create_card(text=item),0.5),pos=(item_x,800))
            item_x+=200
        pg.display.flip()

main_game=game()

if __name__ == '__main__':
    for _ in range(4):
        main_game.players.append(player(src.character.random()))
    for chrctr in range(4):
        for _ in range(3):
            main_game.players[chrctr].deck.append(src.spell.random())
    for x in range(4):
        main_game.display(x)
        wait(5)