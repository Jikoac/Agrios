from classes import action,src_object

class src_action(src_object):
    type=action
    attack=action('Attack',available=False)
    recover=action('Recover',condition=None)
    transform=action('Transform',available=False,level=-1,condition=None)
    antimagic=action('Antimagic',available=False,level=-1)
    def __init__(self):
        self.all=[card for card in self.get_all() if card.available]