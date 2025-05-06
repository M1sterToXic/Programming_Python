""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""№1"""
# import PySimpleGUI as pygui
# try:
#     alphabet = {
#         '1': '.,?!:',
#         "2": "ABC",
#         '3': "DEF",
#         '4': 'GHI',
#         '5': 'JKL',
#         '6': 'MNO',
#         '7': 'PQRS',
#         '8': 'TUV',
#         '9': 'WXYZ',
#         '0': ' '
#     }
#
#     anti_alphabet = {}
#     for key, chars in alphabet.items():
#         for indx, char in enumerate(chars):
#             anti_alphabet[char] = key * (indx + 1)
#
#     def text_by_buttons(text):
#         result = []
#         for char in text.upper():
#             if char in anti_alphabet:
#                 result.append(anti_alphabet[char])
#         return "".join(result)
#
#     man = input("Введите сообщение: ")
#     text = text_by_buttons(man)
#     print(text)
#
# except ValueError:
#     print("Некорректные данные")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""№2"""
# import PySimpleGUI as sg
# try:
#     slovar = {
#         "1": "A,E,I,L,N,O,R,S,T,U",
#         "2": "D,G",
#         '3': 'B,C,M,P',
#         '4': 'F,H,V,W,Y',
#         '5': 'K',
#         '8': 'J,X',
#         '10': 'Q,Z'
#     }
#
#     Users = sg.popup_yes_no("Хотите начать?", font = ('Arial', 12), button_color="green")
#     if Users == 'Yes':
#         word = sg.popup_get_text(
#             "Супер! Enter a word in English please: ",
#             button_color="green",
#             font = ('Arial', 12),
#             size = (40,1)
#             )
#         if word:
#             sum = 0
#             for char in word.upper():
#                 for key, letter in slovar.items():
#                     # print(f'words {letter} key {key}')
#                     if char in letter:
#                         sum += int(key)
#                         # print(f'Буква #{char} стоит:{key}')
#
#             sg.popup_timed(f'Сумма очков из слова "{word}": {sum}', auto_close_duration=3)
#         # else:
#         #     sg.popup_timed('Вы ввели некорректные данные!',font=('Arial',12), auto_close_duration=3)
#     else:
#         print("Ну ладно 😞...")
#
# except ValueError as e:
#     print(f"Ну ладно 😞...")
# except AttributeError as f:
#     print(f"Ну ладно 😞...")
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""№3"""
# emails = {
#     "gryffindor.com": ["andrei_serov", "alexander_pushkin", "elena_belova", "k_stepanov"],
#     "hufflepuff.com": ["alena.semyonova", "ivan.polekhin", "marina_abrabova"],
#     "hogwarts.com": ["sergei.zharkov", "julia_lyubimova", "vitaliy.smirnoff"],
#     "slytherin.com": ["ekaterina_ivanova", "glebova_nastya"],
#     "ravenclaw.com": ["john.doe", "mark.zuckerberg", "helen_hunt"]
# }
# try:
#     for key, words in emails.items():
#         for word in words:
#             print(word + key, end = '')
#             print()
#         print()
# except ValueError:
#     print("ERROR")
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""4"""
import PySimpleGUI as sg
import random

keyboard = [
    [sg.Text("Random boundaries:", background_color='white', text_color='black' ,justification='center', font='10px')],
    [sg.Image('C:/Users/krivo/OneDrive/Изображения/Снимки экрана/Снимок экрана 2024-11-22 194655.png')],
    [sg.Text("START", size=(10, 1), justification="center", relief="raised", background_color="green", text_color="white"),
     sg.Text("STOP", size=(10, 1), justification="center", relief="raised", background_color="green", text_color="white")],
    [sg.InputText(key="START_INPUT", size=(11,1)),
     sg.InputText(key="STOP_INPUT", size=(11,1))],
    [sg.B("Generate", size=(10,5))],
    [sg.Push(), sg.Ok(), sg.Cancel(button_color="red")]
]

window = sg.Window("RANDOM-RULET", keyboard, element_justification='center', background_color='white', )
generate_pressed = False
while True:
    event, value = window.read()

    if event in (sg.WIN_CLOSED, "Cancel"):
        break

    if event == "Generate":
        try:
            start_value = value["START_INPUT"]
            stop_value = value["STOP_INPUT"]

            if not start_value or not stop_value:
                sg.popup_timed("Заполните оба поля!", auto_close_duration=2)
                continue

            num = int(start_value)
            num2 = int(stop_value)

            random_number = random.randint(num, num2)

            sg.popup_timed(f'Your generated number: {random_number}',auto_close_duration=1)
            generate_pressed = True

        except ValueError:
            sg.popup_timed("Введите корректные числовые значения!", auto_close_duration = 2)

    if generate_pressed and event == "Ok":
        break

    print(event, value)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
