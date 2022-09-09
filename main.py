﻿import telebot

bot = telebot.TeleBot('5799725631:AAEYhs-pE1MNRfYlJaMwuju3fZMEKny9WLE')


@bot.message_handler(commands=['start'])
def start(message):
    msg = bot.send_message(message.chat.id,
                           text="Добро пожаловать в паттерны для автоматизации тестирования\n\n"
                                "<b>Шаблоны автоматизации тестирования</b> наиболее полезны, если вы можете сосредоточиться на тех, \n"
                                "которые действительно помогают решить ваши проблемы. Мы начинаем процесс диагностики:\n\n"

                                "/improve - <b>Улучшение автоматизации тестирования</b> - если Вы недовольны своей текущей автоматизацией или она  не дает вам желаемых преимуществ\n\n"
                                "/no_previous_test_automation - <b>Автоматизации еще не было</b> - если Вы только начинаете с автоматизации и никогда не делали этого раньше\n\n"
                                "/limited_experience - <b>Нет опыта в автоматизации тестирования</b> - если Вы присоединяетесь к команде и не имеете опыта в автоматизации тестирования\n\n"
                                "/test_automation_issues - <b>Конкретные проблемы в автоматизации</b> -если Вы уже знаете какие у вас проблемы с автоматизацией\n\n"
                           , parse_mode='html')


@bot.message_handler(commands=['improve'])
def improve(message):
    msg = bot.send_message(message.chat.id,
                           text="<b>Улучшение автоматизации тестирования</b>\n\n"
                                "Что ниже описывает самую насущную проблему, которую вам нужно решить в данный момент?\n\n"

                                "/lack_of_support - <b>Отсутствие поддержки</b> (со стороны руководства, тестировщиков, разработчиков и т. д.)\n\n"
                                "/lack_of_resources - <b>Нехватка ресурсов</b> (персонал, ПО, оборудование, время и т. д.)\n\n"
                                "/lack_of_direction -<b>Отсутствие направления</b> (что автоматизировать, какую архитектуру реализовать и т. д.)\n\n"
                                "/lack_of_specific_knowledge - <b>Отсутствие конкретных знаний</b> (как протестировать ПО (SUT), какие использовать инструменты, как на самом деле работает автоматизация, написать поддерживаемую автоматизацию и т. д.)\n\n"
                                "/management_expectations_not_met - <b>Ожидания руководства в отношении автоматизации не оправдались</b> (окупаемость инвестиций (ROI), отставание от графика и т. д.)\n\n"
                                "/automation_exec_expectations_not_met - <b>Ожидания по автоматизированному выполнению тестов не оправдались</b> (скрипты ненадежны или слишком медленны, тесты не могут выполняться самостоятельно и т. д.)\n\n"
                                "/automation_maintenance_expectations_not_met - <b>Ожидания по техническому обслуживанию не выполнены</b> (недокументированные данные или сценарии, отсутствие контроля версий и т. д.)\n\n"

                                "/start - Вернуться к началу процесса диагностики"
                           , parse_mode='html')


