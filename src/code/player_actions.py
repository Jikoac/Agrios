from classes import player
from characters import src_character
from random import randint
class player(player):
    def attack(self,target):
        if randint(1,6) <= self.skill:
            if self.race.id=='rimeborn' and target.race.id=='drakonios':
                target.health-=2*self.damage
            else:
                target.health-=self.damage
    def recover(self):
        increased_health=min(self.health+randint(1,6),self.max_health)
        self.health=max(increased_health,self.health)
    def perform_action(self,action,target=None):
        if action.id=='attack':
            self.attack(target)
        elif action.id=='recover':
            self.recover()
        elif action.id=='transform':
            if self.other_form:
                self.transform(self.other_form)
            else:
                for char in src_character().wild:
                    if char.id == self.id and char.series == self.series:
                        self.transform(char)
                        break
        elif action.id=='antimagic':
            pass