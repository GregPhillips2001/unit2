#Greg Phillips
#9/14/17
#unitConverter.py - converts units

while True:
    print("1) Kilometers to miles")
    print("2) Kilograms to Pounds")
    print("3) Liters to Gallons")
    print("4) Celsius to Fahrenheit")
    print("5) Quit")

    num = float(input("Choose a number: "))

    if(num==1):
        km = float(input("Enter a number of kilometers: "))
        print(km, "kilometers is", km*0.621371, "miles")
    elif(num==2):
        kg = float(input("Enter a number of kilograms: "))
        print(kg, "kilograms is", kg*2.20462, "pounds")
    elif(num==3):
        li = float(input("Enter a number of liters: "))
        print(li, "liters is", li*0.264172, "gallons")
    elif num==4:
        c = float(input("Enter a degrees of Celsius: "))
        print(c, "degrees Celsius", c*1.8 + 32, "degrees Fahrenheit")
    elif num==5:
        break
    else:
        print("That's not a choice")