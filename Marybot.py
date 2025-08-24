from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from handlers.basehandler import start_command, help_command, error
from handlers.message_handler import message_handler, handle_message
from handlers.menu_handler import menu_handler
from database.mysql_connector import db
from database.models import init_database
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")

BOT_USERNAME = "@MaryBreakfastBot"

def main():
    db.connect()
    init_database()

    print("Бот запускается...")
    app = Application.builder().token(TOKEN).build()


    #собираем все handlers
    message_handler.register_handlers()
    menu_handler.register_menu_handlers()

    # Регистрация команд
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    # Регистрация обработчика сообщений
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Обработка ошибок
    app.add_error_handler(error)

    print("Бот работает! Нажми Ctrl+C для остановки.")
    app.run_polling()

    #когда бот завершается, то отключаемся от БД
    #db.disconnect()

    #запуск бота
if __name__ == "__main__":
    main()











