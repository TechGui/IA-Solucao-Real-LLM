from transformers import pipeline
import torch
import sounddevice as sd
import numpy as np

# Verifica se há GPU disponível
device = 0 if torch.cuda.is_available() else -1

# Cria o pipeline de texto para voz com aceleração via GPU
tts = pipeline("text-to-speech", model="facebook/mms-tts-por", device=device)

def texto_para_voz(texto):
    audio = tts(texto)
    audio_array = audio["audio"]
    sample_rate = audio["sampling_rate"]

    # Ajuste do formato para reprodução imediata
    if isinstance(audio_array, list):
        audio_array = np.array(audio_array)
    if len(audio_array.shape) > 1:
        audio_array = audio_array.squeeze()
    if audio_array.dtype != np.float32:
        audio_array = audio_array.astype(np.float32)

    sd.play(audio_array, samplerate=sample_rate)
    sd.wait()
