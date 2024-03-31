print("Welcome to cryptography")
def main():
    while True:
        print("Choose one option below")
        choice = int(input("1. Encryption\n2. Decryption\n choose(1,2): "))
        if choice == 1:
            encryption()
        elif choice == 2:
            decryption()
        else:
            print("wrong choice")
            break

def encryption():
    msg = input("enter your message: ")
    key = int(input("Enter key (1-94): "))
    text=""
    for i in range(len(msg)):
        temp = ord(msg[i]) + key
        if temp  > 126:
            temp = temp-127+32
        print(temp)
        text += chr(temp)
        print("Encrypted Text: ", text)

def decryption():
    print("Decryption")

    encryption_msg = input("Enter the encrypted message: ")
    decrp_key = int(input("Enter the key (1-94): "))
    decrypted_text = ""

    for i in range(len(encryption_msg)):
        temp = ord(encryption_msg[i]) - decrp_key
        if (temp<32):
            temp = temp+127-32
        decrypted_text += chr(temp)
    print("Decrypted Text: ",decrypted_text)


if __name__ == "__main__":
    main()