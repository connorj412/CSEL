def main():
    user_input = 1
    while user_input != 0:
        user_input = int(input("Enter Number for Rows or 0 to quit: "))
        for x in range(1, user_input + 1):
            space = user_input - x
            for i in range(space):
                print(" ", end="")
            for i in range(x, 0, -1):
                print(i, end="")
            for i in range(2, x + 1):
                print(i, end="")
            print()
if __name__ == "__main__":
    main()