def main():
    choice = 0
    print("Multiplication and Exponent Calculator")
    while choice != 3:
        choice = int(input("Choose option 1 for Multiplication\nChoose option 2 for Exponentiation\nChoose option 3 to Exit\n"))
        print()
        match choice:
            case 1:
                operand1 = int(input("Enter the operand: "))
                operand2 = int(input("Enter the operand: "))
                answer = 0
                for x in range(operand1):
                    answer += operand2
                print(f"{operand1} x {operand2} = {answer}")
            case 2:
                base = int(input("Enter the base: "))
                exponent = int(input("Enter the exponent: "))
                answer = base
                base_inc = base
                for x in range(exponent - 1):
                    for i in range(base - 1):
                        answer += base_inc
                    base_inc = answer
                print(f"{base}^({exponent}) = {answer}")

            case 3:
                print("Closing the Calculator")
            case _:
                print("Invalid Choice")

if __name__ == '__main__':
        main()