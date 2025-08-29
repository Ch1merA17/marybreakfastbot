from telegram import Update
from telegram.ext import ContextTypes
from service import Products, Product
from handlers.basehandler import BaseHandler
from keyboards import get_food_keyboard, get_main_keyboard, get_burger_buttons
from MyDB.models import Product
from service import add_to_cart, get_user_cart, create_new_cart
from typing import Callable
import logging

logger = logging.getLogger(__name__)


class FoodMenuHandler(BaseHandler):

    async def _handle_error(self, update: Update, context: ContextTypes.DEFAULT_TYPE, error: Exception):
        """Обработка ошибок в меню"""
        await update.message.reply_text("⚠️ Ошибка в меню. Попробуйте снова.")

def register_food_menu_handlers(basehandler: BaseHandler):
    """Регистрирует все обработчики кнопок меню"""
    from keyboards import (
        burger_btn_txt, fries_btn_txt, drink_btn_txt,
        back_btn_txt
    )

    basehandler.register_handler(burger_btn_txt, handle_burger)
    basehandler.register_handler(fries_btn_txt, handle_fries)
    basehandler.register_handler(drink_btn_txt, handle_drink)
    basehandler.register_handler(back_btn_txt, handle_back_to_main)
    basehandler.register_fallback(handle_unknown_menu_command)







# Обработчики для каждой кнопки еды
async def handle_burger(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик кнопки Бургер"""
    print("метод handle_burger вызван")
    user_id = update.effective_user.id
    cart = get_user_cart(user_id)
    product = Product(Products.BURGER.value)
    add_to_cart(cart, product)
    if cart is None:
        print("Корзины нет браток")
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
    context.user_data["menu_state"] = "main"
    await update.message.reply_text(
        text="Возвращаемся",
        reply_markup=get_main_keyboard()
    )


async def handle_unknown_menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик неизвестных кнопок в меню"""
    await update.message.reply_text(
        "❌ Неизвестная команда в меню",
        reply_markup=get_food_keyboard()
    )