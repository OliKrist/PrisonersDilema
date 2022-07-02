from numbers import Number
import random
from secrets import choice

from torch import rand


class Box:
    def __init__(self, Number, PrisonerNumber):
        self.Number = Number
        self.PrisonerNumber = PrisonerNumber
        self.Opened = False

    def __str__(self):
        return "Box: " + str(self.Number) + " Prisoner: " + str(self.PrisonerNumber)


class Prisoner:
    def __init__(self, Number):
        self.Number = Number
        self.Tries = 0

    def __str__(self):
        return "Prisoner: " + str(self.Number) + " Tries: " + str(self.Tries)

def FillChoices(qty):
    choices = []
    for i in range(qty):
        choices.append(i+1)
    return choices

Prisoners = []
Qty = 100
Boxes = []
AssignedNumbers = []
n = 1

while n <= Qty:
    Prisoners.append(Prisoner(n))
    n += 1
n = 1

while n <= Qty:
    x = random.randint(1, Qty)

    if x not in AssignedNumbers:
        Boxes.append(Box(n, x))
        AssignedNumbers.append(x)
        n += 1

myNumber = 1
tries = 0

for prisoner in Prisoners:
    # Defining the prisoner
    tries = 0
    myNumber = prisoner.Number
    # Resetting the tries
    for box in Boxes:
        box.Opened = False
    success = False    
    # print(f"Prisoner {myNumber}")
    choices = FillChoices(Qty)
    while not success:
        myChoice = random.choice(Boxes)
        if myChoice.Opened == False:
            prisoner.Tries += 1
            if myChoice.PrisonerNumber == myNumber:
                prisoner.Tries = tries
                success = True
                break
            else:
                myChoice.Opened = True
                continue
    print(f"Prisoner {myNumber} tried {tries} times.")

        

for x in Prisoners:
    print(x)

# Average tries for prisoners
total = 0
for x in Prisoners:
    total += x.Tries
print(f"Average tries: {total/Qty}")

# Bar chart of tries for prisoners
tries = []
for x in Prisoners:
    tries.append(x.Tries)

import matplotlib.pyplot as plt
plt.bar(range(len(tries)), tries)
plt.show()