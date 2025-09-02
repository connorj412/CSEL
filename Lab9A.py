def main():
    def allMath(a, b):
        number1 = a + b
        number2 = a - b
        number3 = a * b
        if b == 0:
            number4 = None
            number5 = None
            number6 = None
        else:
            number4 = a / b
            number5 = a // b
            number6 = a % b
        number7 = a ** b
        return number1, number2, number3, number4, number5, number6, number7
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    print(f"Your resulting tuple is {allMath(a, b)}")
if __name__ == "__main__":
    main()