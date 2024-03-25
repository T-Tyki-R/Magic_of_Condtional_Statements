# Leap Year Checker
print("Please enter a number: ")
userYear = int(input())

if userYear % 4 == 0 and userYear % 400 == 0 or userYear % 100 != 0:
    print(str(userYear) + " is considered a leap year")
else:
    print(str(userYear) + " isn't considered a leap year")