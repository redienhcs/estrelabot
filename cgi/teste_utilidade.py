import win_unicode_console
win_unicode_console.enable()

#Ler o conteúdo de arquivos e descobrir se a resposta do chatbot foi útil
lista_de_arquivos = {
    "eventos.yml",
    "historia.yml",
    "meio_ambiente.yml",
    "perguntas_frequentes.yml"
}

conteudo_arquivos = ""

for arquivo in lista_de_arquivos:
    file = open(arquivo,'r', encoding="utf_8_sig")
    conteudo_arquivos += file.read()

frase_gerada = "A prefeitura de Estrela se localiza na Rua Júlio de Castilhos, 380"

resultado_busca = conteudo_arquivos.find( frase_gerada)

if resultado_busca > -1 :
    print("Segurir preencher o formulário")
    pass

print(resultado_busca)
