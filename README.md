# ChatGpt Telegram Bot
# Introduction:
The ChatGpt Telegram Bot is an interactive bot powered by OpenAI's GPT-3.5 language model. The bot is designed to engage in conversations, answer questions, provide information, and assist users in a chat environment on the Telegram platform.

# Features:
Welcome Message: Upon initiation with the /start command, the bot greets users and introduces itself. It encourages users to ask questions and provides a brief overview of its capabilities in both English and Ukrainian.

User Database: The bot utilizes SQLite to store user information, including user ID and username. This information is captured when users interact with the bot for the first time and is stored in the users table in the user_new.db database.

Help Command: Users can access helpful information about the bot's capabilities by using the /help command. 

Feedback Command: The /feedback command provides users with information on how to offer suggestions for improving the bot or contribute to the project financially. It includes contact details for reaching out via Telegram.

Message Handling: The bot captures all incoming messages not associated with specific commands. It then uses OpenAI's GPT-3.5 model (text-davinci-003) to generate responses based on the received message. The response is then sent back to the user in the Telegram chat.

# Dependencies:
openai: Python library for interfacing with the OpenAI GPT-3.5 model.
telebot: Python library for building Telegram bots.
sqlite3: Python library for SQLite database operations.
Setup Instructions:
Install the required Python libraries: openai, telebot.
Obtain API keys from OpenAI and Telegram Bot Token.
Update the YOUR-API-KEY and YOUR-TELEGRAMBOT-TOKEN placeholders with the respective keys.
Run the script to start the bot.

#Usage:
Start a chat with the bot by using the /start command.
Seek assistance by asking questions or engaging in conversation.
Use the /help command for information on the bot's capabilities.
Provide feedback or support the project using the /feedback command.

# Contact Information:
For further assistance or to provide feedback, contact:
Telegram: @wnezoxq

# Disclaimer:
This project is a demonstration of the capabilities of the OpenAI GPT-3.5 model and is not intended for production use. The bot's responses are generated based on patterns learned during training and may not always be accurate or suitable for all situations. Users are encouraged to use the bot responsibly and be aware of the limitations of AI language models.

UPD:
The script requires modification for compatibility with GPT-4.0 due to changes in OpenAI's usage policies.
