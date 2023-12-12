
from unicodedata import digit


filePath = './input.txt'

sum = 0

# fill the rest of the dictionary
digitWordsTodigits = {
  'one' : 1,
  'two' : 2,
  'three' : 3,
  'four' : 4,
  'five' : 5,
  'six' : 6,
  'seven' : 7,
  'eight' : 8,
  'nine' : 9
}

with open(filePath) as file:

  line = file.readline().strip()

  while line:
    
    digit1 = 0
    digit2 = 0
    
    cache = ""
    
    for letter in line:
      
      print(f'cache: {cache}')
      
      digitFound = False
      for key in digitWordsTodigits:
        if key in cache:
          digit1 = digitWordsTodigits[key]
          print(f"found it: {digit1}")
          digitFound = True
      if digitFound:
        break
      
      if letter.isdigit():
        digit1 = int(letter)
        break
      
      cache += letter
      
    cache = ""
        
    for letter in line[::-1]:
      
      
      
      print(f'cache: {cache}')
      
      digitFound = False
      for key in digitWordsTodigits:
        if key in cache[::-1]:
          digit2 = digitWordsTodigits[key]
          print(f"found it: {digit2}")
          digitFound = True
      
      if digitFound:
        break
      
      if letter.isdigit():
        digit2 = int(letter)
        break
      
      cache += letter
      
    
    
    value = digit1 * 10 + digit2
    print(f'digit1: {digit1}, digit2: {digit2}, value: {value}')
    sum += value
    
    line = file.readline().strip()
  
  print(sum)
    
  
