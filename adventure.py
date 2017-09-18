#Greg Phillips
#7/18/17
#adventure.py - the adventure of a lifetime

print("You are being chased by a pack of wolves")
print("You come across a cave")
print("Do you enter the cave?")
cave = input("")
if "n" in cave or "N" in cave:
    print("You are brutally eaten alive by the wolves and die")
elif "y" in cave or "Y" in cave:
    print("You enter the cave")
    print("Luckily the wolves don't follow you")
    print("However, it is dark")
    print("Do you make a fire?")
    fire = input("")
    if "n" in fire or "N" in fire:
        print("You don't start a fire, and you freeze to death")
    else:
        print("You start a fire, revealing a bunch of cave paintings. You are rescued the next day and become rich due to your discovery.")
        
    
