from telegram import TelegramBot
from config import BOT_TOKEN, DOMAIN, GITLAB_ACCESS_TOKEN, PROJECT_NAME


def main():
    bot = TelegramBot(BOT_TOKEN, domain=DOMAIN, access_token=GITLAB_ACCESS_TOKEN, project_name=PROJECT_NAME)
    bot.start()


if __name__ == '__main__':
    main()
