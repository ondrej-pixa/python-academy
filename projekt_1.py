"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Ondrej Pixa
email: ondrej.pixa@gmail.com
discord: ondra_32
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
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

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}

print("username:", end="")
username = input()
print("password:", end="")
password = input()

is_registered = (username in users) and (users[username] == password)

if not is_registered:
    print("unregistered user, terminating the program..")
    exit()

welcome_text = '''----------------------------------------
Welcome to the app, bob
We have 3 texts to be analyzed.
----------------------------------------
'''
print(welcome_text, end="")

print("Enter a number btw. 1 and 3 to select: ", end="")
number_str = input()
if not number_str.isdigit():
    print("Not a number, terminating the program..")
    exit()

number = int(number_str)
if not (1 <= number <= 3):
    print("Number must be btw. 1 and 3, terminating the program..")
    exit()

print("----------------------------------------")

text = TEXTS[number - 1]
words = text.split()

words_count = len(words)
titlecase_words_count = 0
uppercase_words_count = 0
lowercase_words_count = 0
numeric_strings_count = 0
sum_of_numbers = 0
frequency = {}
max_length = 0

for word in words:
    word = word.replace(',', '')
    word = word.replace('.', '')

    if word.istitle():
        titlecase_words_count += 1
    if word.isupper() and word.isalpha():
        uppercase_words_count += 1
    if word.islower():
        lowercase_words_count += 1
    if word.isdigit():
        numeric_strings_count += 1
        sum_of_numbers += int(word)

    length = len(word)
    frequency[length] = frequency.get(length, 0) + 1
    if length > max_length:
        max_length=length


print(f"There are {words_count} words in the selected text.")
print(f"There are {titlecase_words_count} titlecase words.")
print(f"There are {uppercase_words_count} uppercase words.")
print(f"There are {lowercase_words_count} lowercase words.")
print(f"There are {numeric_strings_count} numeric strings.")
print(f"The sum of all the numbers {sum_of_numbers}")

header = '''----------------------------------------
LEN|  OCCURENCES  |NR.
----------------------------------------'''

print(header)

for length in range(1,max_length+1):
    f = frequency.get(length, 0)
    print(length,"|","*"*f,"|",f)
