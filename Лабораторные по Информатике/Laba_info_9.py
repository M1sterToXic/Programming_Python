
# def func(x):
#     return x**2 / (10 + x**3)
# a = -2
# b = 5
# n = 10000
# h = (b - a) / n
# f = []
# i = a
#
# while i < b:
#     f.append(func(i))
#     i += h
# sum = 0
#
# for i in f:
#     sum += h * i
# print(f"{sum:.2f}")


# n = int(input("Введите кол-во строк", ))
# m = int(input("Введите кол-во столбцов",))
#
# A = []
# for i in range(n):
#     A.append([0] * m)
# print(A)
# # for i in range(len(A)):
# #     for j in range(len(A[i])):
# #         print(A)

# A = [
#     [1, 2, 3, 4],
#     [5, 6, 1, 1],
#     [2, 5, 1, 0],
#     [4, 3, 2, 1]
#
# ]
#
#
# for i in range(len(A)):
#     print(A[i][0], A[i][-1])

# A = [
#     [1, 2, 3, 5, 6],
#     [2, 4, 5, 7, 7],
#     [9, 8, 7, 6, 5]
#
# ]
#
# count = 0
#
# for i in range(len(A)):
#     for j in range(len(A[i])):
#         if A[i][j] == 7:
#             count += 1
# print(count)

# A = [
#     [1, 2, 3, 5, 6],
#     [2, 4, 5, 7, 7],
#     [9, 8, 7, 6, 5]
# ]
#
# max = A[0][0]
# max_i = 0
# max_j = 0
#
# for i in range(len(A)):
#     for j in range(len(A[i])):
#         if A[i][j] > max:
#             max = A[i][j]
#             max_i = i + 1
#             max_j = j + 1
# print(max, max_i, max_j)

# t = [[-8, 14, -19, -18],
# [25, 28, 26, 20],
# [11, 18, 20, 25]]
#
# print("Температура на 2 метеостанции в 4 день была: ", t[1][-1])
# print("Температура на 3 метеостанции в 2 день была: ", t[-1][1])
# for i in range(len(t)):
#     print(t[i][1])
#
# sum = 0
# for i in range(len(t[2])):
#     sum += t[2][i]
# sum /= len(t[2])
# print(sum)




