from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler

from MyDB.database_init import init_db, test_connection
from handlers.basehandler import start_command, help_command, error
from handlers.main_menu_handler import MainMenuHandler, register_main_menu_handlers
from handlers.food_menu_handler import FoodMenuHandler, register_food_menu_handlers
from MyDB.mysql_connector import db
from MyDB.models import init_database
from dotenv import load_dotenv
import os

from handlers.root_menu import RootMenuHandler
from keyboards import menu_btn_txt

load_dotenv()

TOKEN = os.getenv("TOKEN")

BOT_USERNAME = "@MaryBreakfastBot"

def main():
    # db.connect()
    # init_database()
    init_db()
    test_connection()


    print("Бот запускается...")
    app = Application.builder().token(TOKEN).build()

    root_menu = RootMenuHandler()

    main_menu_handler = MainMenuHandler()
    food_menu_handler = FoodMenuHandler()


    #собираем все handlers
    register_main_menu_handlers(main_menu_handler)
    register_food_menu_handlers(food_menu_handler)

    # Регистрация команд
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    # Регистрация обработчика сообщений
    app.add_handler(MessageHandler(filters.TEXT, root_menu.handle))

    # Обработка ошибок
    app.add_error_handler(error)

    print("Бот работает!")
    app.run_polling()

    #когда бот завершается, то отключаемся от БД
    #db.disconnect()

    #запуск бота
if __name__ == "__main__":
    main()











