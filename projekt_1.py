"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Ondrej Pixa
email: ondrej.pixa@gmail.com
discord: ondra_32
"""

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
