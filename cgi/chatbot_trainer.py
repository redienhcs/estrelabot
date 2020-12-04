#Chatbot trainer

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#Cria uma nova instância do chatbot
chatbot = ChatBot('Prefeitura Estrela')


# Cria uma instância do trainer
trainer = ChatterBotCorpusTrainer(chatbot)



# Treina o chatbot com base no corpus e português
print("Iniciando treinamento...")

trainer.train(
    "./portuguese/",
)

