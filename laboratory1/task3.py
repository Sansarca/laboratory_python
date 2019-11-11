"""
Функция:
f(x)=x**2+4*x+5, якщо x<=2
f(x)=1/(x**2+4*x+5, якщо x>2
"""
import re

print("Данилевич Олександр Олександрович\nЛабораторна робота №1\nВаріант 8\nЗнаходження кількості додатніх чисел")

re_number = re.compile("^[-+]?\d+\.?\d*$")


def validator(pattern, promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text


x=float(validator(re_number,"Введіть значення аргументу:"))
print("Значення функції f(x):")
if x<=2:
    print("%.4f" % float(x**2+4*x+5))
elif x>2:
    print("%.4f" % float(1/(x**2+4*x+5)))

