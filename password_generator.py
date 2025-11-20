import random
import string

try:
    characters_list = []
    length = int(input("Enter password length: "))
    upper = input("Include uppercase letters? (y/n): ")
    if upper == "y" or upper == "Y":
        characters_list.append(string.ascii_uppercase)
    lower = input("Include lowercase letters? (y/n): ")
    if lower == "y" or lower == "Y":
        characters_list.append(string.ascii_lowercase)
    numbers = input("Include numbers? (y/n): ")
    if numbers == "y" or numbers == "Y":
        characters_list.append(string.digits)
    special = input("Include special characters? (y/n): ")
    if special == "y" or special == "Y":
        characters_list.append(string.punctuation)
    characters = "".join(characters_list)
    password = "".join(random.choices(characters, k=length))
    print(f"Generate password: {password}")
except IndexError:
    print("Without any characters, I cannot generate a password")
