from replit import clear 
from cal_art import logo 

def add(n1,n2):
  return n1 + n2
def subtract(n1,n2):
  return n1 - n2
def multiply(n1,n2):
  return n1 * n2
def divide(n1,n2):
  return n1 / n2

operations = {'+' : add,'-' : subtract,'*' : multiply,'/' : divide}

def calc():
  clear()
  print(logo)
  print('Welcome to the CALCULATOR !\n')
  num1 = int(input('Enter 1st number : '))
  gameon = True
  while gameon :
    for i in operations:
      print(i) 
    op = input('Choose operation : ')
    num2 = int(input('Enter 2nd number :'))
    print(f"\n{float(num1)} {op} {float(num2)} = {float(operations[op](num1,num2))}")
    choice = int(input('Choose -> 1.New Calculation | 2.Continue | 3.Exit program : '))
    if choice == 1:
      calc()
    elif choice == 2:
      num1 = float(operations[op](num1,num2))
      print(f'\n No. 1 : {num1}')
    else :
      print('Thank you for using the calculator !')
      break 
calc()