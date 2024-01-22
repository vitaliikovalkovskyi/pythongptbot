import openai
import telebot
import sqlite3

openai.api_key = 'YOUR-API-KEY'
bot = telebot.TeleBot("YOUR-TELEGRAMBOT-TOKEN")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(chat_id=message.from_user.id, text='Hi, I am ChatGpt bot. Ask me a question and I will do my best to answer it!')
    bot.send_message(chat_id=message.from_user.id, text='Привіт, я бот Chatgpt. Задайте мені запитання, і я зроблю все можливе, щоб відповісти на нього!\nВведіть /help для перегляду інформації, щодо роботи з ботом.')

    connect = sqlite3.connect('user_new.db')
    cursor = connect.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT
    )
    """)

    connect.commit()

    # Receive user data from the Telegram bot
    user_id = [message.chat.id]
    username = [message.chat.username]
    
    people_id = message.chat.id
    cursor.execute(f"SELECT user_id FROM users WHERE user_id = {people_id}")
    data = cursor.fetchone()
    if data is None:

        cursor.execute("INSERT INTO users (user_id, username)VALUES (?,?);", (user_id[0], username[0]))
        connect.commit()
    

    

@bot.message_handler(commands=['help'])
def send_help_message(message):
        bot.send_message(chat_id=message.from_user.id, text='I can help with succinctly searching for information,\ncreating essays, answering questions, and more.\nJust send your request in the chat!')
        bot.send_message(chat_id=message.from_user.id, text='Я можу допомогти з лаконічним пошуком інформації,\nстворенням есе, відповіддю на запитання та інше.\nПросто відправте свій запит у чат!')


@bot.message_handler(commands=['feedback'])
def send_feedback_message(message):
        bot.send_message(chat_id=message.from_user.id, text='If you have suggestions for improving the bot or want to financially support the project, contact:\ntg: @vitaliy_kovalkovskyi')
        bot.send_message(chat_id=message.from_user.id, text='Якщо у вас є пропозиції, для покращення бота або ви хочете фінансово допомогти проекту - звяжіться з:\ntg: @vitaliy_kovalkovskyi')

@bot.message_handler(func=lambda _: True)
def handle_message(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )
    bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])

    
bot.polling()

