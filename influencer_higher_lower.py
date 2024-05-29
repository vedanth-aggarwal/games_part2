from time import sleep
from art import logo,vs
from game_data import data 
from replit import clear 
import random

def randaccount():
  return random.choice(data)
  
def format(account):
  print(f"{account['name']}, a/an {account['description']}, from {account['country']}")
  
def check(accounta,accountb):
  if accounta['follower_count'] > accountb['follower_count'] and guess == 'A':
    return True
  elif accounta['follower_count'] < accountb['follower_count'] and guess == 'B':
    return True
  else:
    return False
    
gameon = True
global c,score
score = 0
accounta = randaccount()
print(logo)
while True:
  accountb = accounta
  while accountb == accounta:
    accountb = randaccount()
  print(f"Compare A : ",end="")
  format(accounta)
  print(vs)
  print(f"To B : ",end="")
  format(accountb)
  guess = input('Who has higher followers ? A or B : ').upper()
  result = check(accounta,accountb)
  clear()
  print(logo)
  if result:
    score+=1
    print(f'Correct Answer ! Score : {score} ')
  else:
    if accounta['follower_count'] > accountb['follower_count']:
      print(f"Incorrect Answer ! {accounta['name']} has more followers than {accountb['name']}")
    elif accounta['follower_count'] < accountb['follower_count']:
      print(f"Incorrect Answer ! {accountb['name']} has more followers than {accounta['name']}")
    else:
      print('INVALID')
    print("Thanks for playing 'Higher Or Lower' !")
    break
  accounta = accountb
  