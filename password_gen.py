import os
import random
import string
import sys
import time

def menu():
    #Display the welcome message.

    os.system('cls' if os.name == 'nt' else 'clear')
    print('################---WELCOME---################')
    print('#------------Password Generator-------------#')
    print('#------------Made-By-Hugo Vieira------------#')
    print('#--------------Fork-By-0xZ1R0---------------#')
    print('#############################################')

def generate_password(available_chars, password_length):
    #Generate a random password.
    return random.choices(available_chars, k=password_length)

def save_password(password):
    #Save the password to a file.

    timestamp = time.ctime()
    try:
        with open("password.txt", "a") as arquivo:
            arquivo.write("######################\n")
            arquivo.write("# GENERATED PASSWORD #\n")
            arquivo.write("######################\n")
            arquivo.write(f"Password: {password}\n")
            arquivo.write(f"Generated on: {timestamp}\n")
            arquivo.write("------------------------\n")
        print("Password saved in file 'password.txt'.")
    except IOError:
        print("Error: Could not write to file.")

def main():

    menu()

    base_chars = string.ascii_letters + string.digits
    include_special_chars = input("Include special characters? (Y/N): ").upper()
    if include_special_chars == "Y":
        available_chars = base_chars + string.punctuation
    else:
        available_chars = base_chars

    while True:
        password_length_input = input("(Press enter to exit)\n\nHow long is the password? ")
        if password_length_input == "":
            sys.exit()
        if not password_length_input.isdigit():
            print("Please enter a valid numeric value!")
            continue
        password_length = int(password_length_input)
        password = generate_password(available_chars, password_length)
        print(f"Generated Password: {''.join(password)}")

        save_choice = input("Save Password? (Y/N): ").upper()
        if save_choice == "Y":
            save_password("".join(password))

        another_password = input("Generate another password? (Y/N): ").upper()
        if another_password != "Y":
            break

if __name__ == "__main__":
    main()
