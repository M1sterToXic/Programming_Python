import tkinter as tk
from tkinter import ttk

# Фиксированные курсы валют
currency_rates = {
    'USD': {'EUR': 0.85, 'KZT': 525.16, 'RUB': 106.00, 'CNY': 7.27},
    'EUR': {'USD': 1.18, 'KZT': 552.89, 'RUB': 87.0, 'CNY': 7.61},
    'KZT': {'USD': 0.0019, 'EUR': 0.0018, 'RUB': 0.20621, 'CNY': 0.014},
    'RUB': {'USD': 0.013, 'EUR': 0.011, 'KZT': 4.95, 'CNY': 0.069},
    'CNY': {'USD': 0.14, 'EUR': 0.13, 'KZT': 72.23, 'RUB': 14.56},
}

def convert_currency():
    amount = float(amount_entry.get())
    from_currency = from_currency_combobox.get()
    to_currency = to_currency_combobox.get()

    if from_currency == to_currency:
        result_label.config(text=f"Результат: {amount:.2f} {to_currency}")
        return

    converted_amount = amount * currency_rates[from_currency][to_currency]
    result_label.config(text=f"Результат: {converted_amount:.2f} {to_currency}")

# Создание главного окна
root = tk.Tk()
root.title("Конвертор валют")
root.geometry("400x500+600+200")
root.resizable(False, False)
root.iconbitmap('')

# Метка и поле для ввода суммы
amount_label = tk.Label(root, text="Введите сумму:")
amount_label.pack(pady=5)

amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)

# Выбор исходной валюты
from_currency_label = tk.Label(root, text="Выберите исходную валюту:")
from_currency_label.pack(pady=5)

from_currency_combobox = ttk.Combobox(root, values=list(currency_rates.keys()))
from_currency_combobox.set('USD')  # Установка значения по умолчанию
from_currency_combobox.pack(pady=5)

# Выбор целевой валюты
to_currency_label = tk.Label(root, text="Выберите целевую валюту:")
to_currency_label.pack(pady=5)

to_currency_combobox = ttk.Combobox(root, values=list(currency_rates.keys()))
to_currency_combobox.set('EUR')  # Установка значения по умолчанию
to_currency_combobox.pack(pady=5)

# Кнопка конвертации
convert_button = tk.Button(root, text="Конвертировать", command=convert_currency, bg = 'pink')
convert_button.pack(pady=20)

# Метка для отображения результата
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Запуск главного цикла приложения
root.mainloop()
