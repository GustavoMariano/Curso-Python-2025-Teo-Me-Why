# %%

nome = "Gustavo Mariano"

for letra in nome:
    print(letra)


# %%

maxNumero = 10

for i in range(1, maxNumero + 1):
    for c in range(1, maxNumero + 1):
        print(i, "x", c, "=", i * c)
    print("")

# %%

maxNumero = 100

for i in range(4, maxNumero + 1):
    if(i % 4 == 0):
        print("O número", i, "é divisível por 4")