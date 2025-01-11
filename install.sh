#!/bin/bash

echo "شروع نصب..."

sudo apt update -y
sudo apt install -y python3 python3-venv python3-pip git

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "توکن ربات تلگرام را وارد کنید:"
read BOT_TOKEN
echo "BOT_TOKEN=$BOT_TOKEN" > .env

echo "ربات در حال اجرا است..."
python bot/main.py
