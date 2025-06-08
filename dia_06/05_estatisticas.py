# %%
def soma(valores:list)->float:
    return sum(valores)

def media(valores:list)->float:
    return soma(valores=valores) / len(valores)

valores = []
while (True):
    valor = input("Entre com um valor: ")

    if valor == "":
        break

    valores.append(float(valor))

print("Média:", media(valores))

# %%

def somaArgs(a:float, b:float, *args)->float:
    valores = [a, b] + list(args)
    return sum(valores)

def mediaArgs(a:float, b:float, *args)->float:
    valores = [a, b] + list(args)
    return somaArgs(a, b, *args) / len(valores)

a = int(input("Entre com o valor A: "))
b = int(input("Entre com o valor B: "))
c = int(input("Entre com o valor C: "))

print("Média:", mediaArgs(a, b, c))