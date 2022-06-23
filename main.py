import time
from random import randrange
from first_names import first_name_list
from last_names import last_name_list
from mail_extensions import extension_list
from password_wordlist import password_list

import pyautogui
import selenium


# This is a simple email and password generator. Ideally this would be paired with Pyautogui
# or with a Selenium Webdriver in order to spam the websites of scammers with fake email addresses and passwords.

# A simple function to generate a random character to make emails look more unique
def get_extra_char(random_number_between_0_and_3):
    if random_number_between_0_and_3 == 0:
        extra_element = "-"
    elif random_number_between_0_and_3 == 1:
        extra_element = "."
    elif random_number_between_0_and_3 == 2:
        extra_element = "_"
    elif random_number_between_0_and_3 == 3:
        extra_element = ""
    return extra_element


while True:
    first_name = first_name_list[randrange(0, 2000)].lower().strip()  # generates random firstname
    last_name = last_name_list[randrange(0, 998)].lower().strip()  # generates random lastname
    extra_char = get_extra_char(randrange(0, 4))  # generates random character, calls function above

    # putting the names together
    email = f'{first_name}{extra_char}{last_name}{randrange(0, 998)}{extension_list[randrange(0, 6)]}'

    # Generates a random password from the passwordlist
    password = f"{password_list[randrange(0, 1185)].title()}{randrange(0, 999)}"

    print(email, password, sep='   ')

    # Insert code here using pyautogui or selenium to write to a website.
    # Make sure your vpn is up!

    time.sleep(.5)
