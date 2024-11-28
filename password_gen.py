import os
import random
import string
import sys
import time

def clear():
    #Clear the terminal screen.
    os.system('cls' if os.name == 'nt' else 'clear')

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
    input("Press Enter to start...")
    clear()

    base_chars = string.ascii_letters + string.digits

    while True:
        # Ask to include special characters
        clear()
        include_special_chars = input("Include special characters? (Y/N): ").upper()
        if include_special_chars == "Y":
            available_chars = base_chars + string.punctuation
        else:
            available_chars = base_chars

        # Ask for password length
        clear()
        password_length_input = input("How long is the password? ")
        if not password_length_input.isdigit():
            print("Please enter a valid numeric value!")
            continue
        password_length = int(password_length_input)

        # Generate and display password
        clear()
        password = generate_password(available_chars, password_length)
        print(f"Generated Password: {''.join(password)}")
        input("Press Enter to proceed...")

        # Ask to save password
        clear()
        save_choice = input("Save Password? (Y/N): ").upper()
        if save_choice == "Y":
            save_password("".join(password))
            input("Press Enter to proceed...")

        # Ask to generate another password
        clear()
        another_password = input("Generate another password? (Y/N): ").upper()
        if another_password != "Y":
            break

if __name__ == "__main__":
    main()
