def main():
    temp = ""
    average = 0.0
    total = 0

    all_temperatures = input("Enter temperatures in F (separate them with ,): ") + ","

    for x in all_temperatures:
        if x != ",":
            temp = temp + x
        elif x == ",":
            temp = float(temp)
            average = average + temp
            total += 1
            temp = ""

    temp_average = average / total
    temp_average = round(temp_average, 2)

    print(f"You've entered {total} temperature points.")
    print(f"The average temperature is {temp_average}F")
if __name__ == "__main__":
    main()