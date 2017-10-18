# if statements only run when the conditions passed to it evaluate to be true
# in python empty values are considered to be false
height = []
if height:
    print("you are really tall")
# we use elif when we have more than one condition to check for
elif height:
    print("you are of average height")
# else is used when the conditions passed evaluate to false
else:
    print("you are really short")
