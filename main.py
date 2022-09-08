import telebot
from telebot import types

from Diagnostics_buttons import get_diagnostics_markup
from ImproveTesting import get_improve_markup
from patterns.Pattern_problem_buttons import get_patterns_markup

bot = telebot.TeleBot('5799725631:AAEYhs-pE1MNRfYlJaMwuju3fZMEKny9WLE')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Начать диагностику", callback_data='diagnostics')
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Добро пожаловать в паттерны для автоматизации тестирования",
                     reply_markup=markup)


@bot.callback_query_handler(
    lambda call: call.data == 'diagnostics')
def layer_0(call):
    try:
        if call.data == 'diagnostics':
            markup = get_diagnostics_markup()

            msg = bot.send_message(call.message.chat.id,
                                   text="Шаблоны автоматизации тестирования наиболее полезны, если вы можете сосредоточиться на тех, которые действительно помогают решить ваши проблемы. Мы начинаем процесс диагностики, задавая несколько вопросов. Некоторые приведут вас прямо к конкретной проблеме; у других будет ряд возможных ответов, которые приведут к более подробным вопросам или к проблеме, которая лучше всего описывает вашу проблему. На любом уровне вы сможете вернуться на предыдущий уровень. Ваши ответы должны помочь определить основные проблемы. Эти вопросы содержат рекомендации по шаблонам, которые помогут вам решить ваши проблемы. В шаблонах разрешения мы даем некоторые рекомендации, но выбор того, как применять шаблоны, — это то, о чем вам нужно будет подумать в вашей собственной ситуации.",

                                   reply_markup=markup)
            bot.register_next_step_handler(msg, layer_1)
        else:
            pass
    except:
        bot.send_message(call.message.chat.id, f'🚫 | Ошибка при выполнении команды')


@bot.callback_query_handler(
    lambda call: call.data == 'improve' or call.data == 'patterns' or call.data == 'experience' or call.data == 'problems' or call.data == 'back')
def layer_1(call):
    try:

        if call.data == 'improve':
            markup = get_improve_markup()

            msg = bot.send_message(call.message.chat.id,
                                   text='Что ниже описывает наиболее насущную проблему, которую вам предстоит решить на данный момент?\n'
                                        'Если вы обнаружите, что более одного ответа подходит для вашего случая, начните с самого сложного. После того, как вы решите его, вы должны вернуться к этому вопросу и заняться следующими.',
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, layer_1)

        elif call.data == 'patterns':
            markup = get_patterns_markup()

            msg = bot.send_message(call.message.chat.id,
                                   text=open('patterns/patterns_no_prev_auto.txt', 'r').read(), parse_mode='Markdown',
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, layer_1)

    except:
        bot.send_message(call.message.chat.id, f'🚫 | Ошибка при выполнении команды')


bot.polling(none_stop=True)
