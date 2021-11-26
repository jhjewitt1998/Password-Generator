"""
Coded by: Jacob Jewitt
Last updated: 26/11/2021
Version: 1.0

A rudimentary program which will create a random password for the user to meet their needs. It will ask the user what
they want from a password, then create it. It will then be written to a text file for future use. This could be expanded
on so that a user can create multiple passwords in a single setting, instead of relaunching the code.

"""

import string
import random

# putting all ASCII chars, numbers and special chars into lists so password generator can use them later
ASCII_chars_lower = list(string.ascii_lowercase)
ASCII_chars_upper = list(string.ascii_uppercase)
numbers = list(string.digits)
special_chars = list("!£$%^&*@<>?#~")


def random_password_generator():
    print("Welcome to the password generator. This generator will ask you to specify the amount of upper and "
          "lower case characters as well as any numbers and special characters for your password. It will then "
          "generate an output and save it to a txt file")

    # loop used so if exception is detected, it will then restart the process
    while True:
        try:
            # asks the user to input how many certain cases they'd like
            lower_cases = int(input("How many lower case letters?: "))
            upper_cases = int(input("How many upper case letters?: "))
            number_cases = int(input("How many numbers?: "))
            special_char_cases = int(input("How many special characters?: "))

            password = []

            # get x amount of each specified case from lists containing the relevant information
            for i in range(lower_cases):
                password.append(random.choice(ASCII_chars_lower))

            for i in range(upper_cases):
                password.append(random.choice(ASCII_chars_upper))

            for i in range(number_cases):
                password.append(random.choice(numbers))

            for i in range(special_char_cases):
                password.append(random.choice(special_chars))

            # shuffle the password to make it more secure, then change into string for file compatibility
            random.shuffle(password)
            # uncomment print statement below to allow printing to console
            # print(''.join(password))
            password_to_string = ''.join(password)

            # open/create file "Passwords.txt" then save the password to it for future use
            lines = ["Generated Password(s)", password_to_string]
            with open("Passwords.txt", "w") as file:
                for line in lines:
                    file.write(line)
                    file.write("\n")

            break

        except ValueError:
            # if user enters invalid cases such as a string, will present this exception
            print("Entry not valid, please use digits not letters.")


if __name__ == '__main__':
    random_password_generator()
