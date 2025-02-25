from classes import character,src_object
from races import *
from random import randint
import random
class src_character(src_object):
    def __init__(self):
        self.all:list[character]=[character for character in self.get_all() if character.race!=wild_form]
        self.wild:list[character]=[character for character in self.get_all() if character.race==wild_form]
    type=character
    james_forge=character()
    ishmael_archwarden=character("Ishmael Archwarden",12,4,15,2,2,agrimorph)
    ishmael_archwarden_wild=character("Ishmael Archwarden",15,10,5,4,2,wild_form)
    zerriah_netherbane=character("Zerriah Netherbane",8,5,20,2,3,aioneide,gender='female')
    brutus_greye=character("Brutus Greye",10,7,6,3,1,human)
    angela_silverthorn=character("Angela Silverthorn",10,6,10,3,2,cimagiant,gender='female')
    gryphon_monarch=character("Gryphon Monarch",18,6,20,3,3,agrimorph)
    gryphon_monarch_wild=character("Gryphon Monarch",20,15,10,5,3,wild_form)
    taranis=character("Taranis",15,3,25,2,3,ageless)
    xzaeon=character("Xzaeon",20,7,15,3,3,coelestis)
    theus=character("Theus",10,4,16,3,1,ageless)
    vaelora=character("Vaelora",12,5,18,3,2,drakonios,gender='female')
    lord_frostbite=character("Lord Frostbite",15,8,10,4,2,rimeborn)
    oreal_fen=character("Oreal Fen",12,5,8,2,2,aquarian)
    dan_netherbane=character("Dan Netherbane",15,3,5,2,1,aioneide)
    baezer_ves=character("Baezer Ves",8,4,10,3,1,cyborc)
    grand_sorceress_netherbane=character("Grand Sorceress Netherbane",12,6,25,3,3,aioneide_evolved,gender='female')
    eternal_gryphon=character("Eternal Gryphon",25,12,30,4,3,agrimorph)
    eternal_gryphon_wild=character("Eternal Gryphon",31,20,18,5,3,wild_form)
    zadraen_vorres=character("Zadraen Vorres",12,6,10,2,2,xenopod)
    xeira_vorres=character("Xeira Vorres",11,3,15,3,1,xenopod,gender='female')
    odessa_fray=character("Odessa Fray",10,4,12,3,1,agrimorph,gender='female')
    odessa_fray_wild=character("Odessa Fray",8,11,10,4,1,wild_form,gender='female')
    adriguar_zaoholde=character("Adriguar Zaoholde",15,5,20,3,2,xenopod)
    vog_uldarr=character("Vog Uldarr",13,3,6,2,1,aetherian)
    benjamin_heiss=character("Benjamin Heiss",17,4,11,2,2,human)
    darius_kael=character("Darius Kael",10,6,8,3,1,cyborc)
    iarro_dreonne=character("Iarro Dreonne",16,2,10,4,1,drakonios)
    ulysseus=character("Ulysseus",12,5,15,3,2,ageless)
    kazaron=character("Kazaron",15,6,20,3,2,drakonios)
    mina_leere=character("Mina Leere",10,4,8,2,1,aquarian,gender='female')
    jonnis_vexer=character("Jonnis Vexer",12,5,10,3,1,cimagiant)
    sirius=character("Sirius",15,6,15,3,2,drakonios)
    vilzen_stonehollow=character("Vilzen Stonehollow",12,5,12,3,1,rimeborn)
    maea_stonehollow=character("Maea Stonehollow",10,4,10,2,1,rimeborn,gender='female')
    hecate=character("Hecate",15,6,30,3,2,coelestis,gender='female')
    mage_goddess_netherbane=character("Mage Goddess Netherbane",20,8,25,4,3,aioneide_ascended,gender='female')
    mara_kael=character("Mara Kael",10,5,10,3,1,cyborc,gender='female')
    veeren_des=character("Veeran Des",12,4,10,2,2,aetherian)
    alenthria_emberleine=character("Alenthria Emberleine",15,6,15,3,2,drakonios,gender='female')
    gryphon_god_archwarden=character("Gryphon God Archwarden",35,20,25,5,3,coelestis)
    knoughn=character("Knoughn",30,25,20,5,3,ungod)
    jaer_atlantium=character("Jaer Atlantium",15,5,12,3,2,aquarian)
    jason_rozar=character("Jason Rozar",24,6,15,3,2,human)
    # Series 0
    julius_archwarden=character("Julius Archwarden",30,15,30,4,3,aionimorph,series='Series 0')
    julius_archwarden_wild=character("Julius Archwarden",35,25,20,5,3,wild_form,series='Series 0')
    dara_zenne=character("Dara Zenne",20,7,15,3,2,cimagiant,gender='female',series='Series 0')
    matthias_archwarden=character("Matthias Archwarden",20,12,21,4,3,aionimorph,series='Series 0')
    matthias_archwarden_wild=character("Matthias Archwarden",25,18,25,4,3,wild_form,series='Series 0')
    jonas_hunter=character('Jonas Hunter',15,9,15,4,3,anthrimorph,series='Series 0')
    jonas_hunter_wild=character('Jonas Hunter',10,14,5,4,3,wild_form,series='Series 0')
    iris_forge=character('Iris Forge',15,7,10,3,1,agrimorph,'female','Series 0')
    iris_forge_wild=character('Iris Forge',20,16,10,3,1,wild_form,'female','Series 0')
    silas_wayne=character('Silas Wayne',20,8,15,3,3,anthrimorph,series='Series 0')
    silas_wayne_wild=character('Silas Wayne',10,8,10,6,3,wild_form,series='Series 0')
    christopher_drake=character('Christopher Drake',25,10,20,4,2,human,series='Series 0')

    def tier(self,tier:int):
        return [character for character in self.all if character.tier==tier]
    def race(self,race:race):
        return [character for character in self.all if character.race==race]
    def random(self):
        value=randint(1,100)
        if value <=50:
            tier=1
        elif value <=75:
            tier=2
        elif value <=90:
            tier=3
        elif value <=97:
            tier=4
        else:
            tier=5
        return random.choice(self.tier(tier))
    def series(self,series=None):
        return [char for char in self.all if char.series == series]

if __name__=='__main__':
    name=input('Character Name:')
    for char in src_character().all:
        if char.name == name:
            print(char)
            if char.race in wild:
                for char in src_character().wild:
                    if char.name==name:
                        print(char)
                        break
            break
    if name=='' or name=='__tier__':
        print(len(src_character().all))
        for i in range(7):
            i+=1
            print(('★ '*i)+str(len(src_character().tier(i))))
    elif name=='__all__':
        for char in src_character().all:
            print(char)
            if char.race in wild:
                for wild in src_character().wild:
                    if wild.name==char.name:
                        print(wild)
                        break
    elif name=='__race__':
        for r in races:
            print(f'{r.name}: {len(src_character().race(r))}')
    elif name=='__gender__':
        for gender in ['Male','Female']:
            print(f'{gender}: {len([char for char in src_character().all if char.gender == gender.lower()])}')
    elif name == '__series__':
        series=[char.series for char in src_character().all]
        series = list(set(series))
        for s in series:
            print(f'{str(s)}: {len(src_character().series(s))}')
    elif name not in list(map(lambda x:x.name,src_character().all)):
        print('Character not found!')