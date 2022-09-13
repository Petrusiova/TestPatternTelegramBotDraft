from telebot import types


def get_diagnostics_markup():
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)

    btn1 = types.KeyboardButton(
        "Департамент 1")
    btn2 = types.KeyboardButton("Департамент 2")
    btn3 = types.KeyboardButton("Департамент 3")
    btn4 = types.KeyboardButton("Департамент 4")

    markup.add(btn1, btn2, btn3, btn4)

    return markup

def get_diagnostics_markup_2():
    markup = types.ReplyKeyboardMarkup(row_width=1)

    btn1 = types.KeyboardButton(
        "Центр экспертизы 1")
    btn2 = types.KeyboardButton("Центр экспертизы 2")
    btn3 = types.KeyboardButton("Центр экспертизы 3")
    btn4 = types.KeyboardButton("Центр экспертизы 4")

    markup.add(btn1, btn2, btn3, btn4)

    return markup
