from src import player
import colorama as clr
from classes import spell

color=[
      clr.Fore.RED,
      clr.Fore.YELLOW,
      clr.Fore.GREEN,
      clr.Fore.CYAN,
      clr.Fore.BLUE,
      clr.Fore.MAGENTA,
      clr.Fore.WHITE,
      clr.Fore.RESET,
      clr.Fore.BLACK
]

style={
    'plain':'\033[0m',
    'bold':'\033[1m',
    'italics':'\033[3m'
}

class player(player):
    def __str__(self):
        if self:
            value = f'''{color[self.tier-1]}{style['italics'] if self.tier==7 else ''}{self.name}{style['plain']}{' ★'*self.tier}
 {color[6]}Rating: {style["bold"]}{color[self.tier-1]}{self.rating}{style['plain']}
 {color[min(6,max(0,round(self.health/self.max_health*6)-1))]}HP: {self.health}/{self.max_health}
 {color[0]}Damage: {self.damage}
 {color[2]}Stamina: {self.stamina}/{self.max_stamina}
 {color[1]}Skill: {self.skill}
 {color[6]}Items: {', '.join([color[3-item.size]+item.name for item in self.items])}
 {color[5]}{style["bold"]}Race: {style['plain']}{color[self.race.tier]}{self.race}{color[7]}'''
        else:
            value = f'''{style['bold']}{color[8]}{style['italics'] if self.tier==7 else ''}{self.name}{style['plain']}{' ★'*self.tier}{color[8]}{style['bold']}
 Rating: {self.rating}
 HP: {self.health}/{self.max_health}
 Damage: {self.damage}
 Stamina: {self.stamina}/{self.max_stamina}
 Skill: {self.skill}
 Items: {', '.join([item.name for item in self.items])}
 {style["bold"]}Race: {self.race}{style['plain']}'''
        return value

def deck(hero:player):
    def colortype(item,hero):
        value=item[1]
        if isinstance(value,spell):
            if value.stamina>hero.stamina:
                return color[8]+style['bold']
            return color[value.level+2]
        else:
            return color[1-value.level]
    return f'Your deck:{', '.join([f'{colortype(i,hero)}{style['bold']}{i[0]}:{style['plain']}{colortype(i,hero)}{i[1].name}' for i in zip(range(len(hero.deck)),hero.deck)])}{color[7]}'

def display_xp(hero:player):
    display_color=color[min(5,max(0,hero.xp//100))]
    print(f'You earned {display_color}{hero.xp}{color[7]} XP!')