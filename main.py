from integracoes.api import enviar_mensagem_hf
from integracoes.texto_para_voz import texto_para_voz
from integracoes.voz_para_texto import reconhecer_fala

print("Cubô está ao seu serviço. Fale 'sair' para encerrar.\n")

while True:
    entrada = reconhecer_fala()
    if not entrada:
        continue

    if entrada.lower() == "sair":
        break

    resposta = enviar_mensagem_hf(entrada)
    print("Cubô:", resposta)
    texto_para_voz(resposta)
