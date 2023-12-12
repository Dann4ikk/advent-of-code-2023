
filePath = './input.txt'

games = []

with open(filePath) as file:

  line = file.readline().strip()

  while line:
    
    game = []
    set = {}
    color = ""
    balls = 0 
    
    colonIndex = line.find(':')
    for i in range(len(line[colonIndex:])): 
      letter = line[colonIndex:][i]
      if(letter.isdigit()):
        balls = balls * 10 + int(letter)
        continue
      if balls and letter.isalpha():
        color += letter
      if letter == ',':
        set[color] = balls
        color = ""
        balls = 0
        continue
      if letter == ';':
        set[color] = balls
        game.append(set)
        color = ''
        balls = 0
        set = {}
        continue
      if i == len(line[colonIndex:]) - 1:
        set[color] = balls
        game.append(set)
        color = ''
        balls = 0
        set = {}
        continue
      
      
    games.append(game)  
    
    line = file.readline().strip()
   

powersSum = 0
for i, game in enumerate(games):
  minBlue = 0
  minRed = 0
  minGreen = 0
  for set in game:
    for color in set:
      if color == 'blue' and set[color] > minBlue:
        minBlue = set[color]
      if color == 'red' and set[color] > minRed:
        minRed = set[color]
      if color == 'green' and set[color] > minGreen:
        minGreen = set[color]
        
  power = minBlue * minRed * minGreen
  powersSum += power
  
print(powersSum)
  
