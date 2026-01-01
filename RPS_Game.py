#rock paper scissor
import random
options =('rock','paper','scissor')
player=None
computer=random.choice(options) 

while player not in  options:
    player=input('enter your choice') 
print(f'player:{player}')  
print(f'computer:{computer}')

if player == computer:
    print('its a tie')
elif player=='rock'and computer=='scissor':
    print('you win')
elif player=='paper'and computer=='rock':
    print('you win')
else:
    print('lose')
    