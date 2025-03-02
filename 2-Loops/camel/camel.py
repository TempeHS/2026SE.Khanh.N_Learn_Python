# Get user input
camelCase = input("camelCase: ")

# Print "snake_case"
print("snake_case: ", end="")

# Loop through every letter
for letter in camelCase:

    # Check if the letter is uppercase
    if letter.isupper():
        # Print underscores and the lowercase letter
        print("_" + letter.lower(), end="")


    # Otherwise, print the letter
    else:
        print(letter, end="")

# Print space in the end
print()