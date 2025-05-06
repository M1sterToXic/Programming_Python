"""STOP"""
# from random import randint
# s = int(randint(1,3000))
# print(s)
# k1 = 0
# k2 = 600
# k3 = 1200
# k4 = 1800
# F = 0
# if (k1<s) and (k2<s) and (k3<s):
#     f = (k4 - s)
#     print(abs(f))
# elif (k1<s) and (k2<s):
#     f = (k3 - s)
#     print(abs(f))
# elif (k1<s):
#     f = (k2 -s)
#     print(f)
# else:
#     f = (k1 -s)
#     print(f)




"""ARITHMETIC"""
# def arithmetic(a:int, b: int, operator: str):
#     if operator == '+':
#         print('addition = ',a + b)
#     elif operator == "-":
#         print("deduction = ",a - b)
#     elif operator == "*":
#         print("multiply = ",a * b)
#     elif operator == "/":
#         print("division = ",a / b)
#     else:
#         print("ERROR")
#
# operator = input('Введите: "+", "-", "*", "/"  :', )
# a = int(input("Введите число  а: ", ))
# b = int(input("Введите число  b: ", ))
# arithmetic(a,b,operator)




"""LEAP_YEAR"""
# year = int(input("Введите свой год:  "))
# if year%4==0:
#     print("TRUE")
# else:
#     print("FALSE")




"""SQUARE"""
# def f(n):
#     print(f"P = {n} * 4 = {n * 4}")
#     print(f"S = {n} * {n} = {n * n}")
#
# n = int(input())
# f(n)




"""SEASON"""
# def S(n):
#     if n == 12 or n < 3:
#         return("winter")
#     elif n == 3 or n < 6:
#         return("spring")
#     elif n == 6 or n < 9:
#         return("summer")
#     elif n == 9 or n <12:
#         return("autumn")
#
# n = int(input("Введите месяц(число): ", ))
# S(n)




"""BANK"""
# def bank():
#     procent = 1.1
#     vklad = int(input("Введите свою сумму взноса: ", ))
#     year = int(input("На какой срок?: ",))
#
#     for i in range(year):
#         vklad = (vklad * procent)
#         print(int(vklad))
#
# bank()




"""IS_PRIME"""
# def is_prime(x):
#     f = True
#     for i in range(2, int(x**0.5)):
#         if x%i == 0:
#             f = False
#         return(f)
# a = int(input())
# print(is_prime(a))




"""CALENDAR"""
# def calendar(day, month, year):
#     if day <= 31 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
#         print("date corect")
#     elif day <= 30 and (month == 4 or month == 6 or month == 9 or month == 11):
#         print("date corect")
#     elif day <=29 and month == 2 and (year % 4 == 0):
#         print('date corect')
#     elif day <= 28 and month == 2 and (year % 4 != 0):
#         print('Not date corect')
#     else:
#         print('ERROR')
#
# day = int(input("День: ",))
# month = int(input('Месяц: ',))
# year = int(input("Год: ",))
# calendar(day, month, year)



"""ENT_2024"""
# def mult(n,m):
#     x = 1
#     while x<=m:
#         print(n * x)
#         x+=1
# a = int(input("a = ", ))
# b = int(input("b = ", ))
# if b>3:
#     mult(a,3)
# else:
#     mult(a,b)



"""Простое число, Составное число"""
# a = int(input("Введите число а: ", ))
# if (a % 1 == 0) and (a % a == 0) and ((a % 2 == 0) or (a % 5 == 0) or (a % 9 == 0) or (a % 4 == 0) or (a % 7 == 0) or (a % 3 == 0) or (a % 9 == 0) or (a % 6 == 0)):
#     print(f"Составное число: {a}")
# elif a == 1:
#     print(f"Это единица: {a}")
# elif (a % 1 == 0) and (a % a == 0):
#     print(f"Простое число: {a}")




