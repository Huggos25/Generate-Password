import os
import random
import string
import time
import sys

def menu():
    """
    Clear the terminal screen and display the welcome message.

    This function clears the terminal screen and displays a welcome message with the project name and author.

    Args:
        None

    Returns:
        None
    """
    os.system('cls')
    print('################---WELCOME---################')
    print('#------------Password--Generator------------#')
    print('#------------Made-By-Hugo Vieira------------#')
    print('#############################################')

def mecanica(caracteres):
    """
    Generate a random password based on user input.

    This function prompts the user to enter the desired length of the password. If the user presses Enter, the program exits.
    It generates a random password using the specified characters and the given length.

    Args:
        caracteres (str): A string containing the characters from which the password will be generated.

    Returns:
        list: A list containing the characters of the generated password.
    """
    while True:
        try:
            pwdsize_input = input("(Press enter to exit)\n\nHow long is the password?")
            if pwdsize_input == "":
                sys.exit()

            if pwdsize_input.isdigit():
                pwdsize = int(pwdsize_input)
                pwdfinal = random.choices(caracteres, k=pwdsize)
                return pwdfinal
            else:
                print("Insert a numeric number!")
        except ValueError:
            print("Please enter a valid numeric value.")

def main():
    """
    Main function to execute the password generator program.

    This function calls the 'menu()' function to display the welcome message and then enters a loop where it generates passwords and gives the user the option to save them to a file.

    Args:
        None

    Returns:
        None
    """
    menu()

    while True:
        caracteres = string.ascii_letters + string.digits
        pwdfinal = mecanica(caracteres)

        salvar = input("Save Password Press(ENTER)!")
        if salvar.upper() == "":
            with open("password.txt", "a") as arquivo:
                arquivo.write("\n")
                arquivo.write("######################\n")
                arquivo.write("#GENERATED PASSWORDS#\n")
                arquivo.write("######################\n")
                arquivo.write("\n------------------------\n")
                arquivo.write("Password: ")
                arquivo.write("".join(pwdfinal))
                arquivo.write("\n\n")
                arquivo.write(str(time.ctime()))
                arquivo.write("\n------------------------\n")
                print("Password saved in file 'password.txt")

if __name__ == "__main__":
    main()
