# 🤖 IA-Solucao-Real-LLM 

Um projeto de assistente pessoal controlado por voz que converte fala em texto, interpreta comandos usando um modelo de linguagem (LLM) da HuggingFace e responde com síntese de voz em português, este protótipo demonstra a integração de tecnologias modernas para criar uma interface conversacional completa com reconhecimento e síntese de voz.

---

## ✨ Funcionalidades

- 🎙️ Reconhecimento de voz (voz para texto) usando `speech_recognition`
- 🧠 Integração com modelo LLM da Hugging Face (Zephyr-7B-Beta)
- 🔊 Resposta em áudio (texto para voz) com o modelo `facebook/mms-tts-por`
- 📦 Modularizado para facilitar manutenção e expansão
- 🇧🇷 Suporte completo ao idioma português

---

## ▶️ Como executar

### 1. Clone o repositório:

```bash
git clone https://https://github.com/TechGui/IA-Solucao-Real-LLM
cd IA-Solucao-Real-LLM
```

### 2. Instale as dependências:

Recomenda-se o uso de ambiente virtual.

```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
```

### 3. Crie o arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
HF_API_KEY=sua_chave_api_da_huggingface
```

### 4. Execute o projeto:

```bash
python main.py
```

---

## 📚 Tecnologias Utilizadas

- [Python 3.12+](https://www.python.org/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [SoundDevice](https://python-sounddevice.readthedocs.io/)
- [Torch](https://pytorch.org/)
- [facebook/mms-tts-por](https://huggingface.co/facebook/mms-tts-por)
- [HuggingFaceH4/zephyr-7b-beta](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta)

---

## 🛠️ Possíveis melhorias futuras

- Interface gráfica com PyQt5 ou Tkinter
- Resposta multimodal (imagem + voz)
- Suporte a múltiplos idiomas
- Logging de conversas e comandos
- Reconhecimento de intenção do usuário

---

## 👨‍💻 Autores

**João Vitor Dolinski da Silva**  
Desenvolvedor, estudante de Análise e Desenvolvimento de Sistemas

**Guilherme da Rosa Silva**  
Desenvolvedor, estudante de Análise e Desenvolvimento de Sistemas

---

## 📄 Licença

Este projeto é de código aberto e você pode usá-lo como base livremente. 

---
