import os
from time import time
from src import src
from lore import fun_fact
from random import randint
from styling import player,deck,color,style,display_xp
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
hero=set_character()
hero.deck+=[src.action.random()]
cards=5
while cards:
    card=src.spell.randomized()
    if (card.level<3 or hero.race.id=='akyron') and card.stamina<=hero.max_stamina:
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
            print(f'Did you know... {fun_fact()}')
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
                finished=hero.use_card(int(card or randint(0,len(hero.deck))),enemies[int(target or randint(0,1))])
            
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
hero.xp+=50*(2-len([enemy for enemy in enemies if not enemy.health>0]))
if hero.health>0:
    hero.xp+=100
display_xp(hero)