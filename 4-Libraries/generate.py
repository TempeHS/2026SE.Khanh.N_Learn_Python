### simple one for tossing a coin
#from random import choice

#coin = choice(["heads", "tails"])
#print(coin)

### simple one for generating a random number
#import random
## Generate a random number between 1 and 10
#number = random.randint(1, 10)
#print(number)

### simple one for shuffling a deck of cards
import random

cards = ["Ace", "King", "Queen", "Jack"]
random.shuffle(cards)
for card in cards:
    print(card)