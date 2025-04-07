#Create dictionary with all fruits and its calories
fruits = {
    "banana": 110,
    "apple": 130,
    "orange": 80,
    "strawberries": 50,
    "watermelon": 80,
    "grapes": 90,
    "kiwifruit": 90,
    "pear": 100,
    "peach": 60,
    "nectarine": 60,
    "lime": 20,
    "lemon": 15,
    "honeydew melon": 50,
    "grapefruit": 60,
    "cantaloupe": 50,
    "avocado": 50,
    "pineapple": 50,
    "plums": 70,
    "sweet cherries": 50,
    "tangerine": 50,
}

# get user inout
fruit_asked = input("Item: ")

# Loop through the dictionary 
for key in fruits:
    # Find the fruit asked (rmb to use lowercase)
    if key in fruit_asked.lower():
        # Print the calories
        print("Calories:", fruits[key])