@bot.message_handler(commands=['no_previous_test_automation'])
def no_previous_test_automation(message):
    msg = bot.send_message(message.chat.id,
                           text=open('patterns/patterns_no_prev_auto.txt', 'r').read() +

                                "\n\n/set_clear_goals - <b>Установите четкие цели.</b> Эта модель имеет решающее значение. Он должен быть применен в начале любых больших или малых усилий по автоматизации\n\n"
                                "/management_support - <b>Поддержка менеджмента.</b> Важно чтобы поддержка автоматизации НЕ выполнялась в одиночку во избежании остановок т.к. информацией владеет только 1 человек\n\n"
                                "/test_automation_owner - <b>Назначенный владелец</b> не только для внедрения автоматизации тестирования, но и для поддержания ее работы в будущем\n\n"
                                "/dedicated_resources - <b>Специальные ресурсы.</b> Эта модель особенно важна в начале новых усилий по автоматизации. В зависимости от размера вашей автоматизации вы можете позже ослабить ее использование.\n\n"
                                "/right_tools - <b>Правильные инструменты.</b> Этот шаблон необходим не только для длительной автоматизации, но и для быстрых исправлений\n\n"
                                "/automation_roles - <b>Роли автоматизации.</b> Используйте этот шаблон для заполнения ролей, необходимых для разработки тестового программного обеспечения автоматизации. Если возможно, используйте /whole_team_approach - <b>усилия всей команды</b> - и по необходимости /get_training - проводите <b>обучение для своих сотрудников.</b>\n\n"
                                "/plan_support_activities - <b>Планирование деятельности по поддержке.</b> Не забудьте применить этот шаблон, если вы хотите иметь возможность соблюдать свои расписания. Недостающая поддержка со стороны специалистов может довольно эффективно заземлить проект!\n\n"
                                "/maintainable_testware - <b>Поддерживаемое тестовое обеспечение.</b> Применяйте этот шаблон с самого начала, если вы хотите, чтобы ваши усилия по автоматизации были длительными, а расходы на техническое обслуживание были низкими.\n\n"
                                "/automate_whats_needed - <b>Автоматизируйте то что нужно.</b> Этот шаблон показывает вам, как выбрать функции, наиболее достойные автоматизации\n\n"
                                "/take_small_steps - <b>Маленькие шаги.</b> Эта модель особенно важна в начале, но ее всегда следует иметь в виду\n\n"
                                "/unattended_test_execution - <b>Необратимое выполнение теста.</b> Этот шаблон дает вам последние предложения о том, как закончить с автоматизацией тестирования\n\n"

                                "/start - Вернуться к началу процесса диагностики"
                           , parse_mode='html')


@bot.message_handler(commands=['limited_experience'])
def limited_experience(message):
    msg = bot.send_message(message.chat.id,
                           text=open('limitedExperience/limitedExperience.txt', 'r').read() +
                                "\n/tester - <b>Тестер</b>\n\n"
                                "/developer - <b>Разработчик</b>\n\n"
                                "/test_manager - <b>Тест-менеджер</b>\n\n"

                                "Наиболее рекумендуемые:\n\n"

                                "/check_to_learn - <b>Проверка</b> - позвольте новым членам команды учиться, проверяя работоспособность существующего тестового ПО\n\n"
                                "/document_the_testware - <b>Документация тестового обеспечения</b> - используйте с самого начала автоматизации\n\n"
                                "/do_a_pilot - <b>Подготовка пилота</b> - используйте при запуске автоматизации, чтобы члены команды могли научиться\n\n"
                                "/get_training - <b>Обучение</b> -  после выбора инструментов и архитектуры, а также для тестировщиков, чтобы научиться писать тест-кейсы, подходящие для автоматизации.\n\n"
                                "/ask_for_help - <b>Просьба о помощи</b> - просить о помощи - это не трудно\n\n"

                                "Также полезно:\n\n"

                                "/pair_up - <b>Модель выбора</b> - когда новички должны интегрироваться в команду как можно быстрее\n\n"
                                "/take_small_steps - <b>Маленькие шаги</b> - Москва не сразу строилась\n\n"
                                "/steel_thread - <b>Стальная нить</b> - хороший шаблон для обучения автоматизации тестирования через SUT\n\n"
                                "/prefer_familiar_solutions - <b>Знакомые решения</b> - если члены команды уже используют инструменты или процессы, которые могут быть успешно применены также к проекту автоматизации тестирования.\n\n"

                                "/start - Вернуться к началу процесса диагностики"

                           , parse_mode='html')


