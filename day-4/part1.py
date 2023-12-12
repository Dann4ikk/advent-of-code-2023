import json

lines = []
with open("input.txt") as f:
    lines = f.readlines()

cardSet = []

for i,line in enumerate(lines):
  winningNumbers = []
  cardNumbers = []
  
  isParsingNumber = False
  number = None
  isParsingWinningNumbers = True
  
  for char in line[line.find(':'):]:
    if char == '|':
      isParsingWinningNumbers = False
    
    if char.isnumeric() and isParsingNumber:
      number = number * 10 + int(char)
    
    if char.isnumeric() and not isParsingNumber:
      number = int(char)
      isParsingNumber = True
      
    if not char.isnumeric() and isParsingNumber and isParsingWinningNumbers:
      winningNumbers.append(number)
      number = None
      isParsingNumber = False
      
    if not char.isnumeric() and isParsingNumber and not isParsingWinningNumbers:
      cardNumbers.append(number)
      number = None
      isParsingNumber = False
      
  cardSet.append({'cardNumber': i + 1,
                  'winningNumbers': winningNumbers,
                  'cardNumbers': cardNumbers,
                  'instances': 1})
  

for card in cardSet:
  luckyNumbers = 0
  for number in card['winningNumbers']:
    if number in card['cardNumbers']:
      luckyNumbers += 1
      
  if(luckyNumbers == 0):
    continue
  for i in range(1, luckyNumbers + 1):
    for j, card2 in enumerate(cardSet):
      if card2['cardNumber'] == card['cardNumber'] + i:
        card2['instances'] += 1 * card['instances']
        break
      
numberOfCards = 0
for card in cardSet:
  numberOfCards += card['instances']
        
print(f"The total amount of scratchcards is {numberOfCards}")
    
