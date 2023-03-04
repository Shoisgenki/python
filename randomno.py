import random

x = random.randint(1,6)  #chooses random integer from argument
y = random.random() #chooses random floating point from 0 to 1

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList) #chooses random element from list


cards = [1,2,3,4,5,6,7,8,9,'J','Q','K']

random.shuffle(cards) #pretty self explanatory
print(cards)