@bot.message_handler(commands=['test_automation_issues'])
def limited_experience(message):
    msg = bot.send_message(message.chat.id,
                           text=open('testAutoIssues/testAutoIssues.txt', 'r').read() +
                                "\n/inefficient_failure_analysis - <b>Неэффективный анализ сбоев</b>\n\n"
                                "/hard_to_automate - <b>Трудности автоматизации</b>\n\n"
                                "Однако одной из основных причин неудачи является сосредоточение исключительно на технических аспектах. Другие проблемы связаны с тем, как вы работаете, такие как:\n\n"
                                "/late_test_case_design - <b>Поздний тест-дизайн</b>\n\n"
                                "/stalled_automation - <b>Утерянная автоматизация</b> - когда автоматизация, кажется, начинается хорошо, но затем останавливается\n\n"
                                "/high_roi_expectations - <b>Ожидание высокой рентабельности</b>\n\n"

                                "Некоторые проблемы могут возникнуть из-за технических или управленческих проблем."
                                "Мы классифицируем проблемы на следующие категории:\n\n"

                                "/process_issues - <b>Проблемы процесса</b> - как мы работаем с автоматизированными тестами и инструментами\n\n"
                                "/management_issues - <b>Проблемы управления</b> - вопросы управления, кадрового расписания, целей (необходимо время, деньги или люди для исправления)\n\n"
                                "/design_issues - <b>Проблемы проектирования</b> - архитектура тестового программного обеспечения, включая ремонтопригодность\n\n"
                                "/execution_issues - <b>Проблемы с выполнением</b> - запуск тестов в их автоматизированной форме\n\n"

                                "Обратите внимание на:\n\n"

                                "/failure_patterns - <b>Шаблоны отказов</b> - также являются своего рода проблемой, потому что они описывают поведение, которое, если не будет признано вовремя, может поставить под угрозу даже, казалось бы, успешные проекты автоматизации тестирования. Их также называют 'антипаттернами'.\n\n"

                                "/start - Вернуться к началу процесса диагностики"

                           , parse_mode='html')


bot.polling(none_stop=True)

# @bot.callback_query_handler(
#     lambda call: call.data == 'diagnostics')
# def layer_0(call):
#     try:
#         if call.data == 'diagnostics':
#             markup = get_diagnostics_markup()
#
#             msg = bot.send_message(call.message.chat.id,
#                                    text="Шаблоны автоматизации тестирования /наиболее /полезны, если вы можете сосредоточиться на тех, "
#                                         "которые действительно помогают решить ваши проблемы. Мы начинаем процесс диагностики, "
#                                         "задавая несколько вопросов. Некоторые приведут вас прямо к конкретной проблеме; "
#                                         "у других будет ряд возможных ответов, которые приведут к более подробным вопросам "
#                                         "или к проблеме, которая лучше всего описывает вашу проблему. "
#                                         "На любом уровне вы сможете вернуться на предыдущий уровень. "
#                                         "Ваши ответы должны помочь определить основные проблемы. "
#                                         "Эти вопросы содержат рекомендации по шаблонам, которые помогут вам решить ваши проблемы. "
#                                         "В /шаблонах разрешения мы даем некоторые рекомендации, но выбор того, "
#                                         "как применять шаблоны, — это то, о чем вам нужно будет подумать в вашей собственной ситуации.",
#
#                                    reply_markup=markup)
#             bot.register_next_step_handler(msg, layer_1)
#         else:
#             pass
#     except:
#         bot.send_message(call.message.chat.id, f'🚫 | Ошибка при выполнении команды')
#
#
# @bot.callback_query_handler(
#     lambda call: call.data == 'improve' or call.data == 'patterns' or call.data == 'experience' or call.data == 'problems' or call.data == 'back')
# def layer_1(call):
#     try:
#
#         if call.data == 'improve':
#             markup = get_improve_markup()
#
#             msg = bot.send_message(call.message.chat.id,
#                                    text='Что ниже описывает наиболее насущную проблему, которую вам предстоит решить на данный момент?\n'
#                                         'Если вы обнаружите, что более одного ответа подходит для вашего случая, начните с самого сложного. После того, как вы решите его, вы должны вернуться к этому вопросу и заняться следующими.',
#                                    reply_markup=markup)
#             bot.register_next_step_handler(msg, layer_1)
#
#         elif call.data == 'patterns':
#             markup = get_patterns_markup()
#
#             msg = bot.send_message(call.message.chat.id,
#                                    text=open('patterns/patterns_no_prev_auto.txt', 'r').read(), parse_mode='Markdown',
#                                    reply_markup=markup)
#             bot.register_next_step_handler(msg, layer_1)
#
#     except:
#         bot.send_message(call.message.chat.id, f'🚫 | Ошибка при выполнении команды')
