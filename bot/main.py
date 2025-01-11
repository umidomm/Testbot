from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from api_handler.api import get_token, get_all_admins, get_all_users
from pdf_generator.h import write_users_to_pdf
from pdf_generator.g import analyze_pdfs, create_pdf

# دستور شروع
def start(update: Update, context: CallbackContext):
    update.message.reply_text("سلام! به ربات مدیریت خوش آمدید.")

# دستور دریافت توکن
def fetch_token(update: Update, context: CallbackContext):
    try:
        username, password = context.args
        token = get_token(username, password)
        if token:
            update.message.reply_text(f"توکن دریافت شد: {token}")
        else:
            update.message.reply_text("خطا در دریافت توکن.")
    except ValueError:
        update.message.reply_text("فرمت دستور صحیح نیست. مثال: /token username password")

# دستور تولید PDF
def generate_pdf(update: Update, context: CallbackContext):
    directory = "./pdf_generator"
    total_usages = analyze_pdfs(directory)
    if total_usages:
        output_file = os.path.join(directory, "invoice.pdf")
        create_pdf(total_usages, output_file)
        update.message.reply_document(open(output_file, 'rb'))
    else:
        update.message.reply_text("هیچ داده‌ای پیدا نشد.")

def main():
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("token", fetch_token))
    dispatcher.add_handler(CommandHandler("generate_pdf", generate_pdf))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
