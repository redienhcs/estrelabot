import win_unicode_console
win_unicode_console.enable()

#Ler o conteúdo de arquivos e descobrir se a resposta do chatbot foi útil
lista_de_arquivos = {
    "eventos.yml",
    "historia.yml",
    "meio_ambiente.yml",
    "perguntas_frequentes.yml"
}




def ler_conteudo_dos_arquivos( ):
        conteudo_arquivos = ""

        for arquivo in lista_de_arquivos:
            file = open(arquivo,'r', encoding="utf_8_sig")
            conteudo_arquivos += file.read()
        return conteudo_arquivos

def verificar_presenca_frase( frase):
    conteudo_arquivos = ler_conteudo_dos_arquivos()

    return conteudo_arquivos.find( frase)

frase_gerada = "A prefeitura de Estrela se localiza na Rua Júlio de Castilhos, 389"


if verificar_presenca_frase( frase_gerada) > -1 :
    print("Segerir preencher o formulário")
else:
    print("Conversa normal")
