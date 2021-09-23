from aiogram import Bot, Dispatcher, types
from gitlab import GitLab


class TelegramBot:
    def __init__(self, bot_token: str, admin_id: str = None,
                 domain: str = None, access_token: str = None, project_name: str = None) -> None:
        """
        :param bot_token: Telegram bot api token. Uses to manipulate your telegram bot.
        :param admin_id: Bot admin Telegram account id. Uses to get special actions from admin account.
        :param domain: GitLab domain name. For example: gitlab.example.com.
        :param access_token: GitLab private access token. Uses to authenticate with the GitLab API.
        :param project_name: Current GitLab project name.
        """
        self.__bot = Bot(token=bot_token)
        self.__dispatcher = Dispatcher(bot=self.__bot)
        self.__admin_id = admin_id
        self.__git = GitLab(domain, access_token)
        TelegramBot.__project_name = project_name
        TelegramBot.__projects_handler = self.__git.get_projects
        TelegramBot.__commits_handler = self.__git.get_commits

        # Decorators
        TelegramBot.reply_welcome = self.__dispatcher.message_handler(commands=['start'])(TelegramBot.reply_welcome)
        TelegramBot.get_commits = self.__dispatcher.message_handler(commands=['commits'])(TelegramBot.get_commits)
        TelegramBot.reverse_echo = self.__dispatcher.message_handler()(TelegramBot.reverse_echo)

    @property
    def dispatcher(self):
        return self.__dispatcher

    @staticmethod
    async def reply_welcome(message: types.Message) -> None:
        """
        This handler will be called when user sends `/start` command.
        Awaiting for user command.
        :param message:
        """
        await message.reply("Hi!\nI'm Simple ReverseEchoBot!\n")

    @staticmethod
    async def reverse_echo(message: types.Message) -> None:
        """
        This handler will be called when user sends any message.
        Awaiting for user message.
        """
        await message.answer(message.text[::-1])

    @staticmethod
    async def get_commits(message: types.Message) -> None:
        """
        This handler will be called when user sends `/commits` command.
        Awaiting for user command.
        """
        commits = []
        for project in TelegramBot.__projects_handler():
            if project['name'] == TelegramBot.__project_name:
                commits = TelegramBot.__commits_handler(project['id'])
                break
        if not commits:
            print('Error: bad project name')
            return
        reply = ''
        for counter, commit in enumerate(commits):
            reply += f"{counter+1} commit\nDate: {commit['created_at']}\n" \
                             f"Title: {commit['title']}\nMessage: {commit['message']}\n" \
                             f"Committer email: {commit['committer_email']}\n\n"

        await message.reply(reply)
