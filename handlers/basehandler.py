from telegram import Update
from telegram.ext import ContextTypes
from keyboards import get_main_keyboard, menu_btn_txt, price_btn_txt, call_btn_txt, get_food_keyboard, back_btn_txt, burger_btn_txt, get_burger_buttons
from service import *
import os
import json
from MyDB.db_main import SessionLocal
from MyDB.db_service import create_user
from MyDB.db_main import get_db
from abc import ABC, abstractmethod
from typing import Dict, Callable, Optional, Awaitable
import logging


logger = logging.getLogger(__name__)

class BaseHandler(ABC):
    def __init__(self):
        self._handlers: Dict[str, Callable[[Update, ContextTypes.DEFAULT_TYPE], Awaitable[None]]] = {}
        self._fallback_handler: Optional[Callable[[Update, ContextTypes.DEFAULT_TYPE], Awaitable[None]]] = None

    def register_handler(self, text: str, handler: Callable[[Update, ContextTypes.DEFAULT_TYPE], Awaitable[None]]):
        self._handlers[text] = handler

    def register_fallback(self, handler: Callable[[Update, ContextTypes.DEFAULT_TYPE], Awaitable[None]]):
        self._fallback_handler = handler

    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
        text = update.message.text.strip()
        logger.info(f"Handle input:{text}")

        handler = self._handlers.get(text)
        if handler:
            try:
                await handler(update, context)
                return True
            except Exception as e:
                logger.error(f"Error while handling '{text}': {e}")
                await self._handle_error(update, context, e)
                return False

        if self._fallback_handler:
            await self._fallback_handler(update, context)
            return True

        return False


    @abstractmethod
    async def _handle_error(self, update: Update, context: ContextTypes.DEFAULT_TYPE, error: Exception):
        pass


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    with get_db() as db:
        create_user(db, user.id, user.username)

    create_new_cart(user.id)


    await update.message.reply_text("С днём Рождения ❤", reply_markup=get_main_keyboard())

# Обработчик команды /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Я простой бот. Пока умею только здороваться!")

# Обработка ошибок
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")