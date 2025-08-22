Hours1 = int(input("Course 1 hours: "))
Grade1 = int(input("Grade for course 1: "))
Hours2 = int(input("Course 2 hours: "))
Grade2 = int(input("Grade for course 2: "))
Hours3 = int(input("Course 3 hours: "))
Grade3 = int(input("Grade for course 3: "))
Hours4 = int(input("Course 4 hours: "))
Grade4 = int(input("Grade for course 4: "))
TotalHours = Hours1 + Hours2 + Hours3 + Hours4
TotalQualityPoints = (Hours1 * Grade1) + (Hours2 * Grade2) + (Hours3 * Grade3) + (Hours4 * Grade4)
GPA = TotalQualityPoints / TotalHours
print(f"Total Hours: {TotalHours}")
print(f"Total Quality Points: {TotalQualityPoints}")
print(f"Your GPA for this semester is: {round(GPA, 8)}")
