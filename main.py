from integracoes.huggingface_api import enviar_mensagem_hf

print("Cubô está ao seu serviço. Digite 'sair' para encerrar.\n")

while True:
    entrada = input("Você: ")
    if entrada.lower() == "sair":
        break
    resposta = enviar_mensagem_hf(entrada)
    print("Cubô:", resposta)
