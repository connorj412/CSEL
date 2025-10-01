def main():
    escape = False
    IronKey = False
    BrassKey = False
    mattress = False

    print("You wake up in a dimly lit room. The air smells faintly of dust and old wood.\nThe only visible exit is a heavy iron door with a large lock.\n"
          "Looking around, you notice:\n"
          "- A small wooden chest sitting on a table in the corner\n"
          "- A bare mattress on the floor\n"
          "- A section of the floorboards that looks slightly uneven, almost as if one plank doesn't quite fit.\n")
    while escape == False:
        choice = input("What do you do?\n"
                       "A. Open the heavy iron door.\n"
                       "B. Inspect the wooden chest.\n"
                       "C. Inspect the mattress.\n"
                       "D. Inspect the suspicious plank in the floorboard.\n")
        match choice:
            case "A":
                if IronKey == False and BrassKey == False:
                    print("You tug the handle. It doesn’t budge. The key must be somewhere in this room…")
                elif IronKey == False and BrassKey == True:
                    print("The brass key is too small for the door’s lock. Maybe it opens something else.")
                elif IronKey == True:
                    print("The iron key slides into the lock. You turn it, the mechanism clicks. The door swings open. You’re free!")
                    escape = True
            case "B":
                if IronKey == False and BrassKey == False:
                    print("The chest is locked. The key has to be around here somewhere…")
                elif BrassKey == True and IronKey == False:
                    print("The brass key fits the chest lock. It clicks open. Inside rests a heavier iron key. This one looks it is made for a door.")
                    IronKey = True
                elif IronKey == True and BrassKey == True:
                    print("You check the chest again, nothing else inside")
            case "C":
                if mattress == False:
                    print("You inspect the thin mattress, there is nothing on it. You lift it, there is nothing underneath either.")
                    mattress = True
                elif mattress == True:
                    print("You already checked the mattress. There is nothing there.")
            case "D":
                if BrassKey == False:
                    print("You pry up the loose plank. Hidden in the dust lies a small brass key.")
                    BrassKey = True
                elif BrassKey == True:
                    print("You’ve already pried up the plank. There is nothing else underneath.")
if __name__ == "__main__":
    main()