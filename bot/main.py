import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv
from api_handler.api import get_token, get_all_admins, get_all_users
from pdf_generator.h import write_users_to_pdf
from pdf_generator.g import analyze_pdfs, create_pdf

# بارگذاری متغیرهای محیطی از فایل .env
load_dotenv()

# دریافت توکن از فایل .env
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("⚠️ توکن ربات در فایل .env یافت نشد!")

# دستورات ربات
def start(update: Update, context: CallbackContext):
    update.message.reply_text("سلام! به ربات مدیریت خوش آمدید.")

def fetch_token(update: Update, context: CallbackContext):
    update.message.reply_text("این دستور برای دریافت توکن طراحی شده است.")

def generate_pdf(update: Update, context: CallbackContext):
    directory = "./pdf_generator"
    total_usages = analyze_pdfs(directory)
    if total_usages:
        output_file = os.path.join(directory, "invoice.pdf")
        create_pdf(total_usages, output_file)
        update.message.reply_document(open(output_file, 'rb'))
    else:
        update.message.reply_text("هیچ داده‌ای پیدا نشد.")

# اجرای اصلی
def main():
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("token", fetch_token))
    dispatcher.add_handler(CommandHandler("generate_pdf", generate_pdf))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
