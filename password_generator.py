import random
import string
length = int(input("Enter password length: "))
letters = input("Include letters? (y/n): ")
numbers = input("Include numbers? (y/n): ")
special = input("Include special characters? (y/n): ")
if letters == "y" and numbers == "y" and special == "y":
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choices(characters, k=length))
    print(f"Generate password: {password}")
elif letters == "y" and numbers == "y" and special == "n":
    characters = string.ascii_letters + string.digits
    password = "".join(random.choices(characters, k=length))
    print(f"Generate password: {password}")
elif letters == "n" and numbers == "y" and special == "y":
    characters = string.digits + string.punctuation
    password = "".join(random.choices(characters, k=length))
    print(f"Generate password: {password}")
elif letters == "y" and numbers == "n" and special == "y":
    characters = string.ascii_letters + string.punctuation
    password = "".join(random.choices(characters, k=length))
    print(f"Generate password: {password}")
elif letters == "n" and numbers == "y" and special == "n":
    characters = string.digits
    password = "".join(random.choices(characters, k=length))
    print(f"Generate password: {password}")
elif letters == "y" and numbers == "n" and special == "n":
    characters = string.ascii_letters
    password = "".join(random.choices(characters, k=length))
    print(f"Generate password: {password}")
elif letters == "n" and numbers == "n" and special == "y":
    characters = string.punctuation
    password = "".join(random.choices(characters, k=length))
    print(f"Generate password: {password}")
else:
    print("Please input valid answers")
