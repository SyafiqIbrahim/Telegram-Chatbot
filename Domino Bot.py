#########################################################################
#Import packages/API
#########################################################################

from telegram import *
from telegram.ext import *
from requests import *
import time

#########################################################################
#Key in telebot token
#########################################################################

Token = Updater(token="5370884936:AAFLhMKPWXOnPM7hYE1oCg1QCKopHXigIJY")
Dispatch = Token.dispatcher

#########################################################################
#set Variables
#########################################################################

ImageURL = "https://share1.cloudhq-mkt3.net/b6de58cd8a0856.jpeg"
GifURL = 'https://u01.appmifile.com/images/2019/09/10/b3788a8e-24d2-41b3-91c4-131968dab219.gif'
Website = "https://bit.ly/3GBJXCo"

#########################################################################
#Create Definitions
#########################################################################


def startCommand(update: Update, context: CallbackContext):
    gif = get(GifURL).content
    buttons = [[InlineKeyboardButton("Spin the wheel!", callback_data="spin")]]
    context.bot.sendMediaGroup(
        chat_id=update.effective_chat.id,
        media=[
            InputMediaPhoto(
                gif,
                caption=" Spin the wheel for a chance to win a FREE pizza!")
        ])
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Would you like to spin?",
                             reply_markup=InlineKeyboardMarkup(buttons))


def Spin(update: Update, context: CallbackContext):
    if update.callback_query.data == "spin":
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Spinning...")
        time.sleep(2)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Spinning....")
        time.sleep(2)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Spinning.....")
        time.sleep(2)

        image = get(ImageURL).content
        buttons = [[InlineKeyboardButton("Yes", callback_data="Yes")],
                   [InlineKeyboardButton("No, thanks.", callback_data="No")]]
        context.bot.sendMediaGroup(
            chat_id=update.effective_chat.id,
            media=[
                InputMediaPhoto(
                    image,
                    caption=" CONGRATULATIONS! You have won a FREE Pizza!")
            ])
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Do YOU want it?",
                                 reply_markup=InlineKeyboardMarkup(buttons))

    if update.callback_query.data == "Yes":
        buttons = [[InlineKeyboardButton("Claim HERE!", url=Website)]]
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=
            "Wonderful! Please click on the link below to claim your FREE pizza!",
            reply_markup=InlineKeyboardMarkup(buttons))
    if update.callback_query.data == "No":
        buttons = [[InlineKeyboardButton(("Bye!"), callback_data="bye")]]
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="That's okay, see you!",
                                 reply_markup=InlineKeyboardMarkup(buttons))


#########################################################################
#Call Definition
#########################################################################

Dispatch.add_handler(CommandHandler("start", startCommand))
Dispatch.add_handler(CallbackQueryHandler(Spin))

#########################################################################
#Start Bot
#########################################################################

Token.start_polling()
