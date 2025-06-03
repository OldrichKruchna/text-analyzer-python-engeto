"""
text_analyzer.py: the first project for Engeto Online Python Academy

author: Oldřich Kruchňa
email: kruchna.o@gmail.com
"""

from contextlib import nullcontext
from numbers import Number


TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

REGISTRED_USERS = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}


username = input("Enter your username: ")
password = input("Enter your password: ")

if username in REGISTRED_USERS and REGISTRED_USERS[username] == password:
    print('User is logged')
    print('----------------------------------------')
    print(f'Welcome to the app, {username}')
else:
    print('Unregistered user, terminating the program.')
    exit()

print(f'We have {len(TEXTS)} texts to be analyzed.')
index = input(f'Enter a number btw. 1 and {len(TEXTS)} to select:')

text_to_analyze_index = None

if index.isdigit():
    text_to_analyze_index = int(index)
    print(f'The inserted value {text_to_analyze_index} is valid')
else:
    print('The input is invalid.')
    exit()

print('----------------------------------------')
print(text_to_analyze_index)