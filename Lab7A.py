def main():
    def isValid(width, height):
        return (width + height) > 30
    def area(width, height):
        return width * height
    def perimeter(width, height):
        return (width * 2) + (height * 2)
    choice = "Y"
    while choice == "Y":
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))
        if isValid(width, height):
            print("This is a valid rectangle.")
            print(f"The area is: {area(width, height)} ")
            print(f"The perimeter is: {perimeter(width, height)}")
        else:
            print("This is an invalid rectangle.")
        choice = input("Do you want to enter another width and height (Y/N)?: ")

if __name__ == "__main__":
    main()
