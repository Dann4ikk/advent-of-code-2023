from typing import List

file = []
#helper functions
def getNumbersFromString(string) -> List[int]:
  numbersArray = []
  
  isParsingNumber = False
  number = 0
  for i, char in enumerate(string):
    print(char)
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


with open("input.txt") as f:
  file = f.readlines()
  
file = [line.rstrip() for line in file]
file = [line for line in file if len(line) != 0]
  
alamanac = {
  'seeds': [],
  'seed-to-soil': [],
  'soil-to-fertilizer' : [],
  'fertilizer-to-water' : [],
  'water-to-light' : [],
  'light-to-temperature' : [],
  'temperature-to-humidity' : [],
  'humidity-to-location' : [],
  
}
currentlyParsing = ""
for i, line in enumerate(file):
  
  map = []
  
  if line.startswith("seeds:"):
    map = getNumbersFromString(line[6:])
    alamanac['seeds'] = map
    continue
    
  
  if line[0].isalpha():
    currentlyParsing = line.split(" ")[0]
    continue
  
  if line[0].isnumeric():
    map = getNumbersFromString(line)
      
    map = {'destination': map[0],
           'source': map[1],
           'range': map[2]}
    alamanac[currentlyParsing].append(map)
    
print(alamanac)

seeds = alamanac['seeds']
lowestNumberLocation = None
for seed in seeds:
  source = seed
  for mapSet in list(alamanac.values())[1:]:
    destination = None
    for map in mapSet:
      if source >= map['source'] and source < map['source'] + map['range']:
        destination = map['destination'] + (source - map['source'])
        break
    if destination:
      source = destination
  
  if not lowestNumberLocation:
    lowestNumberLocation = source
    continue
  lowestNumberLocation = min(lowestNumberLocation, source)
  
print(f'The location with the lowest number is {lowestNumberLocation}')
      