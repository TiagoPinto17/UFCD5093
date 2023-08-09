from Pessoa import Pessoa

p1 = Pessoa(2, "ana", 10 [])
p2 = Pessoa(4, "marta", 10,[], "email@sapo.pt")
print("--" * 10)
print(p1)
print(p2)
print("--" * 10)

f = p1 + p2

f.nome = "João"

print("--" * 10)
print(p1.filho)
print(p2.filho)
print("--" * 10)

p3 = Pessoa(8, "ana", 10)
p4 = Pessoa(16, "João", 10, "email@sapo.pt")

f2 = p3 + p4
print("--" * 10)

