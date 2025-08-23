print("[Electrical Energy Consumption Calculator]")
Voltage = float(input("Enter the voltage (in volts): "))
Resistance = float(input("Enter the resistance (in ohms): "))
Time = float(input("Enter the time the device was used (in hours): "))
CONVERSION_FACTOR = 1000
Energy = ((Voltage ** 2) * Time) / (Resistance * CONVERSION_FACTOR)
print(f"The device consumed {round(Energy, 2)} kWh of energy.")