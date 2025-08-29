from telegram import Update
from telegram.ext import ContextTypes

from handlers.main_menu_handler import MainMenuHandler, register_main_menu_handlers
from handlers.food_menu_handler import FoodMenuHandler, register_food_menu_handlers

class RootMenuHandler:
    def __init__(self):
        self.main_handler = MainMenuHandler()
        self.food_handler = FoodMenuHandler()

        # Регистрируем хендлеры

        register_main_menu_handlers(self.main_handler)
        register_food_menu_handlers(self.food_handler)

    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        state = context.user_data.get("menu_state", "main")

        if state == "main":
            await self.main_handler.handle(update, context)
        elif state == "food":
            await self.food_handler.handle(update, context)
        else:
            await update.message.reply_text("❗️ Неизвестное состояние меню. Возвращаю в главное меню.")
            context.user_data["menu_state"] = "main"
            await self.main_handler.handle(update, context)
