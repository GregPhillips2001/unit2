#Greg Phillips
#9/13/17
#movie.py - tells you the rating of movie you can watch based on your age

age = int(input("Enter your age here: "))
if(age>=13 and age<17):
    print("You can watch PG-13 movies, PG movies, and G movies")
elif(age<13):
    print("You can watch PG and G movies")
else:
    print("You can watch any movie")
    
