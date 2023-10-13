import sqlite3

from aiogram import types, Dispatcher
from config import bot
from database.sql_commands import Database


async def check_and_ban_users(chat_id, user_id):
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT FROM ban WHERE TELEGRAM_ID = ?', (user_id,))
    count = cursor.fetchone()

    if count and count[0] >= 3:
        try:
            await bot.kick_chat_member(chat_id, user_id)
        except Exception as e:
            print(f"Не удалось забанить пользователя: {e}")

    conn.close()


async def chat_action(message: types.Message):
    ban_words = ['fuck', 'bitch', 'damn']

    trigger_words = ['пошел нахуй', 'иди в жопу', 'заткнись', 'иди нахуй']

    for word in ban_words:
        if word in message.text.lower().replace(" ", ""):
            user = Database().sql_select_user_query(
                telegram_id=message.from_user.id
            )
            print(user)
            if user:
                # Database().sql_update_ban_user_query(
                #     telegram_id=message.from_user.id
                # )
                Database().sql_update_ban_query(
                    telegram_id=message.from_user.id
                )
                print(user)
            else:
                Database().sql_insert_ban_query(
                    telegram_id=message.from_user.id
                )

            await bot.delete_message(
                chat_id=message.chat.id,
                message_id=message.message_id
            )
            await bot.send_message(
                chat_id=message.chat.id,
                text=f'Ты короче подозрительный, ты можешь быть забанен\n'
                     f'Username: {message.from_user.username}\n'
                     f'First-Name: {message.from_user.first_name}'
            )

    for word in trigger_words:
        if word in message.text.lower():
            await message.reply("Сам пошел!")

    if message.text.startswith('/'):
        await message.reply("There is no such a command. Maybe u mispronounced")


def register_chat_actions_handlers(dp: Dispatcher):
    dp.register_message_handler(chat_action)
