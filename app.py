from flask import Flask, request, render_template, jsonify
import speech_recognition as sr
import pyttsx3

app = Flask(__name__)

class ReconhecedorVoz:
    def __init__(self, idioma="pt-BR", taxa_fala=150, volume=0.9):
        self.idioma = idioma
        self.reconhecedor = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.configurar_sintetizador(taxa_fala, volume)

    def configurar_sintetizador(self, taxa_fala, volume):
        self.engine.setProperty('rate', taxa_fala)
        self.engine.setProperty('volume', volume)

    def reconhecer_fala(self):
        with sr.Microphone() as fonte:
            self.reconhecedor.adjust_for_ambient_noise(fonte)
            try:
                audio = self.reconhecedor.listen(fonte, timeout=5, phrase_time_limit=10)
                return self.reconhecedor.recognize_google(audio, language=self.idioma)
            except sr.UnknownValueError:
                return "Não entendi o que foi dito."
            except sr.RequestError:
                return "Erro ao se conectar com o serviço de reconhecimento de voz."
            except sr.WaitTimeoutError:
                return "Tempo de captação expirado. Tente novamente."

    def falar_texto(self, texto):
        if texto:
            self.engine.say(texto)
            self.engine.runAndWait()

reconhecedor = ReconhecedorVoz()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/reconhecer_fala', methods=['POST'])
def reconhecer_fala():
    texto_reconhecido = reconhecedor.reconhecer_fala()
    return jsonify({"texto": texto_reconhecido})

@app.route('/falar_texto', methods=['POST'])
def falar_texto():
    texto = request.json.get("texto", "")
    reconhecedor.falar_texto(texto)
    return jsonify({"status": "Texto falado com sucesso."})

if __name__ == '__main__':
    app.run(debug=True)
