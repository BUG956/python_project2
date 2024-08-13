from random import randint
import random

class Die():
    '''Creates a die with a certain number of sides'''
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        '''Returns a random number between 1 and the number of sides'''
        return randint(1, self.sides)

thisdice = Die() # creates a six-sided die

results = []
for i in range(10): # rolls the die 10 times
    results.append(thisdice.roll_die())

print(results)

lottolist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',\
             'A', 'B', 'C', 'D', 'E'] # list of 10 numbers and 5 letters
winlist = [] # empty list for winners

while len(winlist) < 4: 
    ball = random.choice(lottolist) # choose a random "ball"
    if ball not in winlist: # if it hasn't already been selected
        winlist.append(ball) # add it to the list

print("Here are the winning balls: ", str(winlist)) # print winners
print("Any ticket matching these four numbers/letters wins a prize!")
