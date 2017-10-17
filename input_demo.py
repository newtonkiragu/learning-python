# learning the sys module
import sys
# the sys module is used to receive aruements from the terminal without having to prompt the user to do anything
name = sys.argv[1]
something = sys.argv[2]

print("how old are you")
age = int(input())

print(name)
print(age)
print(something)