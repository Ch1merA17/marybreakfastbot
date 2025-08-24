from telegram import Update
from telegram.ext import ContextTypes

from handlers.basehandler import BaseHandler
from keyboards import get_food_keyboard, get_main_keyboard, get_burger_buttons
from database.models import Product
from service import add_to_cart, get_user_cart, create_new_cart
from typing import Callable
import logging

logger = logging.getLogger(__name__)


class MenuHandler(BaseHandler):

    async def _handle_error(self, update: Update, context: ContextTypes.DEFAULT_TYPE, error: Exception):
        """Обработка ошибок в меню"""
        await update.message.reply_text("⚠️ Ошибка в меню. Попробуйте снова.")

    def register_menu_handlers(self):
        """Регистрирует все обработчики кнопок меню"""
        from keyboards import (
            burger_btn_txt, fries_btn_txt, drink_btn_txt,
            back_btn_txt
        )

        self.register_handler(burger_btn_txt, handle_burger)
        self.register_handler(fries_btn_txt, handle_fries)
        self.register_handler(drink_btn_txt, handle_drink)
        self.register_handler(back_btn_txt, handle_back_to_main)
        self.register_fallback(handle_unknown_menu_command)


menu_handler = MenuHandler()




# Обработчики для каждой кнопки еды
async def handle_burger(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик кнопки Бургер"""
    user_id = update.effective_user.id
    add_to_cart(user_id, "burger", 300)
    await update.message.reply_text(
        "🍔 Бургер добавлен в корзину!",
        reply_markup=get_food_keyboard()
    )


async def handle_fries(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик кнопки Пицца"""
    user_id = update.effective_user.id
    add_to_cart(user_id, "pizza", 450)
    await update.message.reply_text(
        "🍕 Пицца добавлена в корзину!",
        reply_markup=get_food_keyboard()
    )


async def handle_drink(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик кнопки Салат"""
    user_id = update.effective_user.id
    add_to_cart(user_id, "salad", 200)
    await update.message.reply_text(
        "🥗 Салат добавлен в корзину!",
        reply_markup=get_food_keyboard()
    )


async def handle_back_to_main(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик кнопки Назад (в главное меню)"""
    from keyboards import get_main_keyboard
    await update.message.reply_text(
        text="Возвращаемся",
        reply_markup=get_main_keyboard()
    )


async def handle_unknown_menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str):
    """Обработчик неизвестных кнопок в меню"""
    await update.message.reply_text(
        "❌ Неизвестная команда в меню",
        reply_markup=get_food_keyboard()
    )