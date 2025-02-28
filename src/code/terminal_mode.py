import os
from time import time
from src import src
from lore import fun_fact
from random import randint
from styling import player,deck,color,style,display_xp,tutorial
from data_handling import check_file,load,save
from datetime import datetime
os.system('cls' if os.name == 'nt' else 'clear')
if not check_file('data','joined'):
    now=datetime.now()
    current_time = now.strftime(f"%m/%d/{now.strftime('%Y')}, %H:%M:%S")
    save('data','joined',data=current_time)
if check_file('data','games_played'):
    games_played=int(load('data','games_played'))
else:
    games_played=0
    tutorial()
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
if not 'y' in input('Open settings? (Y/N) ').lower():
    allow_non_heal=input('Allow non-healing action cars? (Y/N)')
    selected_hero=input('Select a hero: ').lower().replace(' ','_') or None
    if selected_hero:
        try:
            player_hero=src.character.items[selected_hero]
        except:
            player_hero=None
else:
    allow_non_heal=True
    player_hero=None

games_played+=1
save('data','games_played',data=games_played)

def set_character(character=None):
    hero=character or src.character.random()
    items=[]
    inventory=hero.slots
    while inventory:
        new_item=src.equipment.random()
        if new_item.size<=inventory:
            items.append(new_item)
            inventory-=new_item.size
    return player(hero,*items)
hero=set_character(player_hero)
hero.deck+=[src.action.random()] if not 'n' in allow_non_heal.lower() else [src.action.recover]
cards=5
while cards:
    card=src.spell.randomized()
    if (card.level<3 or hero.race.id=='ageless') and card.stamina<=hero.max_stamina:
        hero.deck+=[card]
        cards-=1
enemy_0=set_character()
enemy_1=set_character()
enemies=[enemy_0,enemy_1]

start_time = time()
turns=0

while (hero.health>0) and ((enemy_0.health>0) or (enemy_1.health>0)):
    turns+=1
    hero.stamina=min(hero.stamina+hero.property['regen'],hero.max_stamina)
    enemy_0.stamina=min(enemy_0.stamina+1,enemy_0.max_stamina)
    enemy_1.stamina=min(enemy_1.stamina+1,enemy_1.max_stamina)
    for move in range(hero.property['moves_per_turn']):

        finished=None
        while not finished:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'Did you know... {style['bold']}{fun_fact()}{style['plain']}')
            print(hero)
            print(style['bold']+'0.'+style['plain']+str(enemy_0))
            print(style['bold']+'1.'+style['plain']+str(enemy_1))
            print(deck(hero))
            if finished == False:
                print(color[0]+'Invalid action. Try again.'+color[7])
            card=input('Choose a card: ')
            if '?' in card:
                print(style['bold']+hero.deck[int(card.replace('?','').strip())].description+style['plain'])
                input('Continue ')
            else:
                target=input('Choose a target: ')
                try:
                    finished=hero.use_card(int(card or randint(0,len(hero.deck))),enemies[int(target or randint(0,1))])
                except ValueError:
                    finished=False
                except IndexError:
                    finished=False
            
    if (enemy_0.health<enemy_0.max_health/2) and enemy_0:
        enemy_0.recover()
    elif enemy_0:
        enemy_0.attack(hero)
    if (enemy_1.health<enemy_1.max_health/2) and enemy_1:
        enemy_1.recover()
    elif enemy_1:
        enemy_1.attack(hero)

end_time = time()
fight_duration = end_time - start_time

os.system('cls' if os.name == 'nt' else 'clear')
print('You win!' if hero.health>0 else 'You lose!')
print(f'The fight lasted {turns:02} turn{'s' if turns>1 else ''} and took {fight_duration:.2f} second{'s' if fight_duration!=1 else ''}.')
hero.xp+=50*len([enemy for enemy in enemies if not enemy.health>0])
if hero.health>0:
    hero.xp+=100
display_xp(hero)
if check_file('data','XP'):
    xp=int(load('data','XP'))
else:
    xp=0
xp+=hero.xp
save('data','XP',data=str(xp))
print(f'Total {style['bold']}XP:{style['plain']}{color[2]}{str(xp)}{color[7]}')