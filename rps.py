import random 
import json

posmoves = []
with open('key.json') as json_file:
    posmoves = json.load(json_file)
posmoves.sort()

while True:
    valid = False

    while (valid==False):
        playermove = input('Ваш ход (rock, paper, scissors): ')
        if (playermove=='scissors') or (playermove=='rock') or (playermove=='paper'):
            valid=True
        else:
            print('Неверный ход!')
    
    playermove = playermove.lower()
    botmove = random.choice(posmoves)

    winner = ''

    if (playermove=='rock') and (botmove=='scissors'):
        winner='player'
    if (playermove=='paper') and (botmove=='rock'):
        winner='player'
    if (playermove=='scissors') and (botmove=='paper'):
        winner='player'
    if (playermove=='rock') and (botmove=='paper'):
        winner='bot'
    if (playermove=='scissors') and (botmove=='rock'):
        winner='bot'
    if (playermove=='paper') and (botmove=='scissors'):
        winner='bot'
    if (playermove==botmove):
        winner='tie'

    print(f'{playermove} vs {botmove}\n{winner} выиграл!')

    if (winner=='player') and (posmoves.count(botmove) != 1):
        posmoves.remove(botmove)
    if (winner=='bot'):
        posmoves.append(botmove)

    posmoves.sort()

    with open('key.json', 'w') as outfile:
            json.dump(posmoves, outfile)