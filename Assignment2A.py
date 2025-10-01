def main():
    print("[Welcome to OwlBanking]")
    choice = "0"
    balance = 0
    history = ""
    while choice != "Q":
        choice = input("Select an option:\n"
                       "1 - Deposit\n"
                       "2 - Withdraw\n"
                       "3 - Check Balance\n"
                       "4 - Check Transaction History\n"
                       "Q - Quit\n")
        match choice:
            case "1":
                deposit = float(input("How much do you want to deposit: $"))
                new_balance = balance + deposit
                history = history + f"\n${deposit} was deposited, balance went from ${balance} to ${new_balance}"
                balance = new_balance
            case "2":
                if balance == 0:
                    print("Error: Cannot Withdraw with balance of zero")
                else:
                    withdraw = float(input("How much do you want to withdraw: $"))
                    if withdraw <= balance:
                        new_balance = balance - withdraw
                        history = history + f"\n${withdraw} was withdrawn, balance went from ${balance} to ${new_balance}"
                        balance = new_balance
                    else:
                        print("Error: Cannot Withdraw a larger amount than balance")
            case "3":
                print(f"Balance: ${balance}")
            case "4":
                print(history)
if __name__ == "__main__":
    main()