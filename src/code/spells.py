from classes import spell,src_object
from random import randint
import random
class src_spell(src_object):
    type=spell
    damage_spell=spell(description=' Garunteed to\ndamage opponent\n Uses 5 stamina')
    heal_spell=spell('Healing Spell',condition={'target':'self','compare':'at_most','standard':'max_health'},description='Heal 2 to 12 HP\n Uses 5 stamina')
    shield_spell=spell('Shield Spell',10,1,condition=None,description='Heal 10 HP. Ignores max HP\n Uses 10 stamina')
    fire_spell=spell('Fire Spell',3,description=' Two chances to\ndamage opponent\n Uses 3 stamina',element='fire')
    sharpness_spell=spell('Sharpness Spell',15,2,condition=None,description='Increase damage by 1\n Uses 15 stamina')
    weakening_spell=spell('Weakening Spell',15,2,description='Decrease enemy damage by 1\n Uses 15 stamina')
    soul_tearing_spell=spell('Soul Tearing Spell',20,3,description=' Decrease enemy\'s max\nHP by up to 6\n Uses 20 stamina')
    spell_of_wisdom=spell('Spell of Wisdom',15,2,condition=None,description='Increase skill by 0 to 2\n Uses 15 stamina')
    leech_spell=spell('Leech Spell',7,1,description='Chance to steal health\n Uses 7 stamina')
    # summoning_spell=spell('Summoning Spell',15,2,'Increase Darkness by 1. When Darkness reaches 5, Xzaeon is summoned.\nUses 15 stamina')
    tsunami_spell=spell('Tsunami Spell',10,1,' Unleash a wave of damage\non an enemy\n Damage is a random number\n between 1 and 6\ntimes a random number\nbetween 1 and 3\n Uses 12 Stamina',element='water')
    magma_spell=spell('Magma Spell',12,1,'Five chances to damage enemy',element='fire')
    def tier(self,tier=0):
        return [spell for spell in self.all if spell.level==tier]
    def random(self):
        level=randint(1,100)
        if level <=50:
            return random.choice(self.tier(0))
        elif level <=80:
            return random.choice(self.tier(1))
        elif level <=95:
            return random.choice(self.tier(2))
        else:
            return random.choice(self.tier(3))
    def randomized(self):
        return random.choice(self.all)