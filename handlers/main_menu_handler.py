from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters
from typing import Dict, Callable, Optional
import logging

from handlers.basehandler import BaseHandler
from keyboards import get_main_keyboard, menu_btn_txt, price_btn_txt, call_btn_txt, back_btn_txt

logger = logging.getLogger(__name__)

class MainMenuHandler(BaseHandler):

    async def _handle_error(self, update: Update, context: ContextTypes.DEFAULT_TYPE, error: Exception):
        await update.message.reply_text("Произошла ошибка. Попробуйте позже.")




def register_main_menu_handlers(basehandler: BaseHandler):
    """Регистрация всех обработчиков"""

    basehandler.register_handler(menu_btn_txt, handle_menu)
    basehandler.register_handler(price_btn_txt, handle_prices)
    basehandler.register_handler(call_btn_txt, handle_call_waiter)
    basehandler.register_handler(back_btn_txt, handle_back)
    basehandler.register_fallback(handle_unknown_command)


# # раньше этой функции не было и в app.add_handler(MessageHandler(filters.TEXT, handle_message))
#     # туда передавался message_handler, а нужно было передать функцию обертку
# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """Эта функция будет передана в MessageHandler"""
#     return await message_handler.handle(update, context)

async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from keyboards import get_food_keyboard
    context.user_data["menu_state"] = "food"
    await update.message.reply_text(
        "Наше меню",
        reply_markup=get_food_keyboard()
    )

async def handle_prices(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from keyboards import get_burger_buttons
    await update.message.reply_text(
        "здесь будут цены"
    )

async def handle_call_waiter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Официант вызван! Ожидайте..."
    )

async def handle_back(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Возвращаюсь",
        reply_markup=get_main_keyboard()
    )

async def handle_unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Я такой кнопки не знаю"
    )