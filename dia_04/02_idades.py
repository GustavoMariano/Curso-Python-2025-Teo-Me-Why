# %%

idades = []

while True:
    idade = input("Entre com a idade: ")

    if idade == "":
        break

    idades.append(int(idade))

print(idades)

quantidade = len(idades)
media = sum(idades) / quantidade
minimo = min(idades)
maximo = max(idades)

print("Média:", media)
print("Mínimo:", minimo)
print("Máximo:", maximo)
print("Quantidade:", quantidade)
