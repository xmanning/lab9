# i cloned the repo to make this comment
# pretend this was a partner

def print_menu():
    print("""Menu
------------
1. Encode
2. Decode
3. Quit
""")

def encode(password):
    encoded = ""
    for char in [*password]:
        encoded += str((int(char) + 10 + 3) % 10)

    return encoded


def decode(password):
    decoded = ""
    for char in [*password]:
        decoded += str((int(char) + 10 - 3) % 10)
    return decoded


def main():
    password = ""
    choice = 0
    while choice != 3:
        print_menu()
        choice = int(input("Please enter an option: "))
        if choice == 1:
            inPassword = input("Please enter your password to encode: ")
            password = encode(inPassword)
            print("Your password has been encoded and stored!")
            print()
        elif choice == 2:
            outPassword = decode(password)
            print(f"The encoded password is {password}, and the original password is {outPassword}")
            print()
        elif choice == 3:
            continue





if __name__ == "__main__":
    main()
