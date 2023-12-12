file = open("input.txt", "r")
lines = file.readlines()

numbers = []

for i, line in enumerate(lines):
  
  isReadingNumber = False
  positionStart = None
  positionEnd = None
  number = 0
  
  for j, char in enumerate(line):
    
    if char.isnumeric():
      number = number * 10 + int(char)
      if(isReadingNumber == False):
        positionStart = j
        isReadingNumber = True
      if line[j+1] and not line[j+1].isnumeric():
        positionEnd = j
        isReadingNumber = False
        numbers.append({'number': number,
                        'positionStart': positionStart,
                        'positionEnd': positionEnd,
                        'line': i})
        number = 0

# print(numbers)

prevPossibleGearPositions = {}

gearRatioSum = 0
for number in numbers:
  y = number['line']
  xStart = number['positionStart']
  xEnd = number['positionEnd']
  isAdjacentToSymbol = False
  for y in range(y-1, y+2):
    if y < 0 or y >= len(lines):
      continue
    
    for x in range(xStart-1, xEnd+2):
      
      if x < 0 or x > len(lines[y]):
        continue
      
      if y == number['line'] and x in range(xStart, xEnd+1):
        continue
      
      if lines[y][x] == '*':
        if((x, y) not in prevPossibleGearPositions):
          prevPossibleGearPositions[(x, y)] = number['number']
          break
        gearRatioSum += number['number'] * prevPossibleGearPositions[(x, y)]

print(f'The sum of all the gear ratios is {gearRatioSum}')  
      