from operator import truediv


def main():
    print("[Sum of Unique Products and Pairs]")
    user_number = int(input("Enter a number: "))
    total = 0

    for i in range(1, user_number + 1):
        for j in range(1, user_number + 1):
            ij_product = i * j
            counted = False

            for a in range(1, i + 1):
                for b in range(1, user_number + 1):
                    if (a < i) or (a == i and b < j):
                        if a * b == ij_product:
                            counted = True
                            break
                if counted:
                    break
            if not counted:
                total += ij_product
                duplicate = ""
            else:
                duplicate = "(duplicate, ignore)"

            print(f"({i},{j})={ij_product} {duplicate}")
    print(f"Sum of unique products: {total}")
if __name__ == "__main__":
    main()