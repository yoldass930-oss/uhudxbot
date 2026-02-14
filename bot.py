import telebot

TOKEN = "8495102269:AAEE3arpBHrwaxM-1ru54Q2jGfJaWT3JAd0"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Selam aleyküm babuş buranın yakışıklı güvenliği benim bir sıkıntın oldumu etiket atman yeterli")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if "@uhudxbot" in message.text.lower():
        bot.reply_to(message, "Beni mi çağırdın kral sorun nedir")

bot.infinity_polling()
import random

@bot.message_handler(func=lambda message: bot.get_me().username.lower() in message.text.lower())
def mention_handler(message):
    cevaplar = [
        "Beni mi çağırdın lan ",
        "Buradayım kral ",
        "dinliyorum😒 ",
        "Ne var la"
    ]
    bot.reply_to(message, random.choice(cevaplar))
