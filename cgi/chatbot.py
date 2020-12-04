#!/usr/bin/env python3

from flask import Flask, request
from flask_cors import CORS
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import unicodedata

app = Flask(__name__)
cors = CORS(app)


#Ler o conteúdo de arquivos e descobrir se a resposta do chatbot foi útil
lista_de_arquivos = {
    "portuguese/eventos.yml",
    "portuguese/historia.yml",
    "portuguese/meio_ambiente.yml",
    "portuguese/perguntas_frequentes.yml"
}


def ler_conteudo_dos_arquivos( ):
        conteudo_arquivos = ""

        for arquivo in lista_de_arquivos:
            file = open(arquivo,'r', encoding="utf_8_sig")
            conteudo_arquivos += file.read()
        return conteudo_arquivos

#Utilizado para
def verificar_presenca_frase( frase):
    conteudo_arquivos = ler_conteudo_dos_arquivos()

    return conteudo_arquivos.find( frase)

def gravar_log_chatbot( str_log):
    file = open("chatbot_log.txt","a")
    file.write( str_log)
    file.close()


@app.route("/", methods=['GET','POST'])
def send_form():
    if request.method == 'GET' :
        dados_enviados = request.args.get('msg')
        return "Atingiu o servidor:{}".format(dados_enviados)

    #Se o tipo de methodo utilizado é igual a POST
    if request.method == 'POST':
        #Pega o tipo de requisição enviada
        op = request.form.get('op')

        #Verifica se o tipo de requisição é para o ChatterBot
        if op == 'chat_response':
            #Pega a mensagem enviada pelo usuário via POST
            msg_post = request.form.get('mensagem')

            #grava a pergunta do usuário no log do chatbot
            gravar_log_chatbot( "#{}".format(msg_post)+"\n")

            #Inicializa o chatterbot
            chatterbot = ChatBot('Prefeitura Estrela')

            #executar chatterbot
            chatterbot_response = str(chatterbot.get_response( msg_post))

            if not chatterbot_response :
                chatterbot_response = "Desculpe, não entendi... poderia repetir?"

            #Grava a resposta do chatterbot no log do chatbot
            gravar_log_chatbot( "]{}".format(chatterbot_response)+"\n")

            #verificar se a pergunta contêm alguma coisa sobre o coronavírus
            lower_mensagem_usuario = msg_post.lower()
            lower_mensagem_usuario = str(unicodedata.normalize('NFKD', lower_mensagem_usuario).encode('ASCII', 'ignore'))[2:]
            if lower_mensagem_usuario.find("coronavirus") > -1 or lower_mensagem_usuario.find("covid") > -1:
                chatterbot_response = "Parece que você está buscando por questões relacionadas ao COVID-19. Para mais informações sobre o assunto, por favor siga esse link da Prefeitura Municipal de estrela com as notívias mais recentes <a href=\"https://estrela.atende.net/#!/tipo/noticia\">Notícias prefeitura de Estrela </a>"
                chatterbot_response += "<div class=\"useful_info\"><br />Esta resposta foi útil? Gostaria de responder a um questionário para ajudar a melhorar este bot?"
                chatterbot_response += "<br />resposta as perguntas neste formulário: <a href=\"https://forms.gle/e2J1jDvtYdHyvD8R8\">Link para o formulário</a></div> "

            if verificar_presenca_frase( chatterbot_response) > -1 :
                mensagem_de_retorno = '{}'.format(chatterbot_response)
                mensagem_de_retorno += "<div class=\"useful_info\"><br />Esta resposta foi útil? Gostaria de responder a um questionário para ajudar a melhorar este bot?"
                mensagem_de_retorno += "<br />resposta as perguntas neste formulário: <a href=\"https://forms.gle/e2J1jDvtYdHyvD8R8\">Link para o formulário</a></div> "
                return mensagem_de_retorno
            else:
                return '{}'.format( chatterbot_response)
        else :
            msg_post = request.form.get('mensagem')
            return "recebi:{}".format(msg_post)



#if __name__ == "__main__":
 #   app.run()
