def main():
    pattern = ""
    print("[Pyramid Pattern]")
    user_string = input("Enter a string: ")
    for x in user_string:
        if x != " ":
            pattern = pattern + x
            print(pattern)
if __name__ == "__main__":
    main()