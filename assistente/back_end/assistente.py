from utils import constantes
from back_end import service
from speech_recognition import *
import pyttsx3
import random


class Assistente:
    def __init__(self):
        self.reconhecedor_de_voz = Recognizer()
        self.microfone = Microphone()
        self.leitor = pyttsx3.init()
        self.finalizar = False
        self.esta_falando = False
        self.aplicar_configuracoes_de_voz()

    def executar_assistente(self):

        while not self.finalizar:
            # Captura de áudio
            with self.microfone as source:
                # Algoritmo de reducao de ruidos no som
                self.reconhecedor_de_voz.adjust_for_ambient_noise(source)
                if self.esta_falando:
                    self.falar_texto(constantes.FALA_ESTOU_OUVINDO)
                # Armazena o que foi dito em uma variavel
                audio = self.reconhecedor_de_voz.listen(source)

            # Reconhecimento de fala
            try:
                # Algoritmo reconhecedor de padroes
                query = self.reconhecedor_de_voz.recognize_google(
                    audio, language="pt-BR")

                if self.esta_falando:
                    if query.__contains__('finalizar'):
                        self.finalizar = True
                        self.falar_texto(constantes.FALA_FINALIZAR_PROGRAMA)
                    else:
                        resposta = service.enviar_pergunta(query)
                        self.falar_texto(resposta)
                        self.esta_falando = False
                        query = ''  # caso o texto falado contenha a palavra safira, não vai cair em um loop
                        self.falar_texto(constantes.FALA_FINALIZAR_AUXILIO)

                if query.upper().__contains__(constantes.FALA_INICIAR):
                    self.falar_texto(constantes.FALA_SAUDACAO)
                    self.esta_falando = True

            except UnknownValueError:
                if self.esta_falando:
                    self.falar_texto(
                        constantes.LISTA_FALAS_INCOMPREENDIDAS[random.randrange(0, len(constantes.LISTA_FALAS_INCOMPREENDIDAS)-1)])
                    print("Não foi possível entender o que você disse.")
            except RequestError as e:
                print(
                    f"Erro ao conectar-se ao serviço de reconhecimento de fala: {e}")
                self.falar_texto(constantes.FALA_ERRO_CONEXAO)
            except Exception as e:
                print(f"Erro: {e}")
                self.falar_texto(constantes.FALA_ERRO_GENERICO)

    def falar_texto(self, texto):

        self.leitor.say(texto)
        self.leitor.runAndWait()
        self.leitor.stop()

    def aplicar_configuracoes_de_voz(self):
        # aplicando a velocidade de fala uma taxa de 70
        self.leitor.setProperty('taxa', 150)
