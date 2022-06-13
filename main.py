import CONSTANTS  as keys
from telegram.ext import *
import responses as R
import pandas_datareader as web

print("BOT STARTED")

def start_command(update,context):
    update.message.reply_text('type something to get started!')

def help_command(update,context):
    update.message.reply_text('if you need help ask GOOGLE')

def pasc_command(update,context):
    update.message.reply_text("""Association for computing machinery (ACM) is the world’s largest educational and scientific society,
    uniting educators, researchers and professors. PICT ACM student chapter (PASC) was established in 2011.
    PASC is awarded as BEST ACM STUDENT CHAPTER in India consecutively in 2018 and 2019.

    Link of PASC website : https://pict.acm.org
    """)

def pisb_command(update,context):
    update.message.reply_text("""PICT IEEE Student Branch (PISB) was established in the year 1988.
    PISB aims to escalate the knowledge and trends in the diverse fields of technologies amongst its members. 
    PISB upholds two major events every year - Credenz and Credenz Tech Dayz with the first one being conducted in odd semester and the latter one in even semester.
    PISB is also marked by its Women in Engineering (WIE) chapter, an initiative for empowerment of women.

    Link of PISB website : https://pictieee.in
    """)

def pcsb_command(update,context):
    update.message.reply_text("""PICT CSI Student Branch, working under CSI, was established in 2016.
     It provides a platform for technical and non-technical education. 
     One of our key strengths at PCSB is our rate of growth in a short span of time. 
     We take pride in the fact that we are one of the best student communities in Pune, still growing at an exponential rate.

     Link of PCSB website : https://www.pictcsi.com
    """)


def handle_message(update,context):
    text=str(update.message.text).lower()
    responses = R.sample_responses(text)

    update.message.reply_text(responses)

def stock(update,context):
    ticker = context.args[0]
    data =web.DataReader(ticker,'yahoo')
    price = data.iloc[-1]['Close']
    update.message.reply_text(f"The current price of {ticker} is {price:.2f}$")

def error(update,context):
    print(f"Update{update} caused error{context.error}")



def main():
    updater = Updater(keys.API_KEY, use_context =True)
    dp =updater.dispatcher

    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("pasc",pasc_command))
    dp.add_handler(CommandHandler("pisb",pisb_command))
    dp.add_handler(CommandHandler("pcsb",pcsb_command))
    dp.add_handler(CommandHandler("help",help_command))
    dp.add_handler(CommandHandler("stock",stock))
    dp.add_handler(MessageHandler(Filters.text,handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()   


