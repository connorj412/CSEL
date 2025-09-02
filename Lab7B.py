def main():
    from MyMath import my_max, my_min, my_avg
    number1 = int(input("Enter number 1: "))
    number2 = int(input("Enter number 2: "))
    print(f"Min is {my_min(number1, number2)}")
    print(f"Max is {my_max(number1, number2)}")
    print(f"Average is {my_avg(number1, number2)}")
if __name__ == "__main__":
    main()