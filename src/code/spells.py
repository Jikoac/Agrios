from classes import spell,src_object
from random import randint
import random
class src_spell(src_object):
    type=spell
    damage_spell=spell()
    heal_spell=spell('Healing Spell',condition=None)
    shield_spell=spell('Shield Spell',10,1,condition=None)
    fire_spell=spell('Fire Spell',3)
    sharpness_spell=spell('Sharpness Spell',15,2,condition=None)
    weakening_spell=spell('Weakening Spell',15,2)
    soul_tearing_spell=spell('Soul Tearing Spell',20,3)
    spell_of_wisdom=spell('Spell of Wisdom',15,2,condition=None)
    leech_spell=spell('Leech Spell',7,1)
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