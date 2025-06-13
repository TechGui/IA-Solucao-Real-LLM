import speech_recognition as sr

def reconhecer_fala():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Fale com o Goku... (aguardando áudio)")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            texto = recognizer.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {texto}")
            return texto
        except sr.UnknownValueError:
            print("Não entendi o que você falou.")
            return None
        except sr.RequestError as e:
            print(f"[ERRO] Serviço de reconhecimento: {e}")
            return None
