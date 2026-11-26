import truststore
truststore.inject_into_ssl()

import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from agente import responder, conversar

load_dotenv()

async def ao_receber(update, context):
    usuario = update.effective_chat.id
    text = update.message.text
    await update.message.reply_text(responder(usuario, text))

app = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ao_receber))

print("Bot no AR!")
app.run_polling()