"""№1"""

# list = [["woman", 'child'], ["man"], ['captain']]
#
# while True:
#     a = []
#     num = input("Введите кол-во экипажа: ")
#     for i in range(int(num)):
#         while True:
#             f = input(f"Имя {i+1} экипажа: ")
#             g = f.split()
#             if len(g) == 2: break
#             print("Некоректные данные!")
#         a.append(g)
#     for i in list:
#         for j in a:
#             if j[1] in i:
#                 print(j[0])
#     # print(a)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""№2"""
# import random
#
# while 1:
#     a = ["Q"]
#     f = int(input("Введите кол-во сообщений: "))
#     for i in range(f-1):
#         a.append(random.choice("QA"))
#     # if a.count("QA") % 2 == 0:
#     #     print('+')
#     if a.count("Q") != a.count("A"):
#         print('-')
#     else:
#         print("+")
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""№3"""
# import PySimpleGUI as sg
#
# c_image = [[sg.Image("bio.png")]]
# c_input = [[sg.Text("Введите количество бактерий:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="micro")],
#            [sg.Text("Количество секунд:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="count")],
#            [sg.Text("Результат:", font="Arial 20"), sg.Input(font="Arial 20", readonly=True, size=(5, 0), key="res")],
#            [sg.Button("Рассчитать", font="Arial 20")]]
#
# layout = [
#     [sg.Column(c_image), sg.VSeperator(), sg.Column(c_input, justification='right')]
# ]
#
# window = sg.Window("Калькулятор бактерий", layout)
#
# while 1:
#
#     event, value = window.read()
#
#     if event == sg.WIN_CLOSED:
#         break
#
#     micro = value["micro"]  #здесь хранится количество бактерий изначально
#     count = value["count"]  #здесь хранится количество секунд для которых требуется рассчитать
#     res = 0                 #здесь будет храниться результат
#
#
#     #код надо писать здесь
#     k = 2
#     b = 4
#     res = int(micro)
#     for i in range(int(count)):
#         res = k*res + b
#
#     if event == "Рассчитать":
#         window["res"].update(res)
#
#
# window.close()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""№4"""
# import PySimpleGUI as sg
#
# def binary(num, bits=8):
#     return f'{num & ((1 << bits) - 1):0{bits}b}'
#
# def dvoi_cod(num):
#     if num >= 0:
#         return '0' + binary(num, 7)
#     else:
#         return '1' + binary(abs(num), 7)
#
# def reverse(num):
#     if num >= 0:
#         return '0' + binary(num, 7)
#     else:
#         inverse = ''.join('1' if bits == '0' else '0' for bits in binary(abs(num), 7))
#         return '1' + inverse
#
# def complement(num):
#     if num >= 0:
#         return '0' + binary(num, 7)
#     else:
#         rev = int(reverse(num)[1:], 2) + 1
#         return '1' + f'{rev:07b}'
#
# Image = [[sg.Image("Digital_rain_animation_small_letters_shine.gif", background_color='black', key='-GIF-')]]
# Buttons = [
#     [sg.Text("Введите ваше число:", background_color="black"), sg.Input(size=(9, 1), enable_events = True, key='num')],
#     [sg.Text("В прямом виде:", background_color='black'), sg.Input(size=(9, 1), readonly=True, key='dvoi')],
#     [sg.Text("В дополнительном виде:", background_color='black'), sg.Input(size=(9, 1), readonly=True, key='dop')],
#     [sg.Text("В обратном виде:", background_color='black'), sg.Input(size=(9, 1), readonly=True, key='obr')]
# ]
#
# layout = [[sg.Column(Image)], [sg.Column(Buttons, background_color='black')]]
#
# window = sg.Window("Реальное обновление", layout, background_color='black')
#
# error_shown = False
#
#
# while True:
#     event, values = window.read(timeout=0)
#
#     if event == sg.WINDOW_CLOSED:
#         break
#
#     window['-GIF-'].update_animation("Digital_rain_animation_small_letters_shine.gif", time_between_frames=100)
#
#     from string import digits
#
#     if event == "num":
#         num_str = values['num']
#         if not num_str or num_str == "-":
#             window['dvoi'].update('')
#             window['dop'].update('')
#             window['obr'].update('')
#             continue
#
#         for c in num_str[int(num_str[0] == "-"):]:
#             if c not in digits:
#                 num_str = num_str.replace(c, "")
#                 window['num'].update(num_str)
#
#         if not num_str or num_str == "-":
#             window['dvoi'].update('')
#             window['dop'].update('')
#             window['obr'].update('')
#             continue
#
#         num = int(num_str)
#         if -128 <= num <= 127:
#             dvoi = dvoi_cod(num)
#             dop = complement(num)
#             obr = reverse(num)
#             window['dvoi'].update(dvoi)
#             window['dop'].update(dop)
#             window['obr'].update(obr)
#         else:
#             window['dvoi'].update('')
#             window['dop'].update('')
#             window['obr'].update('')
#
#
#
# window.close()




