# For loops with conditions
print("input a number")
digit = int(input())
numbers = list(range(1,digit))
for number in numbers:
    if number % 2 == 0:
        print(number)
