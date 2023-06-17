import telebot
from telebot import types
import random

token = '6098263628:AAFT0MH5-_Dlsb1qVPw-qzSLPDxpYVaejjg'
bot = telebot.TeleBot(token)

# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Узнать, какой ты котик😊')
    markup.add(btn1)
    bot.send_message(message.chat.id, text='Привет! Давай узнаем, какой ты сегодня котик😊', reply_markup=markup)
    bot.send_photo(message.chat.id, 'https://avatars.mds.yandex.net/i?id=37b24f4732fdf27af69e251e007c000ce9b1b3b6-9181356-images-thumbs&n=13', None, 'Text')
    
# Функция для получения случайной картинки с котиком 
def get_random_cat_image():
    cat_images = [
        'https://klike.net/uploads/posts/2019-07/medium/1564314090_3.jpg',
        'https://klike.net/uploads/posts/2019-07/medium/1564314134_11.jpg',
        'https://klike.net/uploads/posts/2018-10/1539499416_9.jpg',
        'https://klike.net/uploads/posts/2022-08/1661254762_j-114.jpg',
        'https://klike.net/uploads/posts/2022-08/1661254749_j-107.jpg',
        'https://klike.net/uploads/posts/2022-08/1661254809_j-123.jpg',
        'https://chudo-prirody.com/uploads/posts/2021-08/thumbs/1628741970_14-p-smeshnie-foto-kotov-i-koshek-do-slez-14.jpg',
        'https://chudo-prirody.com/uploads/posts/2021-08/thumbs/1628742029_166-p-smeshnie-foto-kotov-i-koshek-do-slez-182.jpg',
        'https://chudo-prirody.com/uploads/posts/2021-08/thumbs/1628741944_6-p-smeshnie-foto-kotov-i-koshek-do-slez-6.jpg',
        'https://chudo-prirody.com/uploads/posts/2021-08/thumbs/1628741949_128-p-smeshnie-foto-kotov-i-koshek-do-slez-139.jpg'

    ]
    return random.choice(cat_images)

# Функция для получения случайного описания 
def get_random_description():
    descriptions = [
        'ты сегодня лучше всех, ждет тебя успех ❤️',
        'ты сегодня просто солнце, кто увидит - улыбнется ❤️',
        'ты сегодня милый котик, хоть и ешь, как бегемотик ❤️',
        'ты сегодня просто класс, расцелую тебя сейчас ❤️',
        'ты сегодня милота, я куплю тебе кота ❤️',
        'ну какой же ты лапусик, в жизни пусть не будет грусти ❤️',
        'я в глаза твои гляжу, даже слов не нахожу ❤️',
        'что за ушки, что за носик, ты такой милейший котик❤️',
        'я тебе шепчу на ушко, что ты - сахарная плюшка❤️',
        'ой, какая красота заглянула к нам сюда ❤️'
    ]
    return random.choice(descriptions)

# обработчик всех остальных сообщений   
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.strip() == 'Узнать, какой ты котик😊':
        description = get_random_description()
        image = get_random_cat_image()
        bot.send_photo(message.chat.id, image, description)

# главная функция программы
def main():
    # запускаем нашего бота
    bot.polling(none_stop=True)

if __name__ == '__main__':
    main()