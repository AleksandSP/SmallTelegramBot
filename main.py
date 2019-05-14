import telebot

token = "YOUR_Token"

bot = telebot.TeleBot(token)

upd = bot.get_updates();
@bot.message_handler(commands=['help'])
def handle_text(message) :
    bot.send_message(message.chat.id, "Программа не работает если твой id не внесён в переменную myid,сделано для легкой персонализации пользователей ботом!")
@bot.message_handler(commands=['start'])
def handle_text(message):
        bot.send_message(message.chat.id, "Программа работает только для активированных id")
myid=YOUR_ID
#(легко получить гэт апдейтом)
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if((message.chat.type=="group") or (message.chat.type=="supergroup")) :
        uniq(message.chat.id)
    if((message.chat.id==myid)or(message.chat.id==myid1)):
        f = open('text.txt', 'r')
        for IdGroup in f:
            chat_id=IdGroup
            bot.forward_message(chat_id,message.chat.id,message.message_id)

def uniq(id) :
    f = open('text.txt', 'r')
    for IdGroup in f:
        IdGroup=int(IdGroup)
        if (IdGroup==id) :
            id="1"
    f.close()
    if(id!="1"):
        f = open('text.txt', 'a')
        f.write(str(id)+ '\n')
        f.close()
#with open('text.txt') as result:
#uniqlines = set(result.readlines())
#with open('text.txt', 'w') as rmdup:
#rmdup.writelines(set(uniqlines))"""

bot.polling(none_stop=True, interval=0)
