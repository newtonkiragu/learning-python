# a program that takes an input from the user then print ransom answers from the 8ball
#  In your program, allow a person to input a question, and then create a random number. Based on the random number, pick a response to the question using if, elif, and else statemen
import random
affirmative = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes"]
negative = ["Reply hazy try again", " Ask again later", " Better not tell you now", "Cannot predict now", "Concentrate and ask again"]
non_commital = ["Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "very doubtful"]
a = random.choice(affirmative)
b = random.choice(negative)
c = random.choice(non_commital)
question = input("ask me a random question: ")
random_number = random.randint(1,20)
if random_number > 15:
    print(c)
elif random_number > 10:
    print(b)
else:
    print(a)
