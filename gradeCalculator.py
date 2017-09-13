#Greg Phillips
#9/13/17
#gradeCalculator.py - calculates the letter grade to their percentage grade

gradePercent = float(input("Enter your percent grade here: "))
if(gradePercent<60):
    print("You earned an incomplete")
elif(gradePercent>=60 and gradePercent<70):
    print("You earned a D")
elif(gradePercent>=70 and gradePercent<80):
    print("You earned a C")
elif(gradePercent>=80 and gradePercent<90):
    print("You earned a B")
else:
    print("You earned an A")



