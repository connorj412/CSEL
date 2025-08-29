def main():
    grade = float(input("Enter the number grade you received on an exam: "))
    if grade > 97:
        letter_grade = "A+"
    elif grade > 94:
        letter_grade = "A"
    elif grade > 91:
        letter_grade = "A-"
    elif grade > 88:
        letter_grade = "B+"
    elif grade > 85:
        letter_grade = "B"
    elif grade > 82:
        letter_grade = "B-"
    elif grade > 79:
        letter_grade = "C+"
    elif grade > 76:
        letter_grade = "C"
    elif grade > 73:
        letter_grade = "C-"
    elif grade > 70:
        letter_grade = "D+"
    elif grade > 67:
        letter_grade = "D"
    elif grade > 64:
        letter_grade = "D-"
    elif grade <= 64 and grade >= 0:
        letter_grade = "F"
    else:
        letter_grade = "Invalid"
    print(f"Letter Grade is: {letter_grade}")
if __name__ == "__main__":
    main()