"""Бесконечный, Контролируемы Цикл"""
# while True:
#     x = input("Введите число или символы: ",)
#     if x == "stop":
#         break
#     print(f"Ваше сообщение:  {x}", f"     Длина вашего сообщения:  {len(x)}")




"""Бесконечный, Контролируемы Цикл С Числами"""
# a = [0]
#
# while True:
#     x = int(input("Введите число: ",))
#     if x == x:
#         a.append(x)
#     elif x == "-":
#         break
#     print(f"Ваше сообщение:{x}", f"   Список:{a}", "   !ДЛЯ ОСТАНОВКИ ВВЕДИТЕ (-)!")




"""Математические функции и работа с модулем math"""
# import math
# r = [1, 23, 45, 3223, -65, 5]
# a = abs(-234)
# print(r)
# print("max(r): ", max(r))
# print("min(r): ", min(r))
# print("pow(49, 0.5): ", pow(49, 0.5), "pow(27, 1/3): ", pow(27, 1/3))
# print("abs(-1234): ", abs(-1234), "a: ", a)
# print("round(0.5): ", round(0.5), "round(0.50000001): ", round(0.50000001))
# print("round(7.8765, 2): ", round(7.8765, 2), "round(7.8765, 1): ", round(7.8765, 1))
# print("round(781.8765, -2): ", round(781.8765, -2), "round(691.8765, -1): ", round(691.8765, -1))
# print("max(1, 2, abs(min(1,9, -3)), -10): ", max(1, 2, abs(min(1,9, -3)), -10))
# print("math.factorial(5): ", math.factorial(5))





"""Factorial"""
# f = int(input())
# n = 1
# while f>=1:
#     n *= f
#     f-=1
# print(n)




""" НОД и НОК в Математике """
# a = int(input("а: ", ))
# b = int(input("b: ", ))
#
# ia, ib = a, b        #Сохраняем переменнные т.к. они будут меняться
# while ia != ib:
#     if ia > ib:
#         ia = ia - ib
#     else:
#         ib = ib - ia
# print(f"НОД = {ia}")
# print(f"НОК: {a} * {b} // {ia} = {a*b // ia} ")




"""1.0 Нахождение процентов данного числа"""
# a = int(input("Введите процент: ", ))
# b = int(input("Введите число: ", ))
# c = (a*b)/100
# print(c)

"""1.1 Нахождение числа по его процентам"""
# a = int(input("Введите процент: ", ))
# b = int(input("Число от процента: ", ))
# x = (b/a) * 100
# print(x)

"""1.2 Нахождение процентного отношения чисел"""
# a = int(input("Введите процент выполненного a: ", ))
# b = int(input("Введите процент планового b: ", ))
# c = (a/b) * 100
# print(c)



"""ГЕНЕРАТОР ПАРОЛЕЙ"""
# import string
# import random
#
# symbol = list(string.ascii_letters + string.digits)
# random.shuffle(symbol)
# n = int(input("Введите длину пароля:", ))
# password = "".join(symbol[ : n])
# print(password)


"""График"""
# import matplotlib.pyplot as plt
#
# data = [6.1, 5.0, 3.5, 7.8, 4.6, 2.3, 5.2, 7.9, 1.2, 32.1, 1.1, 6.5]
# months = list(range(1, 13))
#
# plt.plot(months, sorted(data))
# plt.show()


"""Генератор цветов"""
# from random import randint
#
# color = randint(0, int('ffffff', 16))
# color = hex(color)
# color = str(color).lstrip("0x")
# print(f"{color}")
#

"""Как сделать полосу загрузки: библеотека tqdm"""
# from tqdm import tqdm
# import time
#
#
# def count_bananas(n):
#     count = 0
#     for _ in tqdm(
#         range(n),
#         desc="Бананы считаются...",
#         ncols=80,
#         colour="2873de",
#     ):
#         count += 1
#         time.sleep(0.1)
#     return count
#
#
# total_bananas = count_bananas(20)
# print(f"Всего бананов: {total_bananas}")


