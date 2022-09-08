from telebot import types


def get_patterns_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)

    btn1 = types.InlineKeyboardButton(
        "1",
        callback_data='improve1')

    btn2 = types.InlineKeyboardButton(
        "2",
        callback_data='patterns1')

    btn3 = types.InlineKeyboardButton(
        "3",
        callback_data='experience1')

    btn4 = types.InlineKeyboardButton(
        "4",
        callback_data='problems1')

    btn5 = types.InlineKeyboardButton("5",
                                      callback_data='back1')

    btn6 = types.InlineKeyboardButton(
        "6",
        callback_data='back11')

    btn7 = types.InlineKeyboardButton(
        "7",
        callback_data='back2')

    btn8 = types.InlineKeyboardButton("8", callback_data='diagnostics')

    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)

    return markup
