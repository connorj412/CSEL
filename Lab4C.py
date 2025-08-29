def main():
    side1 = int(input("Enter the first side of the triangle: "))
    side2 = int(input("Enter the second side of the triangle: "))
    side3 = int(input("Enter the third side of the triangle: "))
    if side1 > 0 and side2 > 0 and side3 > 0:
        if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
            print("The sides do not form a valid triangle.")
        elif side1 == side2 and side1 == side3:
            print("The triangle is an equilateral triangle.")
        elif side1 == side2 or side1 == side3 or side2 == side3:
            print("The triangle is an isosceles triangle.")
        else:
            print("The triangle is a scalene triangle.")
    else:
        print("Invalid input. All sides must be greater than 0.")

if __name__ == "__main__":
    main()