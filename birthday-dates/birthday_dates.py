# a program that is used to calculate the year someone was born and then tell them the year they will turn 80

from datetime import date

print("please tell us your age")
age = int(input())
today = date.today()
born = (today.year - age)
print("you were born in " + str(born))
print("is that correct?")
reply = input()
if reply == "yes":
    print("cool")
    if age >= 80:
        print("you are already older than 80")
        # else statements should always have colons in the end
    else:
        difference = (80 - age)
        year_to_eity = (today.year + difference)
        # when outputting integers using print, they have to be converted to strings and when joining them together, there should be a plus sign
        print("you will turn 80 in " + str(year_to_eity))
else:
    print("Silly potato. Who do you think you can mess with??")
    print("you were born in " + str(born))
