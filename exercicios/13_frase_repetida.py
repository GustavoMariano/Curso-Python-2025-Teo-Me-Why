# %%

dados = {}

while True:
    frase = input("Entre com uma frase: ")

    if frase == "":
        break

    if frase not in dados:
        dados[frase] = 1
    else:
        dados[frase] += 1

for i, j in dados.items():
    print("A frase:", i, "apareceu", j, "vezes")


# %%

dados = {
    "oi": 1,
    "olá": 10,
    "oi tudo bem": 3,
    "test": 2,
    "teste": 5
}

items = list(dados.items())
items.sort(key=lambda x: x[-1], reverse=True)

for i, j in items:
    print(i, "->", j)