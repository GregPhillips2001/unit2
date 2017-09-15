#Greg Phillips
#9/15/17
#warmup3.py - says if number is divisible by 3,2

num = float(input("Enter a number here: "))

if(num%2==0 and num%3==0):
    print(num, "is divisible by both 2 and 3")
elif(num%2==0):
    print(num, "is divisible by 2")
elif(num%3==0):
    print(num, "is divisible by 3")
else:
    print(num, "is not divisble by 2 and 3")
    
