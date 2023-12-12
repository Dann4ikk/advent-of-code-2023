
filePath = './input.txt'

sum = 0

with open(filePath) as file:

  line = file.readline().strip()

  while line:
    digit1Index = line.find(next(filter(str.isdigit, line)))
    digit2Index = line.find(next(filter(str.isdigit, line[::-1])))
    
    digit1 = int(line[digit1Index])
    digit2 = int(line[digit2Index])
    
    value = digit1 * 10 + digit2
    sum += value
    
    line = file.readline().strip()
  
  print(sum)
    
  
