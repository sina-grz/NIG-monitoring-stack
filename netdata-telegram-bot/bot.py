from telegram.ext import Updater, InlineQueryHandler, CommandHandler ,MessageHandler, Filters
import sys 
import os
from get_docker_secret import get_docker_secret

class BotRun:
    def __init__(self,path):
        tk = get_docker_secret('TOKEN')
        updater = Updater(token=tk, use_context=True)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler('subscribe', self.sub))
        dispatcher.add_handler(CommandHandler('start', self.start))
        dispatcher.add_handler(CommandHandler('unsubscribe', self.unsub))
        dispatcher.add_handler(MessageHandler(Filters.text,self.passw))
        self.path = path
        updater.start_polling()
        self.func = ''
        self.msg = ''

    def sub(self,update, context):
        print('sub()')
        self.func = self.subscribe
        self.msg = 'subscribesd!'
        context.bot.send_message(chat_id=update.effective_chat.id, text="enter the passsword-id(if you want to subscribe/unsubscribe youre self just type nothong)")
    def start(self,update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="ok let start!")

    def unsub(self,update, context):
        self.func = self.unsubscribe
        self.msg = 'unsubscribed'
        context.bot.send_message(chat_id=update.effective_chat.id, text="enter the passsword-id"
                                    +"(if you want to subscribe/unsubscribe youre self just type nothong)")
            

    def passw(self,update, context):
        print('pass9')
        ls = update.message.text.split('-')
        print(ls)
        if ls[0] == 'admin':
            print('if1',len(ls))
            if len(ls) == 1:
                self.file = open(self.path,'r')
                
                self.func(update.effective_chat.id)
                context.bot.send_message(chat_id=update.effective_chat.id, text=self.msg)
                print('if2')
            else: 
                self.subscribe(int(ls[1]))
                print('else',ls[1])
                print('el2')
        else: context.bot.send_message(chat_id=update.effective_chat.id, text=self.msg)

    def subscribe(self,id):
        lines = self.file.readlines()
        
        index = 0
        for lne in lines: 
            if lne.startswith('DEFAULT_RECIPIENT_TELEGRAM'):
                print(index)
                break
            index += 1
        print(lines[index])
        print(id)
        nconf = lines[index].replace('DEFAULT_RECIPIENT_TELEGRAM="','DEFAULT_RECIPIENT_TELEGRAM="' +  str(id) + " ")
        print(nconf,8888)
        self.file.close()
        self.file = open(self.path, 'w')
        self.file.writelines(lines[0:index])
        self.file.writelines(nconf)
        self.file.writelines(lines[index + 1:])
        self.file.flush()
        self.file.close()

    def unsubscribe(self,id):
        lines = self.file.readlines()
        nconf = ''
        index = 0
        for lne in lines: 
            if lne.startswith('DEFAULT_RECIPIENT_TELEGRAM'):
                print(index)
                break
            index += 1
        print('un',index)
        if lines[index].__contains__(str(id)):
             print('found')
             nconf = lines[index].replace(str(id),'')
        else:
             nconf = lines[index]
        
        self.file.close()
        self.file = open(self.path, 'w')
        self.file.writelines(lines[0:index])
        self.file.writelines(nconf)
        self.file.writelines(lines[index + 1:])
        self.file.flush()
        self.file.close()

run = BotRun(sys.argv[1])
         


