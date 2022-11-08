import config
from src.Questions import MainClass as Questions

bot = Questions(config.token)
bot.start()
