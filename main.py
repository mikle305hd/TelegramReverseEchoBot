from aiogram import executor
from telegram import TelegramBot
BOT_TOKEN = '2039542921:AAE6F_45d168q_IeWQNySv27_RNt914MO84'


def main():
    bot = TelegramBot(BOT_TOKEN)
    executor.start_polling(bot.dispatcher, skip_updates=True)


if __name__ == '__main__':
    main()
