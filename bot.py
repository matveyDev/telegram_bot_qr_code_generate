import os
import telebot

from path import Path

from utils import create_qr_code
from local_settings import TOKEN

bot = telebot.TeleBot(TOKEN)

user_last_url = dict()


@bot.message_handler(commands=['start'])
def get_text(message):
    bot.send_message(message.from_user.id, 'Отправь мне url, затем картинку!')


@bot.message_handler(content_types=['text'])
def get_text(message):
    bot.send_message(message.from_user.id, 'Отлично, теперь отправь картинку!\nЕсли ошибся, можешь заного отправить url!')
    user_last_url[message.from_user.id] = message.text


@bot.message_handler(content_types=['photo'])
def get_image(message):
    file_id = message.photo[-1].file_id
    file = bot.get_file(file_id)
    downloaded_file = bot.download_file(file.file_path)
    
    file_name = f'{file_id}.jpeg'
    file_path = Path().joinpath('.', f'{file_id}.jpeg')
    file_path_to_save = Path().joinpath('.', f'{file_id}.png')

    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    url_to_redirect = user_last_url[message.from_user.id]
    qr_code = create_qr_code(
        url_to_redirect,
        file_path,
        file_path_to_save
    )
    del user_last_url[message.from_user.id]

    qr_code_image = open(qr_code.PATH_TO_SAVE_QR_CODE, 'rb')
    bot.send_photo(message.from_user.id, qr_code_image)
    qr_code_image.close()

    os.remove(qr_code.PATH_TO_SAVE_QR_CODE)
    os.remove(qr_code.PATH_IMAGE)


bot.infinity_polling()
