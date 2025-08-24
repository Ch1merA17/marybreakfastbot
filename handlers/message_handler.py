from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters
from typing import Dict, Callable, Optional
import logging

from handlers.basehandler import BaseHandler
from keyboards import get_main_keyboard

logger = logging.getLogger(__name__)

class MessageHandler(BaseHandler):

    async def _handle_error(self, update: Update, context: ContextTypes.DEFAULT_TYPE, error: Exception):
        await update.message.reply_text("Произошла ошибка. Попробуйте позже.")




    def register_handlers(self):
        """Регистрация всех обработчиков"""
        from keyboards import (
            menu_btn_txt, price_btn_txt,
            call_btn_txt,
            back_btn_txt
        )

        self.register_handler(menu_btn_txt, handle_menu)
        self.register_handler(price_btn_txt, handle_prices)
        self.register_handler(call_btn_txt, handle_call_waiter)
        self.register_handler(back_btn_txt, handle_back)
        self.register_fallback(handle_unknow_command)

message_handler = MessageHandler()

# раньше этой функции не было и в app.add_handler(MessageHandler(filters.TEXT, handle_message))
    # туда передавался message_handler, а нужно было передать функцию обертку
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Эта функция будет передана в MessageHandler"""
    return await message_handler.handle(update, context)

async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from keyboards import get_food_keyboard
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

async def handle_unknow_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Я такой кнопки не знаю"
    )