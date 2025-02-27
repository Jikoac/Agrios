from random import randint
import random
import pygame as pg
from data_handling import os,path,load
import json

class race:
    def __init__(self,name="Human",tier=0):
        self.name = name
        self.tier = tier
        self.id = name.lower().replace(' ','_')
    def __str__(self):
        return self.name
class character:
    def __init__(self,name="James Forge",health=10,damage=5,stamina=10,skill=2,slots=1,race=race(),gender='male',series:str|None=None,**properties):
        self.name = name
        self.id = name.lower().replace(' ','_')
        self.health = health
        self.damage = damage
        self.stamina = stamina
        self.skill = skill
        self.slots = slots
        self.race = race
        self.gender = gender
        self.series=series
        self.property=properties

        texture_path=os.path.join(path,'assets','textures','character')
        if os.path.isfile(os.path.join(texture_path,self.id)):
            self.texture=pg.image(os.path.join(texture_path,self.id))
        else:
            os.path.join(texture_path,('__none__' if gender == 'male' else '__nonefem__'))

        self.rating = health + stamina +2*damage +5*skill +10*slots +5*race.tier
        self.tier=0
        if self.rating-self.race.tier*5>=150:
            self.tier=7
        elif self.rating-self.race.tier*5>=120:
            self.tier=6
        elif self.rating>100:
            self.tier=5
        elif self.rating>85:
            self.tier=4
        elif self.rating>70:
            self.tier=3
        elif self.rating>60:
            self.tier=2
        elif self.rating>=50:
            self.tier=1
    def attack(self):
        if randint(1,6) <= self.skill:
            return self.damage
    def __format__(self,format_spec):
        if format_spec == "stats":
            return f"{self.name}{' ★'*self.tier}\n Rating: {self.rating}\n HP: {self.health}\n Damage: {self.damage}\n Stamina: {self.stamina}\n Skill: {self.skill}\n Slots: {self.slots}\n Race: {self.race}"
    def __str__(self):
        return format(self,"stats")
class player:
    def __init__(self,character:character=character(),*items):
        self.character=character
        self.items=items
        self.name=character.name
        self.health=character.health
        self.damage=character.damage
        self.stamina=character.stamina
        self.skill=character.skill
        self.slots=character.slots
        self.max_health=character.health
        self.max_stamina=character.stamina
        self.rating=character.rating
        self.tier=character.tier
        self.race=character.race
        self.actions=2
        self.spells=10
        self.deck=[action('Attack',available=False,description='Chance to damage opponent')]
        self.discard=[]
        self.property={'has_hecate_scroll':False,'moves_per_turn':1,'regen':1}
        self.property.update(character.property)
        self.id=self.name.lower().replace(' ','_')
        self.other_form=None
        self.xp=0
        for item in items:
            self.equip(item)
    def __format__(self,format_spec):
        if format_spec == "stats":
            return f"{self.name}{' ★'*self.tier}\n Rating: {self.rating}\n HP: {self.health}/{self.max_health}\n Damage: {self.damage}\n Stamina: {self.stamina}/{self.max_stamina}\n Skill: {self.skill}\n Items: {', '.join([item.name for item in self.items])}\n Race: {self.race}"
    def __str__(self):
        return format(self,"stats")
    def equip(self,item):
        if item.stat in self.__dict__ and not item.is_custom:
            stat=getattr(self,item.stat)
        else:
            stat=self.property[item.stat]
        if item.mode=='add':
            stat+=item.value
            if item.stat=='health':
                self.max_health+=item.value
            if item.stat=='stamina':
                self.max_stamina+=item.value
        elif item.mode=='mul':
            stat*=item.value
            if item.stat=='health':
                self.max_health*=item.value
            if item.stat=='stamina':
                self.max_stamina*=item.value
        elif item.mode=='set':
            stat=item.value
            if item.stat=='health':
                self.max_health=item.value
            if item.stat=='stamina':
                self.max_stamina=item.value
        if item.stat in self.__dict__ and not item.is_custom:
            setattr(self,item.stat,stat)
        else:
            self.property[item.stat]=stat
    def __bool__(self):
        return self.health>0
    def transform(self,new_character):
        original=self
        if isinstance(new_character,character):
            self.__init__(new_character,self.items)
            self.other_form=original
            self.deck=original.deck
        else:
            self.__dict__=new_character.__dict__

class equipment:
    def __init__(self,name='Knight Sword',stat='damage',mode='add',value=3,size:int=1,custom=False,description=''):
        self.name=name
        self.stat=stat
        self.mode=mode
        self.value=value
        self.size=size
        self.is_custom=custom
        self.description=description
class src_object:
    type=None
    name='items'
    def __init__(self):
        self.items={}
        self.all=self.get_all()
    def __iter__(self):
        return self.all.__iter__()
    def get_all(self,type=None):
        self.items={}
        type = type or self.type
        objects = []
        for attr_name in dir(self):
            attr_value = getattr(self, attr_name)
            if isinstance(attr_value, type):
                objects.append(attr_value)
                attr_value.id=attr_name
                self.items.update({attr_name:attr_value})
        return objects
    def random(self):
        return random.choice(self.all)
    def unowned(self,user,name:str=None):
        name = name or self.name
        unowned_items=type(self)()
        unowned_items.all=[item for item in unowned_items.all if not item in getattr(user,name)]
        if len(unowned_items.all):
            return unowned_items.random()
        user.grants.append(name)
        return None
class action:
    def __init__(self,name='Attack',available=True,description='',level=0,condition:dict={'target':'enemy','value':'health','compare':'at_least','standard':0}):
        self.name=name
        self.id=name.lower().replace(' ','_')
        self.available=available
        self.description=description
        self.level=level
        self.rarity=['Common','Rare','Exclusive']
        self.condition=condition
    def __str__(self):
        return f'{self.name}\n{self.description}'
class spell:
    def __init__(self,name='Damage Spell',stamina=5,level=0,description='',condition:dict={'target':'enemy','value':'health','compare':'at_least','standard':0},element=None):
        self.name=name
        self.stamina=stamina
        self.level=level
        self.tier=['light','medium','dark','black'][level]
        self.id=name.lower().replace(' ','_')
        self.description=description
        self.condition=condition
        self.element=element
    def __str__(self):
        return f'{self.name}\n{self.description}'

class user:
    def __init__(self,user_data=''):
        data={'character':['james_forge'],'equipment':[],'action':['recover'],'spell':['damage_spell'],'grants':['character']}
        user_data=json.loads(user_data)
        data.update(user_data)
        self.__dict__.update(data)
class game:
    darkness=0
    players=[]