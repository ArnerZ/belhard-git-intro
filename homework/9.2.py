
import random
import enum

class Colors(enum.Enum):
    red = 1
    purple = 2

class Toys(enum.Enum):
    ball = 1 
    angel = 2

def toy():
    color_list = (random.choice(list(Colors)))
    toy_list = (random.choice(list(Toys)))
    print (f'{color_list.name} {toy_list.name}')
