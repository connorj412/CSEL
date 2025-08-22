CurrentBalance = float(input("Amount owed: $"))
AnnualPercentageRate = float(input("APR: "))
MonthlyPercentageRate = AnnualPercentageRate / 12
MinimumPayment = CurrentBalance * (MonthlyPercentageRate / 100)
print(f"Monthly percentage rate: {round(MonthlyPercentageRate,3)}")
print(f"Minimum payment: ${round(MinimumPayment, 2)}")