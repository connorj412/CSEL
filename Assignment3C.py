def main():
    print("[Welcome to the Letter Frequency Quiz]")
    sentence = input("Enter a sentence (lowercase letters only): ")
    letters = ""
    checked_letters = ""
    complete = False
    number_letter = 0
    for l in sentence:
        if l != " ":
            if l in checked_letters:
                duplicate = True
            else:
                duplicate = False
            if not duplicate:
                letters += l
            checked_letters += l
    while not complete:
        correct_guess = False
        while not correct_guess:
            frequency = 0
            for l in sentence:
                if l == letters[number_letter]:
                    frequency += 1
            guess = int(input(f"Guess the frequency of letter '{letters[number_letter]}': "))
            if guess == frequency:
                correct_guess = True
                number_letter += 1
                print("Correct!")
            else:
                if guess > frequency:
                    print("Too High!")
                else:
                    print("Too Low!")
        if number_letter == len(letters):
            complete = True
    print("Congratulations! You completed the quiz.")
if __name__ == "__main__":
    main()