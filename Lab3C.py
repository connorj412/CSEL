SmallSandwich = int(input("Enter the number of small sandwiches: "))
MediumSandwich = int(input("Enter the number of medium sandwiches: "))
LargeSandwich = int(input("Enter the number of large sandwiches: "))
ExtraLargeSandwich = int(input("Enter the number of extra large sandwiches: "))
print(" ")
print(f"You've entered {SmallSandwich} small sandwiches")
print(f"You've entered {MediumSandwich} medium sandwiches")
print(f"You've entered {LargeSandwich} large sandwiches")
print(f"You've entered {ExtraLargeSandwich} extra large sandwiches")
print(" ")
TotalCookTimeSeconds = (SmallSandwich * 30) + (MediumSandwich * 60) + (LargeSandwich * 75) + (ExtraLargeSandwich * 135)
Minutes = TotalCookTimeSeconds // 60
Seconds = TotalCookTimeSeconds % 60
print(f"Total cooking time is {Minutes} minutes and {Seconds} seconds")