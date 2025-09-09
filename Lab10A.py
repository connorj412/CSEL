def main():
    class Chair:
        def __init__(self, numOfLegs, rolling, material):
            self.numOfLegs = numOfLegs
            self.rolling = rolling
            self.material = material
        def default(self):
            self.numOfLegs = 4
            self.rolling = False
            self.material = "wood"
    print("You are about to create a chair.")
    numOfLegs = int(input("How many legs does your chair have: "))
    rolling = input("Is your chair rolling (true/false): ")
    if rolling == "true":
        rolling = True
    else:
        rolling = False
    material = input("What is your chair made of: ")
    chair1 = Chair(numOfLegs, rolling, material)
    def chair_desc(a, b, c):
        if b:
            isRolling = "rolling"
        else:
            isRolling = "not rolling"
        print(f"Your chair has {a} legs, is {isRolling}, and is made of {c}.")
    chair_desc(chair1.numOfLegs, chair1.rolling, chair1.material)
    print("This program is going to change that.")
    chair1.default()
    chair_desc(chair1.numOfLegs, chair1.rolling, chair1.material)
if __name__ == "__main__":
    main()
