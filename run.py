from slackbot.bot import Bot
from logging import basicConfig, DEBUG

fmt = "%(asctime)s %(levelname)s %(name)s :%(message)s"
basicConfig(level=DEBUG, format=fmt)


def main():
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    print('start slackbot')
    main()
