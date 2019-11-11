"""
Обрахувати формулу пепремноженяя елементів. Від i=1 до n обрахувати добуток при усіх i - (1/x**2+i)
"""

import re

print("Данилевич Олександр Олександрович\nЛабораторна робота №2\nВаріант 8\nПідрахунок значення")

re_number = re.compile("^[-+]?\d+\.?\d*$")

re_integer = re.compile("^[-+]{0,1}\d+$")

def validator(pattern, promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text


def number_greater_zero_validator(prompt):
   number = int(validator(re_integer, prompt))
   while number <= 0:
      number = int(validator(re_integer, prompt))

   return number

def number_not_zero_validator(prompt):
   number = float(validator(re_number, prompt))
   while number == 0:
      number = float(validator(re_number, prompt))

   return number
n=int(number_greater_zero_validator("Введіть кількість повторень:"))
x=float(number_not_zero_validator("Введіть аргумент x:"))

sum=float(1)
for i in range(1, n+1):
   sum =sum*(1/x**2+i)

print("Сума = %.4f" %sum)
