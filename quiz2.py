#Greg Phillips
#9/25/17
#quiz2.py

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a 2nd number: "))

if num1==num2:
    print("The numbers are the same")
elif num1>num2:
    print("The first number is bigger")
else:
    print("The second number is bigger")
if num1%3==0 and num2%3==0:
    print("Both numbers are divisible by 3")
elif num1%3==0:
    print("Only the first number is divisible by 3")
elif num2%3==0:
    print("Only the second number is divisible by 3")
else:
    print("Neither of the numbers are divisible by 3")
    
print("What is the product of your two numbers:")
product = int(input(""))

if num1*num2==product:
    print("Correct")
else:
    print("Incorrect")

    