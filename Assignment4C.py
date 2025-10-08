def main():
    def validate(message, offset):
        isValid = False
        if offset < 1 or offset > 26:
            return False
        else:
            for x in message:
                if x.isalpha() == False:
                    if x == " ":
                        isValid = True
                    else:
                        return False
                else:
                    isValid = True
        return isValid

    def encrypt(message, offset):
        encryptedMessage = ""
        message = message.upper()
        for l in message:
            if l != " ":
                char = ord(l)
                for x in range(offset):
                    if (char + 1) > 90:
                        char = 65
                    else:
                        char = char + 1
                char = chr(char)
                encryptedMessage = encryptedMessage + char
            else:
                encryptedMessage = encryptedMessage + l
        return encryptedMessage

    choice = "Y"
    while choice == "Y":
        message = input("Enter your message:\n")
        offset = int(input("Enter the offset value: "))
        valid = validate(message, offset)
        if not valid:
            print("\nSorry, we can only process messages with letters and spaces, and the offset must be between 0 and 26.")
        else:
            newMessage = encrypt(message, offset)
            print(f"\nYour secret message is..."
                  f"\n{newMessage}")
        choice = input("\nDo you want to encrypt another message? (Y/N): ")

    print("\nClosing out...")
if __name__ == "__main__":
    main()