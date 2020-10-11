import keyboard as k
from colorama import Fore
import random as r
def game(value):# condition to continue the game and value would be passed by the user 
    comp=['paper','scissors','rock']
    random_choice=r.choice(comp)
    # logic 
    winner=""
    if random_choice=='paper' and value=='rock': 
        winner='computer'
    elif random_choice=='paper' and value=='paper': 
        winner='tie'
    elif random_choice=='paper' and value=='scissors': 
        winner="user"
    elif random_choice=='rock' and value=='rock': 
        winner='tie'
    elif random_choice=='rock' and value=='paper': 
        winner='user'
    elif random_choice=='rock' and value=='scissors': 
        winner='computer'
    elif random_choice=='scissors' and value=='scissors': 
        winner='tie'
    elif random_choice=='scissors' and value=='rock': 
        winner='user'
    else: 
        winner='computer'
    print(Fore.GREEN+winner)
    print('wanna play again then press enter or else press esc')
    choice= " "
    if k.read_key('enter'): 
        print('thank you for playing again enter ur choice')
        while choice not in ['paper','scissors','rock']:
            choice=input(':-')
            game(choice)
    elif k.read_key('esc'): 
        print('bye')
value=" "
choice=" "
while value not in ['paper','scissors','rock']:
    choice=input(" enter rock paper or scissors")
    value=choice
game(value)
#author:someone_named_:-_the_boring_guy
