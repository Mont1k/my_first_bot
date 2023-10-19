from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Click me!",
        callback_data="start_questionnaire"
    )
    registration_button = InlineKeyboardButton(
        "Registration",
        callback_data='fsm_start'
    )
    my_profile_button = InlineKeyboardButton(
        "My Profile",
        callback_data="my_profile"
    )

    markup.add(questionnaire_button)
    markup.add(registration_button)
    markup.add(my_profile_button)
    return markup


async def questionnaire_one_keyboard():
    markup = InlineKeyboardMarkup()
    yes_button = InlineKeyboardButton(
        "Yes",
        callback_data="hungry_yes"
    )
    no_button = InlineKeyboardButton(
        "Yes, of course",
        callback_data="hungry_no"
    )
    markup.add(yes_button)
    markup.add(no_button)
    return markup


async def admin_keyboard():
    markup = InlineKeyboardMarkup()
    admin_user_list_button = InlineKeyboardButton(
        "User List",
        callback_data="admin_user_list"
    )
    markup.add(admin_user_list_button)
    return markup
