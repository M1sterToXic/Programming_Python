
""""№1"""
# a = []
# g = []
# k = []
# while 1:
#     s = input()
#     if s != "":
#         a.append(s)
#     else:
#         break
# print(a)
# for i in range(len(a)):
#     if a[i].isdigit():
#         g.append(a[i])
#     else:
#         k.append(a[i])
# print(g)
# print(k)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""№2"""
# from random import randint
# n = 6
# a = [0] * n
# for i in range(n):
#     a[i] = randint(1,50)
# print(a)


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""№4"""
# min = []
# max = []
# musor1 = []
# musor = 0
# r = 0
# while 1:
#     s = input()
#     if s == "":
#         break
#     try:
#         musor1.append(int(s))
#         musor += int(s)
#         print(musor)
#     except ValueError:
#         print("Ошибка: введите корректное число.")
#
# if musor1:
#     r = musor/len(musor1)
#     print("r = ", r)
#
# for i in range(len(musor1)):
#     if musor1[i] < r:
#         min.append(musor1[i])
# for i in range(len(musor1)):
#     if musor1[i] > r:
#         max.append(musor1[i])
#
# print("min", min)
# print("max", max)
# print("r =", r)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""№3"""
# true = []
# a = []
# while 1:
#     s = input()
#     if s == "":
#         break
#     try:
#         a.append(int(s))
#         print(a)
#     except ValueError:
#         print("Ошибка: введите корректное число.")
# for i in range(1,len(a)):
#     if (a[i] > a[i-1]):
#         true.append(a[i])
# print(*true)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""№5"""
# Class = []
# while 1:
#     s = input()
#     if s =="":
#         break
#     try:
#         if int(s) < 230:
#             Class.append(int(s))
#             print(Class)
#     except ValueError:
#         print("Ошибка: введите корректное число.")
# Andrey = int(input("Ведите рост Андрея:"))
# try:
#     if Andrey < 230:
#         Class.append(Andrey)
#     Class.sort()
#     print(Class)
#     print(f"Андрей находится на {Class.index(Andrey)} месте в Списке",)
# except ValueError:
#     print("Ошибка: введите корректное число.")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""№6"""
# import random
# popitka = 0
# monetka = []
# while 1:
#     side = random.choice(["O","P"])
#     monetka.append(side)
#     popitka+=1
#     if len(monetka) >= 3 and monetka[-1] == monetka[-2] == monetka[-3]:
#         break
# print(*monetka,"\n","popitka = ", popitka)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""№7"""
 # 4276440013361511 k
 # 4276440013361512 NE k
# a = "4276440013361511"
# organ = 0
# sum_chet = 0
# sum_ne_chet = 0
# for i in range(1,len(a),2): #26403651
#     sum_chet += int(a[i])
#     #print("a[i]=", a[i])
# print("Sum_Chet = ",sum_chet)
# for i in range(0,len(a),2): #47401311
#     h = int(a[i])*2
#     print(h)
#     if h > 9:
#         print('h',h)
#         h -= 9
#         print('h - 9 = ',h)
#         sum_ne_chet += h
#         print("a[i]=", h)
#     else:
#         sum_ne_chet += h
# print("Sum_Ne_Chet = ",sum_ne_chet)
# organ = (sum_chet + sum_ne_chet)
# print(organ)
# if organ%2==0:
#     print("Корректный номер")
# else:
#     print("Некорректный номер")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""№8"""
# while 1:
#     s = input()
#
#     if not s.isalpha():
#         print("Ошибка: введите слово, состоящее только из букв.")
#         continue
#
#     e = s[0]
#     t = s[-1]
#     f = 0
#     print(f"e = {e}, t = {t}")
#     try:
#         if len(s) <= 10:
#             print(f" s = {s}")
#         else:
#             for i in range(1, len(s)-1, 1):
#                 f += 1
#             print(f" f = {e}{f}{t}")
#     except ValueError:
#         print("")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""№9"""
# from random import randint
#
# while 1:
#     n = input("Введите количество комнат: ", )
#
#     if not n.isdigit():
#         print("Ошибка: введите слово, состоящее только из букв.")
#         continue
#     n = int(n)
#     q = [0] * n
#     p = [0] * n
#     f = 0
#     for i in range(n):
#         q[i] = randint(1, 10)
#     for i in range(n):
#         p[i] = randint(1, 10)
#
#     try:
#         for i in range(n):
#             if p[i] > q[i]:
#                 print(f"p[{i}] = {p[i]} > q[{i}] = {q[i]} -> счётчик f не изменяется")
#                 continue
#         #for i in range(n):
#             elif abs(q[i] - p[i]) >= 2:
#                 f += 1
#                 print(f"p[{i}] = {p[i]}, q[{i}] = {q[i]} -> разница = 2")
#
#         print(f"Есть Место: f = {f}")
#
#     except ValueError:
#         print("ERROR")
#     except TypeError:
#         print("ERROR")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""