# Ask user for input
print("Enter your message")

# Get the user input
input_string = input()

# Dicrionary for the user input
characters = {
    "a":1,
    "b":2,
    "c":3,
    "d":1,
    "e":2,
    "f":3,
    "g":1,
    "h":2,
    "i":3,
    "j":1,
    "k":2,
    "l":3,
    "m":1,
    "n":2,
    "o":3,
    "p":1,
    "q":2,
    "r":3,
    "s":4,
    "t":1,
    "u":2,
    "v":3,
    "w":1,
    "x":2,
    "y":3,
    "z":4
}

# print(characters)
# print(list(characters.keys()))

# Print methods available in the dictionary

# print(dir(characters))
# print(characters.values())

# New dictionary for the user input
user_input = {}


# Loop through the user input and store each letter
for letter in input_string:
    # Convert to lower case to ensure code is case insensitive
    lower_case = letter.lower()

    # Check if the letter is in the key
    if lower_case in characters.keys():

        # Get the value of letter according to the dictionary
        value_of_letter = characters.get(lower_case)

        # Add letter and its value to user input dictionary
        user_input[letter] = value_of_letter

        # Print each letter and its value from the dictionary
        print("Letter: "+ letter + ", Value: " + str(value_of_letter) )

    else:
        # Value of characters not in the key
        print("Letter: " + letter + ", Value:" + str(0))

# Print values of user input dictionary
print(list(user_input.values()))

# Sum values of user input dictionary
sum_of_user_input_values = sum(user_input.values())

print("Total Value: " + str(sum_of_user_input_values))