#this file is where lore will be stored
import random
from data_handling import load, check_path
lore=[
    'The rimeborn were created by Khione to protect the frostlands. They deal double damage to Drakonios.',
    # 'Agrimorphs are shapeshifting beings, half human and half shapeless. Each agrimorph has a wild form.',
    # 'Aioneides are immortal beings created by Adraon. They can mimic different levels of magic.',
    'Drakonios are dragon-like beings created by Evidzer. They are immune to fire.',
    # 'Aquarians are fishlike beings, immune to water.',
    'Ageless are ancient beings that can perform black magic.',
    # 'Xenopods are aliens from planet Xenos. They can select two cards and perform one on their turn.',
    # 'Cyborcs are mechanically reanimated humans. They can resurrect on the turn of death.',
    'Akyrons are beings created by Xzaeon. They are not harmed by Xzaeon.',  
    # 'Cimagiants are beings that can block magic.',
    # 'Coelestis are gods created by Rizon. They can take their turn at any time.',
    'Zerriah is an Aioneide sorceress, who is married to Ishmael Archwarden.',
    'Ishmael Archwarden is an agrimorph with the wild form of a gryphon.',
    'Zadraen Vorres is a xenopod married to Xeira Vorres.',
    'Vaelora is the queen of the Drakonios.',
    'Gryphon Monarch is the chosen one, and the king of the agrimorphs.',
    'Eternal Gryphon is the ascendant form of Gryphon Monarch, and the rarest card in the game.',
    'Evidzer is the god of fire and the creator of the Drakonios.',
    'Khione is the goddess of ice and the creator of the rimeborn.',
    'Hecate is the goddess of magic and queen of the ageless.',
    'Rizon is the god of creation and ruler of the coelestis.',
    'Xzaeon is the god of Oblivion, and lord of The Aether',
    'Adraon was the god of light and creator of the aioneides before he became Xzaeon.',
    'Taranis is the ageless high priest of Hecate.',
    'Only ageless can perform black magic.',
    'After Ishmael Archwarden becomes the Gryphon Monarch, he replaces Adraon as the god of light.',
    'Ishmael Archwarden marries Zerriah Netherbane in a Xenon wedding, binding their souls.',
    'Rizon and Knoughn are the only two beings not confined to one dimension.',
    'Knoughn the ungod is the second most powerful being in existence.',
    'Knoughn the ungod is the creator of The Oblivion.',
    'The shapeless are the only beings that can take any shape.',
    'Echo is a shapeless that was corrupted by The Oblivion.',
    'The Oblivion is the void that consumes all.',
    'Vaelora was created by Evidzer to be his queen.',
    'Evidzer was the god that defeated Adraon when he turned to darkness before his banishment.',
    'Rizon banished Adraon to The Aether when he tried o corrupt Eden.',
    'Angel Silverthorn\'s real name is Angela Veeres, but she changed it when Taranix killed her family.',
    'Angela Silverthorn\'s father was Orroman Veeres, lord of the western cimagiants.',
    'Angela Silverthorn\'s mother, Diana Ironblade, was actualy a Silverthorn who changed her name.',
    'The Veeres ruled the western cimagiants and the Silvernthorns rule the eastern cimagiants.',
    'Diana Ironblade left her family because the east wouldn\'t confront Taranis, but the west would.',
    'Taranis killed the entire Veeres family for opposing the Ageless.',
    'Zerriah Netherbane learned more magic than any being by staying with The Ageless for millenia.',
    'When Zerriah absorbs Hecate\'s life force, she becomes Mage Goddess Netherbane.',
    'Odessa Fray is an Agrimorph with an eagle form who falls in love with Ishmael Archwarden.',
    'Baezer Ves was a human general before he was reanimated as the cyborc general.',
    'Vander Everdenne is the creator of the cyborcs, and becomes one himself after his death.',
    'Jonnis Vexer ruled the Cimagiants who wouldn\'t follow the Silverthorns after the Veeres died.',
    'Theus was the Ageless mage who taught Zerriah Netherbane most of what she knows.',
    'Ulysseus is the Ageless blacksmith who forged the Gryphon Monarch\'s armor',
    #First 50 ^
    'There are only two beings more powerful than the Coelestis.'
]

if check_path('data','games_played'):
    games_played=load('data','games_played')
    lore.append(f'You have played {games_played} games.')
if check_path('data','joined'):
    joined=load('data','joined')
    lore.append(f'You first played Agrios {joined}')

def fun_fact():
    return random.choice(lore)

if __name__ == "__main__":
    print(f"There are {len(lore)} hints in the lore.")