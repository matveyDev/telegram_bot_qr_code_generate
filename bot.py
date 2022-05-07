import telebot

from local_settings import TOKEN


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['photo'])
def get_image(message):
    file_id = message.photo[-1].file_id
    file = bot.get_file(file_id)
    downloaded_file = bot.download_file(file.file_path)

    with open('image.jpg', 'wb') as new_file:
        new_file.write(downloaded_file)


@bot.message_handler(content_types=['text'])
def get_text(message):
    bot.send_message(message.from_user.id, 'Send me your funny image for QR Code')


bot.polling(none_stop=True, interval=0)
