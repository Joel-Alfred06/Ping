"13 to 18 = Junior member  18 - 23 = member, else = senior member"

Age = int(input(" what is your age? ")) 

if (Age > 23):
    print("You are a Senior Member")
if (Age <= 12):
    print("you are not old enough to become a member")
elif (Age <= 18 ):
    print("You are a Junior member")
else :
    print("You are a Member")