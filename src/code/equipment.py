from classes import equipment,src_object
import random
class src_equipment(src_object):
    type=equipment
    knight_sword=equipment(description='Increase damage by 5')
    knight_shield=equipment('Knight Shield','health','add',5,description='Increase health by 5')
    knight_armor=equipment('Knight Armor','health','add',10,description='Increase health by 10')
    warrior_sword=equipment('Warrior Sword','damage','add',10)
    warrior_armor=equipment('Warrior Armor','health','add',15,description='Increase health by 15')
    ancient_glyph=equipment('Ancient Glyph','stamina','add',5)
    gilded_hilt=equipment('Gilded Hilt','skill','add',1)
    sledge_hammer=equipment('Sledge Hammer','damage','mul',2,2)
    dragon_sword=equipment('Dragon Sword','damage','set',20,2)
    scroll_of_hecate=equipment('Scroll of Hecate','has_hecate_scroll','set',True,3)
    time_amulet=equipment('Time Amulet','moves_per_turn','set',2,2)
    ancient_scroll=equipment('Ancient Scroll','stamina','mul',2,2,description='Multiply stamina by 2')
    energy_crystal=equipment('Energy Crystal','regen','add',1)