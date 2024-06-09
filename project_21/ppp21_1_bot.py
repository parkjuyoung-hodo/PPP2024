import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters

token = "7260035422:AAFBok6sQlmid2v-_149OCJJa_6g9ryVqWo"
id = "7496538268"

bot = telegram.Bot(token)
bot.sendMessage(chat_id=id, text="어디가 아프신가요?")

# updater
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()


# 사용자가 보낸 메세지를 읽어들이고, 답장을 보내줍니다.
# 아래 함수만 입맛에 맞게 수정해주면 됩니다. 다른 것은 건들 필요없어요.
def handler(update, context):
    user_text = update.message.text  # 사용자가 보낸 메세지를 user_text 변수에 저장합니다.
    if user_text == "머리":
        bot.send_message(chat_id=id, text="타이에놀을 먹으세요.")
        bot.send_message(chat_id=id, text="더 아픈 곳은 없으신가요?")

    elif user_text == "위":
        bot.send_message(chat_id=id, text="바로스콘더블약션현탁액을 먹으세요.")  # 답장 보내기
        bot.send_message(chat_id=id, text="더 아픈 곳은 없으신가요?")

    else:
        bot.send_message(chat_id=id, text="구글에 물어보세요.")


echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
