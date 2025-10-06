def main():
    def printMenu():
        print("\n1. Espresso - $3.00"
              "\n2. Latte - $4.00"
              "\n3. Cappuccino - $4.00"
              "\n4. Tea - $2.00"
              "\n5. Exit and Checkout")

    def getChoice(userInput):
        if userInput == 0 or userInput >= 6:
            return userInput
        else:
            return -1

    def processOrder(userInput):
        total = 0
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
                price = 5
            case 4:
                item = "Tea"
                price = 2
            case 5:

            case _:
                print("Invalid choice, please select one of options displayed.")
        if userInput == 1 or userInput == 2 or userInput == 3 or userInput == 4:
            quantity =int(input(f"How many {item}(s) would you like? "))
            total = quantity * price
            print(f"Added {quantity} {item}(s) - ${total}.00")
        return total

    def getTotal(subTotal):


if __name__ == '__main__':
    main()