import telebot

bot = telebot.TeleBot('5658251229:AAGoAE5S6udqEHHouIFinjzwQcTm8I4e0BM')
ids = []
texts = {}
forms = {}


@bot.message_handler(content_types=["new_chat_members"])
def new_member(message):
    id = message.new_chat_members[0].id
    try:
        name = message.new_chat_members[0].first_name

        ids.append(id)

        mes_ = bot.send_message(message.chat.id, f"Добро пожаловать, @{name}!"
                                                 f"\nУ нас здесь круто, но есть правило: прежде чем войти, необходимо рассказать о себе"
                                                 f"\nУ тебя 240 секунд")
        texts[id] = []
        texts[id].append(mes_.id)
        mes_ = bot.send_message(message.chat.id, "Как тебя зовут?")
        texts[id].append(mes_.id)
    except:
        delete_previous(id, message)


@bot.message_handler(content_types=['text'])
def start(message):
    id = message.from_user.id
    try:
        if message.from_user.id in ids:
            forms[id] = []
            forms[id].append(message.text)
            texts[id].append(message.id)
            mes_ = bot.send_message(message.chat.id, "Из какого ты подразделения?")
            texts[id].append(mes_.id)
        bot.register_next_step_handler(message=message, callback=next_method)
    except:
        delete_previous(id, message)


@bot.message_handler(content_types=['text'])
def next_method(message):
    id = message.from_user.id
    try:
        if message.from_user.id in ids:
            forms[id].append(message.text)
            texts[id].append(message.id)
            mes_ = bot.send_message(message.chat.id, "Кем ты работаешь?")
            texts[id].append(mes_.id)
        bot.register_next_step_handler(message=message, callback=next_method_2)
    except:
        delete_previous(id, message)


@bot.message_handler(content_types=['text'])
def next_method_2(message):
    id = message.from_user.id
    try:
        if message.from_user.id in ids:
            forms[id].append(message.text)
            texts[id].append(message.id)
            mes_ = bot.send_message(message.chat.id, "Чем ты увлекаешься?")
            texts[id].append(mes_.id)
        bot.register_next_step_handler(message=message, callback=next_method_3)
    except:
        delete_previous(id, message)


@bot.message_handler(content_types=['text'])
def next_method_3(message):
    id = message.from_user.id
    try:
        if message.from_user.id in ids:
            forms[id].append(message.text)
            texts[id].append(message.id)
            bot.send_message(message.chat.id,
                             "К нам присоединился(ась) " + str(forms[id][0]) + " из " + str(
                                 forms[id][1]) + ", он(а) работает " + str(forms[id][2]) + " и увлекается " + (
                             forms[id][3]))
    finally:
        delete_previous(id, message)


def delete_previous(id, message):
    for i in texts[id]:
        bot.delete_message(message.chat.id, i)
    ids.remove(id)
    forms.__delitem__(id)
    texts.__delitem__(id)
    bot.register_next_step_handler(message=message, callback=start)


bot.polling(none_stop=True)
