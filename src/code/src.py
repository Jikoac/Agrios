from characters import src_character
from equipment import src_equipment
from actions import src_action
from spells import src_spell
from player_actions import player as player_act
from spell_actions import player as player_spell
from classes import action, spell,path,user

class src:
    character=src_character()
    equipment=src_equipment()
    action=src_action()
    spell=src_spell()
    path=path

class player(player_act,player_spell):
    def use_card(self,number=0,target=None):
        def test(conditions:dict={'target':'enemy','value':'health','compare':'at_least','standard':0}):
            # Default conditions
            condition={'target':'enemy','value':'health','compare':'at_least','standard':0}
            # Set the conditions
            if not conditions:
                return True
            condition.update(conditions)
            if condition['target']=='enemy':
                test_target=target
            else:
                test_target=self
            # Get the values
            value_a = getattr(test_target,condition['value'])
            if type(condition['standard']) == str:
                value_b = getattr(test_target,condition['standard'])
            else:
                value_b = condition['standard']
            # Compare the values
            if condition['compare']=='at_least':
                return value_a >= value_b
            elif condition['compare']=='at_most':
                return value_a<=value_b
            return False
        try:
            card=self.deck[number]
        except IndexError:
            return False
        if not test(card.condition):
            return False
        if isinstance(card,action):
            self.perform_action(card,target)
        elif isinstance(card,spell):
            return self.perform_spell(card,target)
        return True

class user(user):
    def acquire(self,name,can_be_owned:bool=False):
        if can_be_owned:
            item = getattr(src,name).random
            getattr(self,name).append(item)
        else:
            item = getattr(src,name).unowned(self,name)
            if item:
                getattr(self,name).append(item)