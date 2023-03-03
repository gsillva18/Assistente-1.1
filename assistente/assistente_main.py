from back_end import assistente


class Main:
    def __init__(self):
        # aqui instanciamos o assistente
        self.assistente = assistente.Assistente()
        self.assistente.executar_assistente()


aplication = Main()
