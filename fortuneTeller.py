#Greg Phillips
#9/15/17
#fortuneTeller.py - tells your fortune

print("Pick red or blue: ")
color = input(" ")

print("Pick a number from 1-4: ")
num = float(input(" "))

if(color=="red" and num==1):
    print("You will die in a car crash")
elif(color=="red" and num==2):
    print("You will fail a test")
elif(color=="red" and num==3):
    print("You will break your leg")
elif(color=="red" and num==4):
    print("You will fall down the stairs")
elif(color=="blue" and num==1):
    print("You will be attacked by a pack of wolves")
elif(color=="blue" and num==2):
    print("You will fall off a cliff")
elif(color=="blue" and num==3):
    print("You will repeat a grade")
elif(color=="blue" and num==4):
    print("You will die")