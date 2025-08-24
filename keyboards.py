from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
menu_btn_txt = "Меню 🍽"
price_btn_txt = "Цены 💲"
call_btn_txt = "Позвать официанта 💁‍♂️"
burger_btn_txt = "Бургер"
fries_btn_txt = "Картошка Фри"
drink_btn_txt = "Koka Kola"
cart_btn_txt = "Корзина"
back_btn_txt = "Назад"
def get_main_keyboard():
    menu_button = KeyboardButton(menu_btn_txt)
    price_button = KeyboardButton(price_btn_txt)
    call_button = KeyboardButton(call_btn_txt)
    cart_button = KeyboardButton(cart_btn_txt)

    keyboard = [
        [menu_button, price_button],
        [cart_button],
        [call_button]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def get_food_keyboard():
    burger_button = KeyboardButton(burger_btn_txt)
    fries_button = KeyboardButton(fries_btn_txt)
    back_button = KeyboardButton(back_btn_txt)
    drink_button = KeyboardButton(drink_btn_txt)

    food_keyboard = [
        [burger_button, fries_button],
        [drink_button],
        [back_button]
    ]
    return ReplyKeyboardMarkup(food_keyboard, resize_keyboard=True)

def get_burger_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Добавить сыр (+50₽)", callback_data="add_cheese")],
        [InlineKeyboardButton("В корзину", callback_data="add_to_cart")]
    ])