#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram import Update, ForceReply, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from kur_verisi_al import KurKontrol as kk
import math
import telegram

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def AsalKontrol(s):
    Asal = True
    for i in range(2, round(math.sqrt(s))):
        if(s % i == 0):
            Asal = False
            break
    if(Asal):
        return "Sayı Asal."
    else:
        return "Sayı Asal Değil."

# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )




def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Yardıma mı ihtiyacın var?')

def tek_mi(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    
    
    user = update.message.from_user
    print(user)
    try:
        first_name = str(user["first_name"])
    except:
        first_name = ""
        
    try:
        last_name = str(user["last_name"])
    except:
        last_name = ""
    
    if(user["id"] == 426488428):
        msg = "Hoşgeldin " + first_name + " " + last_name
        msg += "\nKullanıcı ID'niz: " + str(user["id"])
        update.message.reply_text(msg)
        sayi = update.message.text.split(" ")[-1]
        update.message.reply_text("Tek" if int(sayi) % 2 == 1 else "Çift")
        
        # print(update.message.text)
    # print(user)
    
def asal(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    user = update.message.from_user
    if(user["id"] == 426488428):
        sayi = update.message.text.split(" ")[-1]
        update.message.reply_text(AsalKontrol(int(sayi)))
        
        # print(update.message.text)
    # print(user)
    
def kur(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /kur is issued."""    
    user = update.message.from_user
    # update.message.reply_text("Cevap alınıyor. Lütfen bekleyiniz...")
    if(user["id"] == 426488428):
        keyboard = [
            [
                InlineKeyboardButton('\U0001F4B2 ' + "Dolar", callback_data='Dolar'),
                InlineKeyboardButton('\U0001F4B6 ' + "Euro", callback_data='Euro'),
            ],
            [InlineKeyboardButton('\U0001F4AA ' + "Altın", callback_data='Altın')],
            [
                InlineKeyboardButton('\U0001F48D ' + "Gümüş", callback_data='Gumus'),
                InlineKeyboardButton('\U0001F494 ' + "Platin", callback_data='Platin') 
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text('Hangisini görmek istersiniz?', reply_markup=reply_markup)
       
    else:
        update.message.reply_text('Bu botu kullanmaya yetkiniz yok!')
        

def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query    
    tur = query.data
    if("ALTIN" in tur.upper()):
        sonuc = kk.Altin()
    elif("DOLAR" in tur.upper()):
        sonuc = kk.Dolar()
    elif("EURO" in tur.upper()):
        sonuc = kk.Euro()
    elif("GUMUS" in tur.upper()):
        sonuc = kk.Gumus()
    elif("PLATIN" in tur.upper()):
        sonuc = kk.Platin()
    elif("PARITE" in tur.upper()):
        sonuc = kk.Parite()
    query.edit_message_text(text=f"{query.data} Kuru: {sonuc}")

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)
    

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("7144099326:AAHa2zHgkaFmwLORg5aqs4K31uNawTYt-Sg")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("tekmi", tek_mi))
    dispatcher.add_handler(CommandHandler("kur", kur))
    dispatcher.add_handler(CommandHandler("asal", asal))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    