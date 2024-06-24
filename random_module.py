import random

dice = random.randint(1,6)
print(dice)

myList = ["rock", "paper", "scissor"]
print(random.choice(myList))


cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)
print(cards)