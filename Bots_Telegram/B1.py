import telebot

CHAVE_API = "5362897913:AAFkqmaFg3VJnRNYEB30yAT5EhCgGbpYNVY"

bot = telebot.TeleBot(CHAVE_API)

############################################################################### Comandodos ###############################################################################

@bot.message_handler(commands=['DizerBatata'])
def responder(mensagem):
    bot.send_message(mensagem.chat.id, "batata")
    
@bot.message_handler(commands=['DizerTomate'])
def responder(mensagem):
    bot.reply_to(mensagem, "tomate")
        
############################################################################### Verificadores ###############################################################################
        
def verificar(mensagem):
    return True

############################################################################### Mensagens ###############################################################################

@bot.message_handler(func=verificar)
def responder(mensagem):
    if mensagem.text == "batata":
        texto = "sim, batata"
    else:
        texto = """Escolha um Comando:
    /DizerBatata
    /DizerTomate"""    
    bot.reply_to(mensagem, texto)

############################################################################### Analise de Texto ###############################################################################

bot.polling()