"""№1"""
# def trapezoidal_rule(f, a, b, N):
#
#     h = (b - a) / N
#
#     integral = 0.5 * (f(a) + f(b))
#
#     for i in range(1, N):
#         x = a + i * h
#         integral += f(x)
#     integral *= h
#
#     return integral
#
#
# def f(x):
#     return x ** 2 / (10 + x ** 3)
#
#
# a = -2
# b = 5
#
# for N in [10, 100, 1000]:
#     approximation = trapezoidal_rule(f, a, b, N)
#     print(f"Приближенное значение интеграла для N = {N}: {approximation}")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""№2"""
# from random import choice
#
# # создание матрицы 3 на 3, в которой находятся нули
# m = []
# for i in range(3):
#     m.append([0] * 3)
#
# #заполнение рандомными элементами из списка матрицу
# #так сделано для того, чтобы элементы в матрицы не повторялись
# #то есть, как только вы добавляете элемент в матрицу, он удалется из списка number и вы не можете его добавить снова
# while 1:
#     try:
#         number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#         for i in range(3):
#             for j in range(3):
#                 m[i][j] = choice(number)
#                 number.remove(m[i][j])
#         if ((m[0][0] + m[1][1] + m[2][2]) == 15) and \
#            ((m[0][2] + m[1][1] + m[2][0]) == 15) and \
#            ((m[0][1] + m[1][1] + m[2][1]) == 15) and \
#            ((m[1][0] + m[1][1] + m[1][2]) == 15):
#             for i in range(3):
#                 for j in range(3):
#                     print(m[i][j], end=" ")
#                 print()
#             break
#     except ValueError:
#         print("ERROR")
#
# #
# # тут надо проверить соответствует ли данная матрица требованием магического квадрата
# # если да, то вывести на экран
# # если нет, то заново заполнять матрицу


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""№3"""
# import math
# n = int(input("Введите кол-во сокровищ: "))
#
# t_map = [
#     [1, 2],
#     [3, 5],
#     [5, 6],
#     [7, 8]
# ]
# Alecsandr_map = []
#
# a1 = int(input("Введите 1 координату Александра: "))
# Alecsandr_map.append(a1)
# a2 = int(input("Введите 2 координату Александра: "))
# Alecsandr_map.append(a2)
#
# if n == 1:
#     del t_map[1:4]
#     print('Координаты сокровищ: ',t_map[0][0])
# elif n == 2:
#     del t_map[2:4]
#     print('Координаты сокровищ: \n')
#     for i in range(2):
#         for j in range(2):
#             print(t_map[i][j], end=" ")
#         print()
# elif n == 3:
#     del t_map[3:4]
#     print('Координаты сокровищ: \n')
#     for i in range(3):
#         for j in range(2):
#             print(t_map[i][j], end=" ")
#         print()
# elif n == 4:
#     print('Координаты сокровищ: \n')
#     for i in range(4):
#         for j in range(2):
#             print(t_map[i][j], end=" ")
#         print()
#
# print("Координаты Александра",Alecsandr_map)
#
# def distance(x1, y1, x2, y2):
#     return math.sqrt((x2-x1) ** 2 + (y2 -y1) ** 2)
#
# distances = []
#
# for i in t_map[:n]:
#     dist = distance(Alecsandr_map[0], Alecsandr_map[1], i[0], i[1])
#     distances.append(dist)
#
# min_d_index = distances.index(min(distances))
# print("Координаты ближайшего сокровища:", t_map[min_d_index])

# # Координаты Александра: (2, 3).
# # Сокровища: (1, 2), (3, 5), (5, 6), (7, 8).
# # Расстояние от (2, 3) до (1, 2) равно примерно 1.41.
# # Расстояние от (2, 3) до (3, 5) равно примерно 2.24.
# # Расстояние от (2, 3) до (5, 6) равно примерно 4.24.
# # Расстояние от (2, 3) до (7, 8) равно примерно 7.81.


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""№4"""
# menu = [
# ["Пицца Маргарита", ["мука", "томаты", "сыр", "базилик"], 10],
# ["Салат Цезарь", ["салат", "курица", "сыр", "сухарики"], 8],
# ["Суп Томатный", ["томаты", "лук", "морковь", "картофель"], 6]
# ]
#
# while 1:
#     try:
#         print("\n")
#         l = int(input("""Здравствуйте, что бы вы хотели?
#         1. Отобразить меню ресторана.
#         2. Найти блюдо по названию и отобразить его ингредиенты и цену. (Вы вводите название блюда).
#         3. Добавить новое блюдо в меню.
#         4. Изменить цену блюда (Вы вводите название и новую цену).
#         5. Нечего.
#         Выберете цифру: """, ))
#         #Отабражаю меню
#         if l == 1:
#             print("\nМеню следующее... :")
#             for item in menu:
#                 print(f"{item[0]}: Ингредиенты ({','.join(item[1])}); Цена - {item[2]}$")
#
#         #Ищу блюдо по запросу
#         elif l == 2:
#             print("\n")
#             food = input("Пожалуйста введите название блюда: ")
#
#             found = False
#             for item in menu:
#                 if item[0].lower() == food.lower():
#                     print(f"\nБлюдо: {item[0]}")
#                     print(f"\nИгредиенты: {','.join(item[1])}")
#                     print(f"\nЦена: {item[2]}$")
#                     found = True
#                     break
#
#             if not found:
#                 print("Блюдо не найдено в меню.")
#
#         #Добавляю новое блюдо
#         elif l == 3:
#             print("\n")
#
#             bludo = input("Введите название нового блюда: ")
#             ingredients = input("Напишите ингридиенты (через запятую): ").split(", ")
#             price = int(input("Введите цену нового блюда: "))
#
#             menu.append([bludo, ingredients, price])
#             print("Блюдо добавлино в меню!",)
#
#         #Меняю цену блюда
#         elif l == 4:
#             print('\n')
#             bludo = input("Введите название блюда: ")
#             new_price = int(input("Введите новую цену блюда: ",))
#
#             found = False
#             for item in menu:
#                 if item[0].lower() == bludo.lower():
#                     item[2] = new_price
#                     print(f"Цена блюда '{item[0]}' успешно обновлена.")
#                     found = True
#                     break
#
#             if not found:
#                 print("Блюдо не найдено в меню.")
#
#         #Выход из цикла
#         elif l == 5:
#             print("Досвидания!")
#             break
# # h = menu.index(k)
# # print(menu[h])
#
#
#
#
#     except ValueError:
#         print("ERROR")
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""№5"""
# n = int(input("Введите кол-во строк: "))
# m = int(input("Введите кол-во строк: "))
# matrix = []
# print('\n')
# for i in range(n):
#     row = []
#     for j in range(m):
#         f = "".join([str(i+1),str(j+1)])
#         row.append(f)
#         # print("value",value)
#         # print("row",row)
#     matrix.append(row)
# for row in matrix:
#     print(*row)
# print('\n')
# for j in range(m):
#     for i in range(n):
#         print(matrix[i][j], end = ' ')
#     print()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""№6"""
# n = int(input("Введите размер массива: ",))
# m = n
# matrix = []
# count = 1
# for i in range(n):
#     row = []
#     for j in range(m):
#         row.append(count)
#         count += 1
#     matrix.append(row)
# for i in range(n):
#     for j in range(m):
#         print(matrix[i][j], end = ' ')
#     print()
#
# for j in range(n):
#     matrix[j][j], matrix[n - 1 - j][j] = matrix[n - 1 -j][j], matrix[j][j]
#
# print('\n')
# for row in matrix:
#     print(' '.join(map(str, row)))
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""№7"""
# from random import randint
# n = int(input("Введите кол-во рядов: "))
# m = int(input("Введите кол-во мест в рядах: ",))
# matrix = []
# row = []
#
# print("Занятость мест в зале (1 - занято, 0 - свободно):")
# for i in range(n):
#     row = [randint(0,1) for _ in range(m)]
#     matrix.append(row)
# for i in range(n):
#     for j in range(m):
#         print(matrix[i][j], end = ' ')
#     print()
#
#
# k = int(input("Введите кол-во людей: ",))
# quantity = [1] * k
# count = []
# for i in range(n):
#     free_seats = 0
#     for j in range(m):
#         if matrix[i][j] == 0:
#             free_seats += 1
#             if free_seats == k:
#                 count.append(i + 1)
#                 break
#         else:
#             free_seats = 0
#     if count:
#         break
#
#
# if count:
#     print(f"Можно посадить группу в ряду номером: {min(count)}")
# else:
#     print("Подходящего рядов нет. 0")
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""№8"""
# n = int(input("Введите кол-во строк: ",))
# m = int(input("Введите кол-во столбцов: ",))
# matrix = []
#
# for i in range(n):
#     matrix.append([0] * m)
# #Инициализация Матрицы
# print('\n')
# for i in range(n):
#     for j in range(m):
#         print(matrix[i][j], end = ' ')
#     print()
#
# for i in range(n):
#     for j in range(m):
#         matrix[0][j] = 1
#         matrix[i][0] = 1
# #Инициализация матрицы
# print('\n')
# for i in range(n):
#     for j in range(m):
#         print(matrix[i][j], end = ' ')
#     print()
#
# for i in range(1,n):
#     for j in range(1,m):
#         matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
#
# #Инициализация матрицы
# print('\n')
# for i in range(n):
#     for j in range(m):
#         print(matrix[i][j], end = ' ')
#     print()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""№9"""
# import random
# def print_board(board):
#     # печатем игровое поле
#     for row in board:
#         print(' '.join(row))
#
# def game_field():
#     # Создаём пустое поле 4х4
#     field = [[' * ' for _ in range(4)] for _ in range(4)]
#
#     #Размещение кораблей
#     ships = 0
#     while ships < 4:
#         x, y = random.randint(0,3), random.randint(0, 3)
#         if field[x][y] == ' * ':
#             field[x][y] = " S "
#             ships += 1
#
#     #Размещение Бомбы
#     bomb = False
#     while not bomb:
#         x, y = random.randint(0, 3), random.randint(0, 3)
#         if field[x][y] == ' * ':
#             field[x][y] = " B "
#             bomb = True
#
#     return field
#
# def play_game():
#     #Поле
#     board = game_field()
#
#     #Кол-во выстрело
#     steps = 0
#
#     #Найдено кораблей
#     ships_dead = 0
#
#     while ships_dead < 4:
#         print('\nТекущее поле: ')
#         visible_board = [[' * ' if cell == ' S ' or cell == ' B ' else cell for cell in row] for row in board]
#         print_board(visible_board)
#
#         try:
#             # Запрос координат
#             x, y = map(int, input("Введите координаты выстрела (например, 1 2): ").split())
#
#             x -= 1
#             y -= 1
#
#             if not (0 <= x < 4 and 0 <= y < 4):
#                 print("Некорректные координаты, попробуйте ещё раз")
#                 continue
#
#             if board[x][y] == ' S ':
#                 print(f'Есть пробите! ({x + 1}, {y + 1})')
#                 board[x][y] = ' X '
#                 ships_dead += 1
#             elif board[x][y] == " B ":
#                 print(f"Ну всё, доигрались! ({x + 1}, {y + 1})")
#                 print("Игра окончена!")
#                 break
#             else:
#                 print("Мимо!")
#
#             steps +=1
#
#
#         except ValueError:
#             print("ERROR")
#
#     if ships_dead == 4:
#         print(f"\nПоздравляем! Вы нашли все корабли за {steps} выстрелов.")
#
# play_game()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""