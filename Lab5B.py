def main():
    size = int(input("Please enter a value for the size: "))
    print(f"This is the requested right-facing {size}x{size} right-triangle:")
    for h in range(size):
        for w in range(size):
            print("*", end="")
        print()
    print(f"This is the requested right-facing {size}x{size} right triangle:")
    for h in range(size):
        for i in range(h + 1):
            print("*", end="")
        print()
    print(f"This is the requested left-facing {size}x{size} right triangle:")
    for h in range(size):
        for i in range(size - h - 1):
            print(" ", end="")
        for i in range(h + 1):
            print("*", end="")
        print()
if __name__ == '__main__':
    main()