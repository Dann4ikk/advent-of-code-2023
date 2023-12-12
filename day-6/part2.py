from typing import List
import math

def getNumberFromString(string) -> int:
  number = 0
  
  for i, char in enumerate(string):
    if char.isnumeric():
      number = number * 10 + int(char)
      
    
  return number

lines = []

with open('day-6/input.txt') as f:
    lines = f.readlines()
    
race = {
  'time': getNumberFromString(lines[0][4:]),
  'distance': getNumberFromString(lines[1][8:])      
}

print(race)

''' 
| a + b = c
| a * b > d

b = c - a
ac - a*a > d

a^2 -ca + d < 0

a1 = (c - sqrt(c^2 - 4d)) / 2)
a2 = (c + sqrt(c^2 - 4d) / 2)
'''

print(getNumberFromString(lines[0]))

minHoldingTime = (race['time'] - math.sqrt(race['time']**2 - 4*race['distance'])) / 2
maxHoldingTime = (race['time'] + math.sqrt(race['time']**2 - 4*race['distance'])) / 2 

minHoldingTime = math.floor(minHoldingTime) + 1
maxHoldingTime = math.ceil(maxHoldingTime) - 1

possibleHoldingTimes = maxHoldingTime - minHoldingTime + 1
    
print(f'The number of all the possible ways to beat the record is {possibleHoldingTimes}')
    

    
