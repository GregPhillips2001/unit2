#Greg Phillips
#9/14/17
#compoundConditionalDemo.py - and/or

num = float(input("Enter a number: "))

if(num>0 and num%7 == 0):
    print("Your number is positive and divisible by 7")
#num%7 == 0 is testing to see if number is divisble by seven
elif(num>0):
    print("Your number is positive and not divisble by seven :( ")
elif(num<0 and num%7 == 0):
    print("Your numver is negative and divisible by seven")
elif(num<0):
    print("Your number is negative and not divisible by seven")
else:
    print("Your number is zero")
