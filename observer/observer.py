class ContadorDePalavras:
    @staticmethod
    def contar(frase):
        frase = frase.strip()
        palavras = frase.split()
        return len(palavras)


class ContadorDePalavrasPares:
    @staticmethod
    def contar(frase):
        frase = frase.strip()
        palavras = frase.split()

        palavras_pares = 0
        for palavra in palavras:
            if len(palavra) % 2 == 0:
                palavras_pares += 1

        return palavras_pares


class ContadorPalavrasMaiusculo:
    @staticmethod
    def contar(frase):
        frase = frase.strip()
        palavras = frase.split()

        palavras_maiusculas = 0
        for palavra in palavras:
            if palavra[0].isupper():
                palavras_maiusculas += 1

        return palavras_maiusculas


class Observavel:
    def __init__(self):
        self.observers = []

    def registrar_observer(self, observer):
        self.observers.append(observer)

    def remover_observer(self, observer):
        self.observers.remove(observer)

    def notificar_observers(self, data):
        for observer in self.observers:
            observer.update(data)


class Observer:
    def update(self, data):
        pass


# Implementação concreta do observer
class ConcreteObserver(Observer):
    def update(self, data):
        print("Frase enviada:", data)
        print("A frase contém " + str(ContadorDePalavras.contar(data)) + " palavras, das quais " +
              str(ContadorDePalavrasPares.contar(data)) + " são pares e " +
              str(ContadorPalavrasMaiusculo.contar(data)) + " são maiúsculas.\n")


# Exemplo de uso
observavel = Observavel()

observer1 = ConcreteObserver()
observer2 = ConcreteObserver()

observavel.registrar_observer(observer1)
observavel.registrar_observer(observer2)

observavel.notificar_observers("Manda um salvin ai")

observavel.remover_observer(observer2)

observavel.notificar_observers("Observer2 foi removido.")
