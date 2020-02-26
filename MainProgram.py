import random
import pandas as pd


fruitCount = pd.read_csv("Fruits.csv")

print(fruitCount)
x = 1
while x <=1000:

    fruitQty = fruitCount['Name'].count()
    randomPick = random.randrange(fruitQty)
    print(randomPick)
    x=x+1


    #Increments the Qty by one each time it is randomly picked
    fruitCount['Qty'][randomPick] = fruitCount['Qty'][randomPick] + 1

y = 0
while y < fruitCount['Name'].count():
    print('{}: {}'.format(fruitCount['Name'][y],fruitCount['Qty'][y]))
    y=y+1


