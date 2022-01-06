import crawler
class telbot:
    def read_token(self):
        try:
            f=open('LSA1101_bot_api.TXT','r')
        except:
            print("can't find token file")
        self.token=f.read()
        print(self.token)
        f.close()
    def __init__(self):
        self.read_token()
    def startbot(self):
        from telegram.ext import Updater # 更新者
        from telegram.ext import CommandHandler, CallbackQueryHandler # 註冊處理 一般用 回答用
        from telegram.ext import MessageHandler, Filters # Filters過濾訊息
        from telegram import InlineKeyboardMarkup, InlineKeyboardButton # 互動式按鈕
        # 初始化bot
        self.updater = Updater(token=self.token, use_context=False)
        self.dispatcher = self.updater.dispatcher
        self.dispatcher.add_handler(CommandHandler('hi', self.hi))
        self.dispatcher.add_handler(CommandHandler('luckycolor', self.luckycolor))
        self.dispatcher.add_handler(CommandHandler('off', self.off))
    def hi(self,bot, update): # 新增指令/start
        message = update.message
        chat = message['chat']
        update.message.reply_text(text='HI  ' + str(chat['first_name'])+' '+str(chat['last_name']))    
    def luckycolor(self,bot,update):
        message=update.message
        starsign=list(message['text'])
        starsign=starsign[12:]
        starsign=''.join(starsign)
        print(starsign)
        if starsign=="":
            update.message.reply_text(text='請在指令後方加入星座')
            return
        mysearch=crawler.Fetch()
        if mysearch.isin(starsign):
            update.message.reply_text(text='稍等一下，正在查詢....')
            mysearch.get_html(starsign)
            update.message.reply_text(text='今天'+starsign+'的幸運顏色是: '+mysearch.luckycolor)
            mysearch.end()
        else:
            update.message.reply_text(text='沒有'+starsign+'這個星座')
        
    def off(self,bot,update):
        print("turn off")
        self.updater.stop()
if __name__=='__main__':
    mybot=telbot()
    mybot.startbot()
    mybot.updater.start_polling()
    while True:
        text = input()
        # Gracefully stop the event handler
        if text == 'stop':
            mybot.updater.stop()
            break

        # else, put the text into the update queue to be handled by our handlers
        elif len(text) > 0:
            mybot.update_queue.put(text)
