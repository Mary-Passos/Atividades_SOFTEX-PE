from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass

try:
    animal = Animal()
except Exception as e:
    print(f"Erro gerado: {type(e).__name__}: {e}")

    #tive dificuldade nessa, então acabei utilizando IA para me ajudar. :,)