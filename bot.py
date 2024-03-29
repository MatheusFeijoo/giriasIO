import telebot
from telebot import types
import time
from testeNLTK import tokenFrase


bot_token = ""

bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = bot.reply_to(message, "Olá!!")


@bot.message_handler(func=lambda message:True)
def recebendo(message):
    try:
        chat_id = message.chat.id
        passaGiria = message.text
        print (passaGiria)
        messageTraduzida, passou = tokenFrase(passaGiria)
        if(passou == 1):
            bot.reply_to(message, messageTraduzida, parse_mode= 'Markdown')
    except Exception as e:
        bot.reply_to(message, 'algo deu errado')

bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()

bot.polling()