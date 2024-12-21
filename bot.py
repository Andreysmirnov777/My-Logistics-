from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update: Update, context):
    await update.message.reply_text(f"Привет, {update.effective_user.first_name}!")

if __name__ == "__main__":
    app = ApplicationBuilder().token("7361098927:AAH3eCbzi0k7XmNtAf3hBcxz7bMiiBDjFx4").build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен!")
    app.run_polling()
  
