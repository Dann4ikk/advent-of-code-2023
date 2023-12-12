
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
   
print(games)
sum = 0
for i in range(len(games)):
  game = games[i]
  isPossible = True
  
  for set in game:
    if('red' in set.keys() and set['red'] > 12):
      isPossible = False
      break
    if('green' in set.keys() and set['green'] > 13):
      isPossible = False
      break
    if('blue' in set.keys() and set['blue'] > 14):
      isPossible = False
      break
    
  if isPossible:
    sum += i + 1
    
print(sum)
    
  
