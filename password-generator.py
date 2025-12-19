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

    count = int(input("How many passwords to generate: "))
    choice = input("Save passwords to a text file? (y/n): ")
    if choice == 'y' or choice == 'Y':
        file_path = input("Enter file path: ")
        passwords_generated = 1
        while passwords_generated <= count:
            password = "".join(random.choices(characters, k=length))
            print(f"{password}")
            with open(file_path, 'a') as file:
                file.write(password + "\n")
            passwords_generated += 1
        print(f"Passwords added to {file_path}")
    else:
        passwords_generated = 1
        while passwords_generated <= count:
            password = "".join(random.choices(characters, k=length))
            print(f"{password}")
            passwords_generated += 1
except IndexError:
    print("Without any characters, I cannot generate a password")
