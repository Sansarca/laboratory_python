"""
Підрахувати кількість додатніх серед чисел а, b, с (ввести з клавіатури).
"""
import re

print("Данилевич Олександр Олександрович\nЛабораторна робота №1\nВаріант 8\nЗнаходження кількості додатніх чисел")

re_float = re.compile("^[-+]?\d+\.?\d*$")

def validator(pattern, promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

first_number = validator(re_float, "Введіть перше число:")
second_number = validator(re_float, "Введіть друге число:")
third_number = validator(re_float, "Введіть третє число:")

n=0
if float(first_number)>0:
    n+=1
if float(second_number)>0:
    n+=1
if float(third_number)>0:
    n+=1

print("Кількість додатніх чисел =",n)