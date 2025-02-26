from classes import player
from characters import src_character
from random import randint
class player(player):
    def attack(self,target):
        if randint(1,6) <= self.skill:
            self.xp+=2*self.damage
            if self.race.id=='rimeborn' and target.race.id=='drakonios':
                target.health-=2*self.damage
            else:
                target.health-=self.damage
    def recover(self):
        increase=randint(1,6)
        increased_health=min(self.health+increase,self.max_health)
        self.health=max(increased_health,self.health)
        self.xp+=increase
    def rest(self):
        self.stamina=min(self.stamina+5,self.max_stamina)
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
                    if char.id == (self.id+'_wild') and char.series == self.series:
                        self.transform(char)
                        break
        elif action.id=='rest':
            self.rest()
        elif action.id=='antimagic':
            pass