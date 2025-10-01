def main():
    #chair class
    class Chair:
        def __init__(self, numOfLegs, rolling, material):
            self.numOfLegs = numOfLegs
            self.rolling = rolling
            self.material = material
        #default chair
        def default(self):
            self.numOfLegs = 4
            self.rolling = False
            self.material = "wood"

    #creating the chair
    print("You are about to create a chair.")
    numOfLegs = int(input("How many legs does your chair have: "))
    rolling = input("Is your chair rolling (true/false): ").lower()
    if rolling == "true": #changes string input to boolean value
        rolling = True
    else:
        rolling = False
    material = input("What is your chair made of: ")
    chair1 = Chair(numOfLegs, rolling, material)

    #printing the chair description
    def chair_desc(a, b, c):
        if b:
            isRolling = ""
        else:
            isRolling = "not"
        print(f"Your chair has {a} legs, is {isRolling} rolling, and is made of {c}.")

    chair_desc(chair1.numOfLegs, chair1.rolling, chair1.material) #this runs the chair_desc function
    print("This program is going to change that.")
    chair1.default() #this changes the chair properties to the default
    chair_desc(chair1.numOfLegs, chair1.rolling, chair1.material) #this runs the chair_desc function again with the updated properties
if __name__ == "__main__":
    main()
