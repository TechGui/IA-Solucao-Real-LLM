import os
from .gemini_integration import GeminiClient

def run_gemini_exemplo():
    try:
        print("Iniciando a geracao de texto do Gemini...")
        text_client = GeminiClient(model_name='')
    except ValueError as e:
        print(f"Erro da API: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")