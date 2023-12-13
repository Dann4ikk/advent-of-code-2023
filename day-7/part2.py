
from typing import List
from json import dumps

cardOrder = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
handTypeOrder = ['high-card', 'one-pair', 'two-pair', 'three-of-a-kind', 'full-house', 'four-of-a-kind', 'five-of-a-kind']

def sortHandArray(array: List[dict]) -> List[dict]:
  
  if len(array) == 1:
    return array
  
  if len(array) == 2:
    for i, card1 in enumerate(array[0]['hand']):
      card2 = array[1]['hand'][i]
      if cardOrder.index(card1) < cardOrder.index(card2):
        return array
      if cardOrder.index(card1) > cardOrder.index(card2):
        return array[::-1]
      if cardOrder.index(card1) == cardOrder.index(card2):
        continue
      return array
      
  if len(array) == 0:
    return []
      
  pivot = array[-1]
  left = []
  center = [pivot]
  right = []
  for hand in array:
    if hand == pivot:
      continue
    
    for i, card1 in enumerate(hand['hand']):
      card2 = pivot['hand'][i]
      if cardOrder.index(card1) > cardOrder.index(card2):
        right.append(hand)
        break
      if cardOrder.index(card1) < cardOrder.index(card2):
        left.append(hand)
        break
      if cardOrder.index(card1) == cardOrder.index(card2):
        continue
      center.append(hand)
  
  return sortHandArray(left) + [pivot] + sortHandArray(right)

lines = []
with open('day-7/input.txt') as f:
  lines = f.readlines()
  
hands = []
  
for line in lines:
  parts = line.strip().split(' ')
  hand = {'hand': parts[0],
            'bid': int(parts[1])}
  
  jokerCount = 0
  cards = {}
  for char in parts[0]:
    if char in cards:
      cards[char] += 1
    else:
      cards[char] = 1
      
  
      
  dominantCard = ('', 0)
  for card in list(cards.keys()):
    if card == 'J':
      continue
    if cards[card] >= dominantCard[1]:
      dominantCard = (card, cards[card])
      
  if dominantCard[0] != '' and 'J' in list(cards.keys()):
    cards[dominantCard[0]] += cards['J']
    cards.pop('J')
  
      
  if len(list(cards.keys())) == 1:
    hand['type'] = 'five-of-a-kind'
  elif len(list(cards.keys())) == 2 and (list(cards.values())[0] == 1 or list(cards.values())[0] == 4):
    hand['type'] = 'four-of-a-kind'
  elif len(list(cards.keys())) == 2 and (list(cards.values())[0] == 2 or list(cards.values())[0] == 3):
    hand['type'] = 'full-house'
  elif len(list(cards.keys())) == 3 and 3 in list(cards.values()):
    hand['type'] = 'three-of-a-kind'
  elif len(list(cards.keys())) == 3:
    hand['type'] = 'two-pair'
  elif len(list(cards.keys())) == 4:
    hand['type'] = 'one-pair'
  elif len(list(cards.keys())) == 5:
    hand['type'] = 'high-card'
    
  hands.append(hand)

print(dumps(hands, indent=2))
  
handsByType = {}
  
for hand in hands:
  if 'type' not in hand:
    print(hand)
  if hand['type'] in handsByType:
    handsByType[hand['type']].append(hand)
  else:
    handsByType[hand['type']] = [hand]
      
sortedHands = []
      
for handType in handTypeOrder:
  if handType not in handsByType:
    continue
  
  sortedHands += sortHandArray(handsByType[handType])

winnings = 0

for i, hand in enumerate(sortedHands):
  sortedHands[i]['rank'] = i + 1
  
  winnings += sortedHands[i]['rank'] * sortedHands[i]['bid']
  
print(f'The total winnings are {winnings}')
  
  
  
