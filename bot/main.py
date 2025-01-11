import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv

# بارگذاری متغیرهای محیطی
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("توکن ربات تنظیم نشده است!")

# دستور شروع
def start(update: Update, context: CallbackContext):
    update.message.reply_text("سلام! به ربات خوش آمدید. برای تنظیم آدرس پنل از دستور /set_panel استفاده کنید.")

# دستور تنظیم آدرس پنل
def set_panel(update: Update, context: CallbackContext):
    if len(context.args) != 1:
        update.message.reply_text("فرمت دستور صحیح نیست. مثال: /set_panel https://your-panel.com")
        return
    
    panel_url = context.args[0]
    if not panel_url.startswith("http"):
        update.message.reply_text("لطفاً یک آدرس معتبر وارد کنید.")
        return

    # ذخیره آدرس پنل در فایل .env
    with open(".env", "a") as env_file:
        env_file.write(f"\nBASE_URL={panel_url}")
    
    update.message.reply_text(f"آدرس پنل تنظیم شد: {panel_url}")

# اجرای اصلی
def main():
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("set_panel", set_panel))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
