from telegram import Update, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Inserisci qui il token del tuo bot
TOKEN = '8194113255:AAEQLG_T28CcJYXw5hEOuSEkBLUxoPCeASA'

# Inserisci qui l'ID del gruppo Telegram dove vuoi inoltrare le immagini
# Per trovare l'ID gruppo:
# 1) Aggiungi il bot al gruppo
# 2) Scrivi /start nel gruppo
# 3) Usa questo codice: print(update.message.chat_id) (lo vediamo insieme se vuoi)
GROUP_ID = -1002825092884  # esempio: negativo perché è gruppo

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ciao! Mandami foto in privato e le inoltrerò nel gruppo in modo anonimo.")
    print(update.message.chat_id)

async def forward_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type != "private":
        # Ignora messaggi non privati
        return
    photo = update.message.photo[-1]
    caption = update.message.caption or ""
    # Inoltra la foto al gruppo senza info mittente
    await context.bot.send_photo(chat_id=GROUP_ID, photo=photo.file_id, caption=caption)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO & filters.ChatType.PRIVATE, forward_photo))
    print("Bot anonimo avviato...")
    app.run_polling()
