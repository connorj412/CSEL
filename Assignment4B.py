def main():
    def printMenu():
        print("\n1. Espresso - $3.00"
              "\n2. Latte - $4.00"
              "\n3. Cappuccino - $4.00"
              "\n4. Tea - $2.00"
              "\n5. Exit and Checkout")

    def getChoice(userInput):
        if userInput <= 0 or userInput >= 6:
            return -1
        else:
            return userInput

    def processOrder(userInput):
        subTotal = 0
        price = 0

        match userInput:
            case 1:
                item = "Espresso"
                price = 3
            case 2:
                item = "Latte"
                price = 4
            case 3:
                item = "Cappuccino"
                price = 4
            case 4:
                item = "Tea"
                price = 2

            case _:
                print("\nInvalid choice, please select one of options displayed.")
        if userInput == 1 or userInput == 2 or userInput == 3 or userInput == 4:
            quantity =int(input(f"How many {item}(s) would you like? "))
            subTotal = quantity * price
            print(f"Added {quantity} {item}(s) - ${subTotal:.2f}")
        return subTotal

    def getTotal(subTotal):
        if subTotal > 0:
            subTotal = float(subTotal)
            tax = subTotal * 0.06
            total = subTotal + tax
            print(f"\nSubtotal: ${subTotal:.2f}"
                  f"\nTax (6%): ${tax:.2f}"
                  f"\nTotal: ${total:.2f}")

    userInput = 0
    subTotal = 0
    while userInput != 5:
        printMenu()
        userInput = int(input("> "))

        userInput = getChoice(userInput)
        if userInput != 5:
            subTotal = subTotal + processOrder(userInput)

    getTotal(subTotal)
    print("[Program Terminated]")

if __name__ == '__main__':
    main()