import random

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso',
            'Não sei, você que sabe',
            'Não faz isso não',
            'Acho que tá na hora certa!'
        ]

    def Iniciar(self):
        input("Faça sua pergunta: ")
        print(random.choice(self.respostas))

decida = DecidaPorMim()
decida.Iniciar()

