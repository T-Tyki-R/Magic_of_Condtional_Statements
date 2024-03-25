# The Greatest Showdown
print("Hello, user! Please enter 3 different numbers")
num1 = int(input(""))
num2 = int(input(""))
num3 = int(input(""))

if num1 > num2 and num1 > num3:
    print((str(num1)) + " is the highest number!")
elif num2 > num3 and num2 > num1:
    print((str(num2)) + " is the highest number!")
else:
    print((str(num3)) + " is the highest number!")

if num1 < num2 and num1 < num3:
    print((str(num1)) + " is the lowest number!")
elif num2 < num3 and num2 < num1:
    print((str(num2)) + " is the lowest number!")
else:
    print((str(num3)) + " is the lowest number!")

if num1 == num2:
    print((str(num1)) + " and " + str(num2) + " are the same!")
elif num1 == num3:
    print((str(num1)) + " and " + str(num3) + " are the same!")
else:
    print((str(num2)) + " and " + str(num3) + " are the same!")
 
