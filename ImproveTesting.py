from telebot import types


def get_improve_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)

    btn1 = types.InlineKeyboardButton(
        "Отсутствие поддержки (со стороны руководства, тестировщиков, разработчиков и т. д.)",
        callback_data='improve1')

    btn2 = types.InlineKeyboardButton(
        "Нехватка ресурсов (персонал, программное обеспечение, оборудование, время и т. д.)",
        callback_data='patterns1')

    btn3 = types.InlineKeyboardButton(
        "Отсутствие направления (что автоматизировать, какую архитектуру автоматизации реализовать и т. д.)",
        callback_data='experience1')

    btn4 = types.InlineKeyboardButton(
        "Недостаток специальных знаний (окупаемость инвестиций (ROI), отставание от графика и т. д.)",
        callback_data='problems1')

    btn5 = types.InlineKeyboardButton("Ожидания руководства в отношении автоматизации не оправдались",
                                      callback_data='back1')

    btn6 = types.InlineKeyboardButton(
        "Не оправдались ожидания в отношении автоматизированного выполнения тестов (скрипты ненадежны или слишком медленны, тесты не могут выполняться без присмотра и т. д.)",
        callback_data='back11')

    btn7 = types.InlineKeyboardButton(
        "Ожидания по обслуживанию не оправдались (недокументированные данные или скрипты, отсутствие контроля версий и т. д.)",
        callback_data='back2')

    btn8 = types.InlineKeyboardButton("Вернуться к началу диагностики", callback_data='diagnostics')

    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)

    return markup
