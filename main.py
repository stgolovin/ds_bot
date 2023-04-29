import telebot
from telebot import types

import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    global price
    price = 0
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рассчитать подъемник")
    item2 = types.KeyboardButton("Перейти на наш сайт")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Здравствуйте, {0.first_name}! "
                                      "Приветствуем Вас в телеграмм-боте компании Доступная Среда! "
                                      "Мы занимаемся комплексной адаптацией "
                                      "для маломобильных групп населения.".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler()
def answer(message):
    if message.chat.type == 'private':
        if message.text == 'Рассчитать подъемник':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Вертикальный', callback_data='vertical')
            item2 = types.InlineKeyboardButton('Горизонтальный', callback_data='horizontal')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, "Выберите тип подъемника", reply_markup=markup)
        if message.text == 'Перейти на наш сайт':
            markup = types.InlineKeyboardMarkup(row_width=1)
            item = types.InlineKeyboardButton("Перейти на ds93krd.ru", url="https://ds93krd.ru")
            markup.add(item)
            bot.send_message(message.chat.id, "Доступная Среда", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global price
    if call.message:
        if call.data == 'vertical':
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text='Вы выбрали вертикальный подъемник.',
                                  reply_markup=None)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('До 1 метра', callback_data='1m')
            item2 = types.InlineKeyboardButton('До 2 метров', callback_data='2m')
            markup.add(item1, item2)
            bot.send_message(call.message.chat.id, "Выберите высоту подъема", reply_markup=markup)

        elif call.data == 'horizontal':
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text='Вы выбрали горизонтальный подъемник.',
                                  reply_markup=None)
            bot.send_message(call.message.chat.id, 'Пока сюжет не написан. Лучше попробуйте вертикальный.')

        if call.data == '1m':
            price += 175000
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text='Вы выбрали высоту подъема до 1 метра',
                                  reply_markup=None)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Нужна', callback_data='withdisp')
            item2 = types.InlineKeyboardButton('Не нужна', callback_data='withoutdisp')
            markup.add(item1, item2)
            bot.send_message(call.message.chat.id, "Что насчет диспетчиризации?", reply_markup=markup)

        elif call.data == '2m':
            price += 240000
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text='Вы выбрали высоту подъема до 2 метров',
                                  reply_markup=None)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Нужна', callback_data='withdisp')
            item2 = types.InlineKeyboardButton('Не нужна', callback_data='withoutdisp')
            markup.add(item1, item2)
            bot.send_message(call.message.chat.id, "Что насчет диспетчеризации?", reply_markup=markup)

        if call.data == 'withdisp':
            price += 30000
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text='Вы сказали, что диспетчеризация нужна',
                                  reply_markup=None)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Потребуется', callback_data='withfence')
            item2 = types.InlineKeyboardButton('Не потребуется', callback_data='withoutfence')
            markup.add(item1, item2)
            bot.send_message(call.message.chat.id, "Потребуется ли калитка на верхней площадке?", reply_markup=markup)

        elif call.data == 'withoutdisp':
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text='Вы сказали, что диспетчеризация не нужна',
                                  reply_markup=None)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Потребуется', callback_data='withfence')
            item2 = types.InlineKeyboardButton('Не потребуется', callback_data='withoutfence')
            markup.add(item1, item2)
            bot.send_message(call.message.chat.id, "Потребуется ли калитка на верхней площадке?", reply_markup=markup)

        if call.data == 'withfence':
            price += 32000
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text='Вы сказали, что калитка нужна',
                                  reply_markup=None)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Необходимо', callback_data='withaudit')
            item2 = types.InlineKeyboardButton('Нет необходимости', callback_data='withoutaudit')
            markup.add(item1, item2)
            bot.send_message(call.message.chat.id, "Необходимо ли произвести полное техническое "
                                                   "освидетельствование платформы подъемной?", reply_markup=markup)

        elif call.data == 'withoutfence':
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text='Вы сказали, что калитка не нужна',
                                  reply_markup=None)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Необходимо', callback_data='withaudit')
            item2 = types.InlineKeyboardButton('Нет необходимости', callback_data='withoutaudit')
            markup.add(item1, item2)
            bot.send_message(call.message.chat.id, "Необходимо ли произвести полное техническое "
                                                   "освидетельствование платформы подъемной?", reply_markup=markup)

        if call.data == 'withaudit':
            price += 25000
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text='Вы сказали, что ПТО ПП необходимо',
                                  reply_markup=None)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Потребуется', callback_data='withcons')
            item2 = types.InlineKeyboardButton('Не потребуется', callback_data='withoutcons')
            markup.add(item1, item2)
            bot.send_message(call.message.chat.id, "Потребуется ли монтаж платформы подъемной?", reply_markup=markup)

        elif call.data == 'withoutaudit':
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text='Вы сказали, что в ПТО ПП нет необходимости',
                                  reply_markup=None)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Потребуется', callback_data='withcons')
            item2 = types.InlineKeyboardButton('Не потребуется', callback_data='withoutcons')
            markup.add(item1, item2)
            bot.send_message(call.message.chat.id, "Потребуется ли монтаж платформы подъемной?", reply_markup=markup)

        if call.data == 'withcons':
            price += 89000
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text="Вы сказали, что монтаж потребуется",
                                  reply_markup=None)
            bot.send_message(call.message.chat.id, f"Общая стоимость составляет {price} рублей.")

        elif call.data == 'withoutcons':
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text="Вы сказали, что монтаж не потребуется",
                                  reply_markup=None)
            bot.send_message(call.message.chat.id, f"Общая стоимость составляет {price} рублей.")


# RUN
bot.polling(none_stop=True)
