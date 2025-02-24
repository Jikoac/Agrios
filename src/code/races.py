from classes import race
human=race() #just a basic human
agrimorph=race("Agrimorph",3) #shapeshifting beings; half human, half shapeless
aioneide=race("Aioneide",1) #immortal beings created by Adraon; can mimic light magic
drakonios=race("Drakonios",2) #dragon-like beings created by Evidzer; immune to fire
aquarian=race("Aquarian",1) #fishlike beings, immune to water
ageless=race("Ageless",3) #ancient beings that can perform black magic
aioneide_evolved=race("Aioneide (Evolved)",2) #immortal beings created by Xzaeon; can mimic medium and light magic
xenopod=race("Xenopod",3) #aliens from planet Xenos; select two cards and perform one on your turn
cyborc=race("Cyborc",2) #mechanically reanimated humans; can resurrect on turn of death
aetherian=race("Akyron",1) #beings created by Xzaeon; not harmed by Xzaeon
cimagiant=race("Cimagiant",1) #beings that can block magic
coelestis=race("Coelestis",4) #gods created by Rizon; take your turn at any time
#if two Coelestis want to take their turn at the same time, the first in order goes first
wild_form=race("Wild Form",0) #the wild form of an agrimorph
rimeborn=race("Rimeborn",1) #beings created by Khione to protect the frostlands; deals 2x damage to Drakonios
aioneide_ascended=race("Aioneide (Ascended)",3) #immortal beings created by Xzaeon; can mimic dark, medium and light magic
ungod=race('ungod',tier=5) #Knoughn is the only ungod, and continues to play even after his death
aionimorph=race('Aionimorph',4) #Aionimorphs are half Aioneide, half Agrimorph, and can take the form of any Agrimorph
anthrimorph=race('Anthrimorph',3) #Anthrimorphs are humans that have artificially gained shapeshifting powers

races = [
    human,
    agrimorph,
    aioneide,
    drakonios,
    aquarian,
    ageless,
    aioneide_evolved,
    xenopod,
    cyborc,
    aetherian,
    cimagiant,
    coelestis,
    rimeborn,
    aioneide_ascended,
    ungod,
    aionimorph
]