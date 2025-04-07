# user input 
# check for vowels ( a, e, i, o, u)
#remove vowels from the string
# return the string without vowels
# if none of the vowels are present in the string, return the string as it is
# then print 

User = input("Input: ")

print ("Output: ", end="")

remove_vowels = ["a", "e", "i", "o", "u"] # ANOTHER WAY remove_vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"] 

for letter in User: 
    #if not letter.lower() in  ["a", "e", "i", "o", "u"]:  youtube video tutorial
    if letter.lower() not in remove_vowels: # ANOTHER WAY if letter not in remove_vowels:
        print(letter, end="")
print()