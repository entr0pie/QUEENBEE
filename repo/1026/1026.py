""" QUEENBEE: github.com/entr0pie/QUEENBEE """
# Date: 2022-10-18
# Source: https://www.beecrowd.com.br/judge/pt/problems/view/1026
# Author: entr0pie
# Contact: <https://github.com/entr0pie>
# Name: BEE 1026

# https://www.geeksforgeeks.org/python-bitwise-operators/
while True:
  try:  
    numbers = input("")
  except EOFError:
    break

  numbers = numbers.split(' ')
  A, B = int(numbers[0]), int(numbers[1])

  op1 = ~A & B
  op2 = A & ~B

  mofiz = op1 | op2

  print(mofiz)
