from classes import player
from random import randint
from races import drakonios
class player(player):
    def damage_spell(self,target:player):
        target.health-=self.damage
    def heal_spell(self):
        increased_health=min(self.health+randint(1,6),self.max_health)
        self.health=max(increased_health,self.health)
        increased_health=min(self.health+randint(1,6),self.max_health)
        self.health=max(increased_health,self.health)
    def shield_spell(self):
        self.health+=10
    def fire_spell(self,target:player):
        if randint(1,6) <= self.skill:
            target.health-=self.damage
        if randint(1,6) <= self.skill:
            target.health-=self.damage
    def sharpness_spell(self):
        self.damage+=1
    def weakening_spell(self,target:player):
        target.damage-=1
    def soul_tearing_spell(self,target:player):
        target.max_health-=randint(1,6)
        target.health=min(target.health,target.max_health)
    def spell_of_wisdom(self):
        self.skill+=randint(0,2)
    def leech_spell(self,target:player):
        if randint(1,6)<=(self.skill*1.5):
            increased_health=min(self.health+self.damage,self.max_health)
            self.health=max(increased_health,self.health)
            target.health-=self.damage
    def new_spell(self):
        pass

    def perform_spell(self,spell,target:player=None):
        if self.stamina>=spell.stamina:
            self.stamina-=spell.stamina
            if not self.property['has_hecate_scroll']:
                self.deck.remove(spell)
        else:
            return False
        if spell.id=='damage_spell':
            self.damage_spell(target)
        elif spell.id=='healing_spell':
            self.heal_spell()
        elif spell.id=='shield_spell':
            self.shield_spell()
        elif spell.id=='fire_spell':
            if target.race!=drakonios:
                self.fire_spell(target)
            else:
                self.stamina-=spell.stamina
                if not self.property['has_hecate_scroll']:
                    self.deck.append(spell)
                return False
        elif spell.id=='sharpness_spell':
            self.sharpness_spell()
        elif spell.id=='weakening_spell':
            self.weakening_spell(target)
        elif spell.id=='soul_tearing_spell':
            self.soul_tearing_spell(target)
        elif spell.id=='spell_of_wisdom':
            self.spell_of_wisdom()
        elif spell.id=='leech_spell':
            self.leech_spell(target)
        return True
