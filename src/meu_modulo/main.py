import sys

from algoritmos import detectar_vacas

if __name__ == "main":
    video_path = "src/meu_modulo/vacas.mp4"
    detectar_vacas.detectar_vacas(video_path)

