numeros = [1, 2, 3, 3, 2, 1, 1, 1, 1, 1, 5, 6, 7, 7, 6, 5]

numero = int(input("Entre com um número "))

count = 0
for num in numeros:
    if(num == numero):
        count += 1

print("Na lista existem", count, "número", numero)

