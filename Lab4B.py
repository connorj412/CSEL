def main():
    print("Welcome!")
    number = float(input("Please input a number: "))
    selection = int(input('What would you like to do with this number: '
                          '\n0) Get the additive inverse of this number'
                          '\n1) Get the reciprocal of this number'
                          '\n2) Square the number'
                          '\n3) Cube the number'
                          '\n4) Exit the program\n'))
    match selection:
        case 0: print(f"The additive inverse of {number} is {round(0 - number, 3)}")
        case 1:
            match number:
                case 0: print("Cannot divide by 0!")
                case _: print(f"The reciprocal on {number} is {round(1 / number, 3)}")

        case 2: print(f"The square of {number} is {round(number ** 2, 3)}")
        case 3: print(f"The cube of {number} is {round(number ** 3, 3)}")
        case 4: print("Thank you, goodbye!")
        case _: print('Invalid option!')
if __name__ == "__main__":
    main()