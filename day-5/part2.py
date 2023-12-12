from typing import List
from copy import deepcopy

file = []
#helper functions
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
    numbers = getNumbersFromString(line[6:]) 
    rangeSet = []
    for i in range(0, len(numbers), 2):
      rangeSet.append({'rangeStart': numbers[i]})
    for i in range(1, len(numbers), 2):
      # rangeSet[i//2]['rangeLength'] = numbers[i]
      rangeSet[i//2]['rangeEnd'] = rangeSet[i//2]['rangeStart'] + numbers[i] - 1
    alamanac['seeds'] = rangeSet
    continue
    
  
  if line[0].isalpha():
    currentlyParsing = line.split(" ")[0]
    continue
  
  if line[0].isnumeric():
    map = getNumbersFromString(line)
      
    map = {#'destination': map[0],
          #  'source': map[1],
          #  'range': map[2],
           'start': map[1],
           'end': map[1] + map[2] - 1,
           'modifier': map[0] - map[1]}
    alamanac[currentlyParsing].append(map)
    
# print(alamanac)

initialSeedRanges = alamanac['seeds'].copy()
seedRangesInput = initialSeedRanges.copy()
seedRangesMapOutput = []
seedRangesMapSetOutput = []

seedRanges = []
for mapSet in list(alamanac.values())[1:]:
  for map in mapSet:
    print(f'Input:\n{seedRangesInput}')
    print(f'Map:\n{map}')
    for seedRange in seedRangesInput:
      if map['start'] > seedRange['rangeEnd'] or map['end'] < seedRange['rangeStart']:
        seedRangesMapOutput.append(seedRange)
        continue
      
      intervalStart = max(map['start'], seedRange['rangeStart'])
      intervalEnd = min(map['end'], seedRange['rangeEnd'])
      
      newRange = {
        'rangeStart': intervalStart + map['modifier'],
        'rangeEnd': intervalEnd + map['modifier'],
      }
      
      seedRangesMapSetOutput.append(newRange)
      
      if intervalStart != seedRange['rangeStart']:
        seedRangesMapOutput.append({
          'rangeStart': seedRange['rangeStart'],
          'rangeEnd': intervalStart -1,
        })
        
      if intervalEnd != seedRange['rangeEnd']:
        seedRangesMapOutput.append({
          'rangeStart': intervalEnd + 1,
          'rangeEnd': seedRange['rangeEnd'],
        })
        
    print(f"MapSetOutput: {seedRangesMapSetOutput}")
    print(f"MapOutput: {seedRangesMapOutput}")
    
    print('-------------------------------')
        
    seedRangesInput = deepcopy(seedRangesMapOutput)
    seedRangesMapOutput = []
    
  for seedRange in seedRangesInput:
    seedRangesMapSetOutput.append(seedRange)
    
  print("New Mapset")
      
  seedRangesInput = seedRangesMapSetOutput.copy()
  seedRangesMapSetOutput = []
  seedRangesMapOutput = []
  
seedRanges = seedRangesInput.copy()
lowestNumberLocation = None

print(seedRanges)

for seed in seedRanges:
  lowestNumberLocation = min(seed['rangeStart'], lowestNumberLocation) if lowestNumberLocation else seed['rangeStart']
      
print(f'The location with the lowest number is {lowestNumberLocation}')
      
# lowestNumberLocation = None
# for seedRange in seedRanges:
#   for seed in range(seedRange['rangeStart'], seedRange['rangeStart'] + seedRange['rangeLength']):
#     print(f"{(seed - seedRange['rangeStart']) * 100 / seedRange['rangeLength']}% - {seed}")
#     source = seed
#     for mapSet in list(alamanac.values())[1:]:
#       destination = None
#       for map in mapSet:
#         if source >= map['source'] and source < map['source'] + map['range']:
#           destination = map['destination'] + (source - map['source'])
#           break
#       if destination:
#         source = destination
    
#     if not lowestNumberLocation:
#       lowestNumberLocation = source
#       continue
#     lowestNumberLocation = min(lowestNumberLocation, source)
  
# print(f'The location with the lowest number is {lowestNumberLocation}')
      