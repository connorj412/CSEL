def main():
    import random
    random_number = random.randint(1, 100)
    user_number = 0
    print("Guess the number I am thinking!")
    while random_number != user_number:
        user_number = int(input("Enter any number between 1 and 100: "))
        if user_number > random_number:
            print("Too High!")
        elif user_number < random_number:
            print("Too Low!")
    print(f"Correct! I was thinking of {random_number}")
if __name__ == "__main__":
    main()