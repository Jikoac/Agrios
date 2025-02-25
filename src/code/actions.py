from classes import action,src_object

class src_action(src_object):
    type=action
    attack=action('Attack',available=False,description='Chance to damage opponent')
    recover=action('Recover',condition={'target':'self','compare':'at_most','standard':'max_health'},description='Heal 1 to 6 HP')
    transform=action('Transform',available=False,level=-1,condition=None)
    antimagic=action('Antimagic',available=False,level=-1)
    def __init__(self):
        self.all=[card for card in self.get_all() if card.available]