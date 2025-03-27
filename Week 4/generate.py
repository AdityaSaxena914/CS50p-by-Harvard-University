#import random will import whole random.py file
import random

#randint() randomize int
for number in range(1,11):
    number  = random.randint(1, 10)
    print(number)

#shuffle() shuffles the element in list like structures
cards = ["jack","queen","king"]
random.shuffle(cards)
for card in cards:
    print(card)