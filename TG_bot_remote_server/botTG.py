#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Добро пожаловать! Я автоматический бот Михаила. Умею не очень много, но с самым важным - получить ваше коммерческое предложение и передать его Михаилу. Для этого достаточно отправить ваше предложение ответным сообщением после запуска бота или использовать команду /offer. После команды /offer бот будет готов передать ваше сообщение Михаилу.")

def offer(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        update.message.reply_text('Пожалуйста, введите предложение и контакты в следующем сообщении.')
        context.user_data['waiting_for_offer'] = True  # Устанавливаем флаг ожидания предложения
    else:
        if 'waiting_for_offer' in context.user_data:
            del context.user_data['waiting_for_offer']  # Сбрасываем флаг ожидания предложения

        message = ' '.join(context.args)
        sender = update.effective_user.username
        if not sender:
            sender = update.effective_user.full_name
        message = f"Предложение от {sender}:\n\n{message}"

        context.bot.send_message(chat_id=********, text=message)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Спасибо за ваше обращение. Ваше предложение уже передано Михаилу, и он свяжется с вами в ближайшее время.")

def handle_text_message(update: Update, context: CallbackContext):
    if 'waiting_for_offer' in context.user_data:
        message = update.message.text
        sender = update.effective_user.username
        if not sender:
            sender = update.effective_user.full_name
        message = f"Предложение от {sender}:\n\n{message}"

        context.bot.send_message(chat_id=********, text=message)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Спасибо за ваше обращение. Ваше предложение уже передано Михаилу, и он свяжется с вами в ближайшее время.")
        del context.user_data['waiting_for_offer']  # Сбрасываем флаг ожидания предложения

def help_command(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Бот получает информацию о ваших предложениях для Михаила и пересылает ему. Для этого достаточно отправить ваше предложение ответным сообщением после запуска бота или использовать команду /offer. После команды /offer бот будет готов передать ваше сообщение Михаилу.")

def main():
    bot_token = '****************'
    updater = Updater(token=bot_token, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("offer", offer, pass_args=True))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text_message))
    dispatcher.add_handler(CommandHandler("help", help_command))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
