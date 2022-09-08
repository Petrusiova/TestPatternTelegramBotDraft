from telebot import types


def get_diagnostics_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)

    btn1 = types.InlineKeyboardButton(
        "Улучшить автоматизацию тестирования - если Вы недовольны своей текущей автоматизацией или она  не дает вам желаемых преимуществ",
        callback_data='improve')
    btn2 = types.InlineKeyboardButton("Шаблоны автоматизации тестирования - если Вы только начинаете с автоматизации и никогда не делали этого раньше", callback_data='patterns')
    btn3 = types.InlineKeyboardButton("Нет опыта автоматизации - если Вы присоединяетесь к команде и не имеете опыта в автоматизации тестирования", callback_data='experience')
    btn4 = types.InlineKeyboardButton("Проблемы автоматизации тестирования - если Вы уже знаете какие у вас проблемы с автоматизацией", callback_data='problems')

    markup.add(btn1, btn2, btn3, btn4)

    return markup
