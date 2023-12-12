from typing import List
import math

def getNumbersFromString(string) -> List[int]:
  numbersArray = []
  
  isParsingNumber = False
  number = 0
  for i, char in enumerate(string):
    if char.isnumeric():
      if not isParsingNumber:
        isParsingNumber = True
      number = number * 10 + int(char)
    
    if (not char.isnumeric() and isParsingNumber) or i == len(string)-1:
      isParsingNumber = False
      numbersArray.append(number)
      number = 0
      continue
    
  return numbersArray

lines = []

with open('day-6/input.txt') as f:
    lines = f.readlines()
    
races = []
timeList = getNumbersFromString(lines[0][4:])
distanceList = getNumbersFromString(lines[1][8:])

for i in range(len(timeList)):
    races.append({'time': timeList[i],
                  'distance': distanceList[i]})

''' 
| a + b = c
| a * b > d

b = c - a
ac - a*a > d

a^2 -ca + d < 0

a1 = (c - sqrt(c^2 - 4d)) / 2)
a2 = (c + sqrt(c^2 - 4d) / 2)
'''

print(races)

possibleHoldingTimesProduct = 1

for race in races:
    minHoldingTime = (race['time'] - math.sqrt(race['time']**2 - 4*race['distance'])) / 2
    maxHoldingTime = (race['time'] + math.sqrt(race['time']**2 - 4*race['distance'])) / 2

    
    minHoldingTime = math.floor(minHoldingTime) + 1
    maxHoldingTime = math.ceil(maxHoldingTime) - 1
    

    possibleHoldingTimesProduct *= maxHoldingTime - minHoldingTime + 1
    
print(f'The product of all the possible ways to beat the record is {possibleHoldingTimesProduct}')
    

    
