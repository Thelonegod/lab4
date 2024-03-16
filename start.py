import telebot
token = '7095775124:AAFHD2akU4EFctwUE5a7K6jmoXoNYxNrPx4'


bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()
