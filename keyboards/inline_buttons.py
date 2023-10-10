from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Click me!",
        callback_data="start_questionnaire"
    )
    markup.add(questionnaire_button)
    return markup


async def questionnaire_one_keyboard():
    markup = InlineKeyboardMarkup()
    yes_button = InlineKeyboardButton(
        "Yes",
        callback_data="yes1"
    )
    yes2_button = InlineKeyboardButton(
        "Yes, of course",
        callback_data="yes2"
    )
    markup.add(yes_button)
    markup.add(yes2_button)
    return markup
