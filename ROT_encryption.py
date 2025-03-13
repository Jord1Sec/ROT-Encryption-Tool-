#interface
def main():
    while True:
        print("\nENCRYPTION THROUGH ROTATION PROGRAM\n")
        print("[+] 1. Encryption")
        print("[+] 2. Decryption")
        print("\n[-] x. Exit")
        choice = input("[?] What would you like to do today?: ")
        #logic
        if choice == "1":
            plaintext = input("\n[+] Please input what you would like to encrypt: ")
            rotation = int(input("How many characters would you like to rotate?: "))
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            for char in plaintext.lower():
                index = alphabet.find(char)
                new_index = (index + rotation) % 26
                new_char = alphabet[new_index]
                print(new_char, end="")
        elif choice == "2":
            plaintext = input("\n[+] Please input what you would like to decrypt: ")
            rotation = int(input("How many characters would you like to rotate?: "))
            rotation = -(rotation)
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            for char in plaintext.lower():
                index = alphabet.find(char)
                new_index = (index + rotation) % 26
                new_char = alphabet[new_index]
                print(new_char, end="")
        elif choice == "x":
            break
        else:
            print("\nPlease enter a valid input!")

main()