from dataclasses import dataclass
from math import sqrt, pow

print(pow(2, 10))

@dataclass()
class  Ponto:
    x: int
    y: int

    def distance_to(self, pt2: 'Ponto'):
        x = pt2.x - self.x
        x = pt2.y - self.y

        return sqrt(pow(x, 2) + pow(y, 2))
        pass


@dataclass
class Morada:
    rua: str
    porta: str
    apt: str

@dataclass
class Pessoa:
    nome: str
    idade: int
    email: str
    morada: Morada

@dataclass
class PessoaC:

    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
