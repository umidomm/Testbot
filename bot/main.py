import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv

# بارگذاری متغیرهای محیطی
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("توکن ربات تنظیم نشده است!")

# دستور شروع
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! به ربات خوش آمدید. برای تنظیم آدرس پنل از دستور /set_panel استفاده کنید.")

# دستور تنظیم آدرس پنل
async def set_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1:
        await update.message.reply_text("فرمت دستور صحیح نیست. مثال: /set_panel https://your-panel.com")
        return
    
    panel_url = context.args[0]
    if not panel_url.startswith("http"):
        await update.message.reply_text("لطفاً یک آدرس معتبر وارد کنید.")
        return

    # ذخیره آدرس پنل در فایل .env
    with open(".env", "a") as env_file:
        env_file.write(f"\nBASE_URL={panel_url}")
    
    await update.message.reply_text(f"آدرس پنل تنظیم شد: {panel_url}")

# اجرای اصلی
def main():
    # ایجاد برنامه
    application = Application.builder().token(BOT_TOKEN).build()

    # ثبت دستورات
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("set_panel", set_panel))

    # اجرای برنامه
    application.run_polling()

if __name__ == "__main__":
    main()
