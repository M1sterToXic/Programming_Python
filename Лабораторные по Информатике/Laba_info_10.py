# f = open("/Users/krivo/Downloads/lab10/file1.txt", encoding="UTF8")
# text = f.read()

# sim = ".,-()"
#
# for s in sim:
#     text = text.replace(s, "")
#
# print(text)
#
# words = text.split()
# print(words)
#
# long_word = ""
# for word in words:
#     if(len(word) > len(long_word)):
#         long_word = word
# print(long_word)
#
# small_word = words[0]
# for word in words:
#     if(len(word) < len(small_word)):
#         small_word = word
# print(small_word)
#
# delete_word = "все"
# i = 0
# while i < len(words):
#     if words[i] == delete_word or words[i] == delete_word.title():
#         words.pop(i)
#     else:
#         i += 1
# print(words)
#
# words = text.split()
# print(len(words))


# text = "kgkgkgglglglglggkf"
#
# f = open("ffff.txt", 'w')
# f.write(text)
# f.close()

# max_score = 0
# winer = ""
# with open ("/Users/krivo/Downloads/lab10/file4.txt", 'r', encoding="UTF8") as f:
#
#     for r in f:
#         h = r.split()
#         if int(h[-1]) > max_score:
#             max_score = int(h[-1])
#             winer = h[0] +' '+ h[1]
#
#     # text = f.readline()
#     #
#     # while text:
#     #     r = text.split()
#     #
#     #     if int(r[-1]) > max_score:
#     #         max_score = int(r[-1])
#     #         winer = r[0] +' '+ r[1]
#     #     text = f.readline()
#
# print(max_score)
# print(winer)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""№1"""
# max_score = 0
# max_score_prizer = 0
# winer = ""
# winer_prizer = ''
# with open("/Users/krivo/Downloads/lab10/file4.txt", 'r', encoding="UTF8") as f:
#
#     for r in f:
#         h = r.split()
#         if int(h[-1]) > max_score:
#             max_score = int(h[-1])
#             winer = h[0] + " " + h[1]
#     print("max_score = ", max_score)
#     print("winer: ", winer)
#
#     f.seek(0)
#
#     for j in f:
#         g = j.split()
#         if (max_score - int(g[-1])) == 1:
#             max_score_prizer = g[-1]
#             winer_prizer = g[0] + ' ' + g[1]
#     print("max_score_prizer = ", max_score_prizer)
#     print("winer_prizer: ", winer_prizer)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""№2"""
# found_in_file5 = 0
# word = 'Academy'
# with open("/Users/krivo/Downloads/lab10/file5.txt", 'r', encoding="UTF8") as f:
#     for r in f:
#         lines = r.split()
#         if word in lines:
#             print("Слово (Academy) в file5.txt")
#             found_in_file5 = 1
#             break
#         else:
#             print("Словa (Academy) нет в file5.txt")
#
# with open("/Users/krivo/Downloads/lab10/file6.txt", 'r', encoding="UTF8") as f:
#     if found_in_file5 == 0:
#         for line in f:
#             r = line.split()
#             if word in r:
#                 print("Слово (Academy) в file6.txt")
#                 found_in_file5 = 1
#                 break
#             else:
#                 print("Словa (Academy) нет в file6.txt")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""№3"""
# counter_e = 0
# number_e = "e"
# sum = 0.0
# all_words = []
# with open("/Users/krivo/Downloads/lab10/file6.txt", 'r', encoding="UTF8") as f:
#     for r in f:
#         words = r.split()
#         all_words.extend(words)
#
#         for word in words:
#             if 'e' in word:
#                 counter_e += 1
#
# long_line = len(all_words)
# sum = (counter_e / long_line) * 100
#
# print("Доля слов с 'e':", sum)
# print("Количество слов с 'e':", counter_e)
# print("Общее количество слов:", long_line)


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""№4"""
# man = int(input("Сколько самых популярных мужских имен вы хотите знать? "))
# wuman = int(input("Сколько самых популярных женских имен вы хотите знать? "))
# if man > 0:
#     with open("/Users/krivo/Downloads/lab10/file8.txt", 'r', encoding="UTF8") as f:
#         names = []
#         for r in f:
#             h = r.split()
#             names.append(h[0])
#     print("Man: ")
#     for i in range(man):
#         print(names[i])
#     print('\n')
#
#
# if wuman > 0:
#     with open("/Users/krivo/Downloads/lab10/file7.txt", 'r', encoding="UTF8") as f:
#         names = []
#         for r in f:
#             h = r.split()
#             names.append(h[0])
#     print("Wuman: ")
#     for i in range(wuman):
#         print(names[i])

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""№5"""
# with open("/Users/krivo/Downloads/lab10/file9.txt", 'r', encoding="UTF8") as f:
#     lines = f.readlines()
#
# count = len(lines)//2
#
# while True:
#     offer = str(input("Введите свою строку (или нажмите [стоп] для выхода): "))
#
#     if offer.lower() == "стоп":
#         print("Запись завершена.")
#         break
#
#     lines.insert(count, offer + '\n')
#
# with open("/Users/krivo/Downloads/lab10/file9.txt", 'w', encoding="UTF8") as f:
#     f.writelines(lines)
#
# with open("/Users/krivo/Downloads/lab10/file9.txt", 'r', encoding="UTF8") as f:
#     for i in f:
#         print(i)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""№6"""
# shifr = []
# deshifr = []
# h = []
# while True:
#     try:
#         question = input("Вы хотите зашифровать слово или дешифровать?: З|Д  ")
#
#         if question.lower() == "выйти":
#             print("Программа завершена.")
#             break
#
#         if question.lower() == "з":
#             word_shifr = str(input("Введите слово, которое хотите зашифровать: "))
#
#             for i in range(len(word_shifr) - 1, -1, -1):
#                 shifr.append(word_shifr[i])
#
#             result = "".join(shifr)
#             print(result)
#
#         elif question.lower() == "д":
#             word_deshifr = str(input("Введите слово, которое хотите дешифровать: "))
#
#             for letter in range(len(word_deshifr) - 1, -1, -1):
#                 deshifr.append(word_deshifr[letter])
#
#             result = ''.join(deshifr)
#             print(result)
#         else:
#             print("Введите корректные данные: ")
#
#     except ValueError:
#         print("ERROR")
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""№7"""
# import random
#
# words = []
# password = []
# with open("/Users/krivo/Downloads/lab10/file5.txt", 'r', encoding="UTF8") as f:
#     for r in f:
#         words = r.split()
#     print("Исходный список слов: ",words)
#
#     for i in range(len(words) -1, -1, -1):
#         if len(words[i]) < 3:
#             words.pop(i)
#     print("Подчищенный список слов: ", words)
#
#     clear_words = []
#     for word in words:
#         clear_word = word.replace(',', '').replace('.', '')
#         clear_words.extend(clear_word.split())
#     words = clear_words
#
#     while True:
#         random_password1 = random.choice(words)
#         upper_word = random_password1[0].upper() + random_password1[1:]
#
#         random_password2 = random.choice(words)
#         upper_word1 = random_password2[0].upper() + random_password2[1:]
#
#         password = upper_word + upper_word1
#
#         if 8 <= len(password) <= 10:
#             break
#
# print(password)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""№8"""
# try:
#     n = int(input("Введите высоту змеи: "))
#     m = int(input("Введите длину змеи: "))
#     matrix = []
#     for i in range(n):
#         if i%2 == 0:
#             matrix.append(["#"] * m)
#         else:
#             if (i // 2) % 2 == 0:
#                 row = ["."] * (m-1) + ["#"]
#             else:
#                 row = ['#'] + ["."] * (m-1)
#             matrix.append(row)
#     for i in range(n):
#         print(' '.join(matrix[i]))
#
# except ValueError:
#     print("ERROR")
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

