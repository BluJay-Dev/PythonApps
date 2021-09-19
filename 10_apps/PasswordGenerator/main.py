""""
Password checker / Generator
Author: BluJay-Dev
User will input a password and the programme will let them know if it fits the criteria.
"""
import random
import string

import string_utils


def length_checker(password):
    if len(password) <= 12:
        print("This password isn't strong enough")
        exit()

    else:
        print("This password is long enough")


def capital_checker(password):
    count = sum(1 for c in password if not c.isupper())
    if count < 4:
        print("Not enough capitals, need at least four")
        exit()

    else:
        print("Enough capital letters")


def special_character(password):
    count = sum(1 for c in password if not c.isalpha())
    if count <= 2:
        print("Not enough special characters")

    else:
        print("This password has passed")


def generator():
    letters = string.ascii_uppercase + string.digits + string.punctuation
    result_str = ''.join(random.choice(letters) for i in range(12))
    print(f"Your password is:  '{result_str}'")


option = input("1 to enter a password 2 to generate one \n")

if option == "1":
    user_pass = input("Please enter your password: ")
    length_checker(password=user_pass)
    capital_checker(password=user_pass)
    special_character(password=user_pass)

elif option == "2":
    generator()

else:
    exit()
