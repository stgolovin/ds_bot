import telebot
from telebot import types

import config

bot = telebot.TeleBot(config.TOKEN)



@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('Вертикальный', callback_data='vertical')
    item2 = types.InlineKeyboardButton('Наклонный', callback_data='horizontal')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Здравствуйте {0.first_name}! "
                                      "Давайте посчитаем подъемник:".format(message.from_user,bot.get_me()),
                     parse_mode='html', reply_markup=markup)
global price


price = 0


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
            bot.send_message(call.message.chat.id, 'Вы выбрали горизонтальный подъемник.')
        if call.data == '1m':
            price += 125000
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text='Вы выбрали высоту подъема до 1 метра',
                                  reply_markup=None)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Нужна', callback_data='withdisp')
            item2 = types.InlineKeyboardButton('Не нужна', callback_data='withoutdisp')
            markup.add(item1, item2)
            bot.send_message(call.message.chat.id, "Что насчет диспетчиризации?", reply_markup=markup)
        if call.data == '2m':
            price += 240000
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text='Вы выбрали высоту подъема до 1 метра',
                                  reply_markup=None)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Нужна', callback_data='withdisp')
            item2 = types.InlineKeyboardButton('Не нужна', callback_data='withoutdisp')
            markup.add(item1, item2)
            bot.send_message(call.message.chat.id, "Что насчет диспетчиризации?", reply_markup=markup)
        if call.data == 'withdisp':
            price += 30000
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text='Вы сказали что диспетчиризация нужна',
                                  reply_markup=None)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Нужен', callback_data='withcons')
            item2 = types.InlineKeyboardButton('Не нужен', callback_data='withoutcons')
            markup.add(item1, item2)
            bot.send_message(call.message.chat.id, "Нужен ли монтаж?", reply_markup=markup)

        if call.data == 'withoutdisp':
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text='Вы выбрали красный цвет',
                                  reply_markup=None)
        if call.data == 'withcons':
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=f"Общая стоимость составляет {price} рублей.",
                                  reply_markup=None)
            # bot.send_message(call.message.chat.id, f"Общая стоимость составляет {price} рублей.")





            # remove inline buttons
            # bot.edit_message_text(chat_id=call.message.chat.id,
            #                       message_id=call.message.message_id,
            #                       text='Second',
            #                       reply_markup=None)

            # show alert
            # bot.answer_callback_query(chat_id=call.id, show_alert=False, text='Это тестовое уведомление!')


# RUN
bot.polling(none_stop=True)
