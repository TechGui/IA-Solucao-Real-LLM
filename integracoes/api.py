import os
import requests
from dotenv import load_dotenv
from pathlib import Path

# Load .env
dotenv_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path)

API_TOKEN = os.getenv("HF_API_KEY")
model_name = "HuggingFaceH4/zephyr-7b-beta"
API_URL = f"https://api-inference.huggingface.co/models/{model_name}"

headers = {"Authorization": f"Bearer {API_TOKEN}"}

# System prompt para o Cubô
system_prompt = (
    "Você é um assistente de IA chamado Cubô. "
    "Responda sempre em português, de forma concisa, informal, objetiva e educada "
    "Não invente respostas criativas ou poéticas. "
    "Seja direto e responda apenas o que foi perguntado."
)

def enviar_mensagem_hf(mensagem):
    # Prompt específico para Zephyr
    prompt_completo = (
        "<|system|>\n"
        f"{system_prompt}\n\n"
        "<|user|>\n"
        f"{mensagem}\n\n"
        "<|assistant|>\n"
    )

    payload = {
        "inputs": prompt_completo,
        "parameters": {
            "max_new_tokens": 200,
            "temperature": 0.7,
        },
        "options": {"wait_for_model": True}
    }

    print("Aguardando resposta do modelo...")

    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        generated = response.json()[0]["generated_text"]
        # Para Zephyr, geralmente ele responde a partir da tag <|assistant|>
        # Então você pode tentar só pegar tudo depois de "<|assistant|>\n"
        if "<|assistant|>\n" in generated:
            resposta = generated.split("<|assistant|>\n")[-1].strip()
        else:
            resposta = generated.strip()
        return resposta
    else:
        return f"[ERRO] Hugging Face: {response.status_code} - {response.text}"
