import replit 
import random 
import art 
highscore = 0
def guessnum():
  global highscore
  replit.clear()
  print(art.logo)
  number = random.randint(1,100)
  guess = None
  level = int(input('Choose Lives ? 5 or 10 : '))
  lives = level
  while lives!= 0:
    guess = int(input('Enter Guess : '))
    if guess == number:
      print(f"\nGreat Job ! Number is {repr(number)}")
      print(f"You took {10-lives} tries")
      break
    elif guess > number:
      print('Too high')
    elif guess < number : 
      print('Too Low')
    lives-=1
    print(f"You have {lives} lives remaining !\n")
  else :
    print(f"You lost , correct number is {repr(number)}")
  choice = input('\nPlay Again ? Y or N : ').upper()
  if choice == 'Y':
    guessnum()
  else:
    print('Thanks for playing the guessing game')

guessnum()