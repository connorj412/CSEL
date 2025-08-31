def main():
    highest_number = 0
    for x in range(10):
        user_number = int(input(f"Please enter number {x + 1}: "))
        if user_number > highest_number:
            highest_number = user_number
    print()
    print(f"The largest number was {highest_number}")
if __name__ == '__main__':
    main()