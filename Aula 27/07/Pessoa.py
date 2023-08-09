from dataclasses import dataclass

@dataclass
class Pessoa:
    id: int
    nome: str
    idade: int
    filho: list ['Pessoa']
    email: str = "sem email"


    def __init__(self, id,:int nome:str, idade:int, email:str = "sem email"):

    def __eq__(self, rhs):
        return self.id == rhs.id

    def __le__(self, other): ##<=
        pass

    def __lt__(self, other): # <
        pass

    def __gt__(self, other): # >=
        pass

    def __ge__(self, other): # >=
        pass

    def __add__(self, other): # +
        novoid = self.id + other.id
        filho = Pessoa(novoid, "sem nome", 0)

        self.filhos.append (filho)
        other.filhos.append (filho)

        return filho

@dataclass
class Ponto:...

@dataclass
class cao:
    id: int
    nome: str

    def __eq__(lhs, rhs):
        return lhs.id != rhs.id
