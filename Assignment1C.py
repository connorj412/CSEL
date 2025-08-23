print("[Weight Conversion- Kilograms to Stones and Pounds]")
Kilograms = float(input("Enter weight in kilograms: "))
Pounds = Kilograms * 2.20462
Stones = Pounds // 14
RemainingPounds = Pounds % 14

print(f"{int(Kilograms)} kilograms in approximately {Stones} stones and {round(RemainingPounds, 2)} pounds.")