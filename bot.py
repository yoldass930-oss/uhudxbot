import telebot

TOKEN = "8495102269:AAEE3arpBHrwaxM-1ru54Q2jGfJaWT3JAd0"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Selam aleyküm güvenlik ve asayişten ben sorumluyum(mıdıtenyosayk😏")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if "@uhudxbot" in message.text.lower():
        bot.reply_to(message, "Beni mi çağırdın kral sorun nedir"
                    "seni dinliyorum"
                     "ne var la"

bot.infinity_polling()
