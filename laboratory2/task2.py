"""
Скласти програму розкладання натурального числа n на прості множники.
"""

import re

print("Данилевич Олександр Олександрович\nЛабораторна робота №2\nВаріант 8\nРозкладання натурального числа n на прості множники.")

re_integer = re.compile("^[-+]{0,1}\d+$")

def validator(pattern, promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text


def int_greater_zero_validator(prompt):

    number = int(validator(re_integer, prompt))
    while number<=0:
        number = int(validator(re_integer, prompt))

    return number

n = int_greater_zero_validator("Ввведіть натуральне число:")
i=1
print("Прості множники числа:")
while(i<=n+1):
    i+=1
    if(n%i==0):
        print(i)
        n=n/i
        i=1
