from ascii_logos import p_calc_logo
import os

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  # Recursive Function Example
 
  print(p_calc_logo)

  num1 = float(input("What's the first number?: "))
  print('Choose an operator from below.')
  for symbol in operations:
    print(symbol)
  is_destroyed = False
 
  while not is_destroyed:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      is_destroyed = True
      os.system('clear')
      calculator()

calculator()
