#!/bin/bash

echo "شروع نصب پروژه روی سرور اوبونتو..."

# 1. به‌روزرسانی مخازن
echo "به‌روزرسانی مخازن اوبونتو..."
sudo apt update -y

# 2. نصب پیش‌نیازهای سیستم
echo "نصب پیش‌نیازهای سیستم..."
sudo apt install -y python3 python3-venv python3-pip git

# 3. ایجاد محیط مجازی
echo "ایجاد محیط مجازی..."
python3 -m venv venv

# فعال کردن محیط مجازی
source venv/bin/activate

# 4. نصب وابستگی‌ها
echo "نصب وابستگی‌های پروژه..."
pip install --upgrade pip
pip install -r requirements.txt

# 5. درخواست توکن از کاربر
echo "لطفاً توکن ربات تلگرام را وارد کنید:"
read BOT_TOKEN

# ذخیره توکن در فایل .env
echo "BOT_TOKEN=$BOT_TOKEN" > .env
echo "توکن با موفقیت در فایل .env ذخیره شد."

# 6. بررسی پوشه‌های ضروری
echo "بررسی پوشه‌های ضروری..."
ASSETS_DIR="pdf_generator/assets"
if [ ! -d "$ASSETS_DIR" ]; then
    echo "پوشه assets یافت نشد. در حال ایجاد..."
    mkdir -p "$ASSETS_DIR"
    echo "پوشه $ASSETS_DIR ایجاد شد."
else
    echo "پوشه $ASSETS_DIR وجود دارد."
fi

# بررسی فایل‌های لوگو و فونت
LOGO_PATH="$ASSETS_DIR/logo.png"
FONT_PATH="$ASSETS_DIR/Vazir.ttf"

if [ ! -f "$LOGO_PATH" ]; then
    echo "⚠️ فایل لوگو ($LOGO_PATH) موجود نیست. لطفاً آن را به صورت دستی اضافه کنید."
else
    echo "✅ فایل لوگو یافت شد."
fi

if [ ! -f "$FONT_PATH" ]; then
    echo "⚠️ فایل فونت ($FONT_PATH) موجود نیست. لطفاً آن را به صورت دستی اضافه کنید."
else
    echo "✅ فایل فونت یافت شد."
fi

# 7. پایان نصب
echo "✅ نصب پروژه با موفقیت به پایان رسید!"
echo "برای فعال‌سازی محیط مجازی از دستور زیر استفاده کنید:"
echo "source venv/bin/activate"
echo "برای اجرای ربات فایل bot/main.py را اجرا کنید."
