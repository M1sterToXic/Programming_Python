import PySimpleGUI as sg

# Фиксированные курсы валют
currency_rates = {
    'USD': {'EUR': 0.85, 'KZT': 525.16, 'RUB': 106.00, 'CNY': 7.27},
    'EUR': {'USD': 1.18, 'KZT': 552.89, 'RUB': 87.0, 'CNY': 7.61},
    'KZT': {'USD': 0.0019, 'EUR': 0.0018, 'RUB': 0.20621, 'CNY': 0.014},
    'RUB': {'USD': 0.013, 'EUR': 0.011, 'KZT': 4.95, 'CNY': 0.069},
    'CNY': {'USD': 0.14, 'EUR': 0.13, 'KZT': 72.23, 'RUB': 14.56},
}

# Определение интерфейса
layout = [
    [sg.Text("Введите сумму:")],
    [sg.InputText(key='-AMOUNT-', size=(20, 1))],

    [sg.Text("Выберите исходную валюту:")],
    [sg.Combo(list(currency_rates.keys()), default_value='USD', key='-FROM-')],

    [sg.Text("Выберите целевую валюту:")],
    [sg.Combo(list(currency_rates.keys()), default_value='EUR', key='-TO-')],

    [sg.Button("Конвертировать", button_color=('white', 'pink'))],
    [sg.Text("", size=(30, 1), key='-RESULT-')],
]

# Создание окна
window = sg.Window("Конвертер валют", layout, size=(300, 250), element_justification='c')

# Основной цикл
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "Конвертировать":
        try:
            amount = float(values['-AMOUNT-'])
            from_currency = values['-FROM-']
            to_currency = values['-TO-']

            if from_currency == to_currency:
                result_text = f"Результат: {amount:.2f} {to_currency}"
            else:
                converted_amount = amount * currency_rates[from_currency][to_currency]
                result_text = f"Результат: {converted_amount:.2f} {to_currency}"
            window['-RESULT-'].update(result_text)

        except ValueError:
            window['-RESULT-'].update("Введите корректное число!")

# Закрытие окна
window.close()
