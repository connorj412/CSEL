def main():
    print("[friend List]")
    choice = 0
    friend = []
    while choice != 3:
        choice = int(input("1 - Add friend\n"
                           "2 - List friends\n"
                           "3 - Quit\n"
                           "Make your selection: "))
        match choice:
            case 1:
                name = input("Enter your friend's name: ")
                age = int(input("enter your friend's age: "))
                tup = (name, age)
                friend.append(tup)
            case 2:
                for x in friend:
                    print(f"Name: {x[0]}, Age: {x[1]}")
    print("Shutting down...")
if __name__ == "__main__":
    main()