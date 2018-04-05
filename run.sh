#!/bin/sh
set -e

# POSTFIX CONFIG
echo "Postfix config.."
sed -i 's/mail.example.com/'$FAKE_DOMAIN'/g' /etc/postfix/main.cf

# RUN APP
echo "Running Bot.."
python3 /opt/mailbot/mailbot.py -t $TELEGRAM_BOT_TOKEN -d $FAKE_DOMAIN -i $TELEGRAM_USER_ID

exec "$@"
