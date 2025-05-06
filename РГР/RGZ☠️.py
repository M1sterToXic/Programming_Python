import PySimpleGUI as sg
import random
import re

with open("PNGG.txt", 'r') as f:
    lines = f.readlines()

stone_base64 = lines[0]
paper_base64 = lines[2]
scissor_base64 = lines[1]
Geyson = lines[3]

"""Первое окно: ввод имени и кол-во раундов"""
layout = [[sg.Text('Введите ваше имя:', text_color='black', background_color="#196c4f", font=15)],
          [sg.Input(key='-NAME-', background_color='green', font=15, text_color='black', size=(20, 1))],
          [sg.Text('Введите количество раундов, или оставьте поле пустым для бесконечной игры :)', text_color='black', background_color="#196c4f", font=15)],
          [sg.Input(key='-RAUNDS-', background_color='green', font=15, text_color='black', size=(20, 1))],
          [sg.Button("START", size=(25, 5), button_color='green', key="start")]]

window = sg.Window('Игра "Камень-Ножницы-Бумага!"', layout, background_color='#196c4f', element_justification='center')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        exit()
    if event == 'start':
        user = values.get('-NAME-', '').strip()
        if not user:
            user = "Player"

        rounds_limit = values.get("-RAUNDS-", '').strip()
        if rounds_limit:
            """Проверка на корректный ввод"""
            if not re.match(r'^\d+$', rounds_limit):
                sg.popup_error("Рофл не принят. Всего доброго!",
                               background_color='#196c4f',
                               keep_on_top=True)
                exit()
            rounds_limit = int(rounds_limit)
            if rounds_limit <= 0:
                sg.popup_error("Рофл не принят. Всего доброго!",
                               background_color='#196c4f',
                               keep_on_top=True)
                exit()
        else:
            rounds_limit = None

        window.close()
        break

"""Второе окно: игра"""
player_score = 0
pc_score = 0
rounds_played = 0

Buttons = [
    [sg.Column([[sg.Text(f"Computer VS {user}", background_color='black', text_color='white', font=20, justification='center')]],
               justification='center', expand_x=True)],
    [sg.Column([[sg.Text("СЧЁТ", background_color='#196c4f', text_color='white', font=20, justification='center')]],
               justification='center', vertical_alignment='center')],
    [sg.Text(f"Computer :[0 : 0]: {user}", background_color='black', text_color='#66FF00', font=20, justification='center', key='score')]
]

pc_image = [[sg.Text("Ход компьютера", font=("Arial", 25, "bold"), justification='center')],
            [sg.Image("", subsample=2, key="pc_hod")]]
player_image = [[sg.Text("Ваш ход", font=("Arial", 25, "bold"), justification='center')],
                [sg.Image("", subsample=2, key="player_hod")]]

Buttons_play = [[sg.Button('', image_data=paper_base64, key="paper", tooltip="Бумага"),
                 sg.Button('', image_data=stone_base64, key="stone", tooltip="Камень"),
                 sg.Button('', image_data=scissor_base64, key='scissors', tooltip="Ножницы")]
                ]

layout_game = [
    [sg.Column(pc_image, element_justification="center", vertical_alignment='center', expand_x=True, expand_y=True),
     sg.Column(player_image, element_justification="center", vertical_alignment='center', expand_x=True, expand_y=True)],
    [sg.Column(Buttons, justification='center')],
    [sg.Column(Buttons_play, justification='center', vertical_alignment='bottom')]
]

window_game = sg.Window("RGZ", layout_game, finalize=True)

def winner_game(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'draw'
    elif (player_choice == 'paper' and computer_choice == 'stone') or \
         (player_choice == 'stone' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return 'player'
    else:
        return 'computer'

while True:
    event, values = window_game.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event in ["paper", "stone", "scissors"]:
        rounds_played += 1

        """Изображения для игрока"""
        player_img = {
            "paper": paper_base64,
            "stone": stone_base64,
            "scissors": scissor_base64
        }[event]

        comp_choice = random.choice(["paper", "stone", "scissors"])
        comp_img = {
            "paper": paper_base64,
            "stone": stone_base64,
            "scissors": scissor_base64
        }[comp_choice]

        window_game["player_hod"].update(data=player_img)
        window_game["pc_hod"].update(data=comp_img)

        winner = winner_game(event, comp_choice)
        if winner == 'player':
            player_score += 1
        elif winner == 'computer':
            pc_score += 1

        window_game['score'].update(f"Computer [{pc_score} : {player_score}] {user}")

        print(f"You selected: {event}, Computer selected: {comp_choice}")
        print(f"Winner: {winner}")

        date = (f"Comp:{pc_score} | Player:{player_score}")
        with open("Score.txt", 'w') as file:
            file.write(date)

        if rounds_limit is not None and rounds_played >= rounds_limit:
            if player_score > pc_score:
                result_message = "Вы победили!"
                result_color = '#66FF00'
            elif player_score < pc_score:
                result_message = "Вы проиграли!"
                result_color = '#FF0000'
            else:
                result_message = "Ничья!"
                result_color = '#FFFF00'

            sg.popup(
                result_message,
                f"Конечный счет: Computer [{pc_score}] : [{player_score}] {user}",
                keep_on_top=True,
                background_color='#5a5f59',
                text_color=result_color,
                button_color=('black', 'green')
            )
            break

window_game.close()
