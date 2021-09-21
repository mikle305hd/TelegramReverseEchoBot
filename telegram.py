from aiogram import Bot, Dispatcher, types


class TelegramBot:
    def __init__(self, bot_token: str, admin_id: str = None) -> None:
        self.__bot = Bot(token=bot_token)
        self.__dispatcher = Dispatcher(bot=self.__bot)
        self.__admin_id = admin_id
        # decorator
        TelegramBot.reply_welcome = self.__dispatcher.message_handler(commands=['start'])(TelegramBot.reply_welcome)
        TelegramBot.reverse_echo = self.__dispatcher.message_handler()(TelegramBot.reverse_echo)

    @property
    def dispatcher(self):
        return self.__dispatcher

    @staticmethod
    async def reply_welcome(message: types.Message) -> None:
        """
        This handler will be called when user sends `/start` or `/help` command
        """
        await message.reply("Hi!\nI'm Simple ReverseEchoBot!\n")

    @staticmethod
    async def reverse_echo(message: types.Message) -> None:
        """
        This handler will be called when user sends any message
        """
        await message.answer(message.text[::-1])
