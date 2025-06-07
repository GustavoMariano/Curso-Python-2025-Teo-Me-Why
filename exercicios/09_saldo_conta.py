saldoTotal = 0

valor = 0
while True:
    saldo = input("Entre com o saldo: ")
    if(saldo == ""):
        break
    saldoTotal += float(saldo)

print(saldoTotal)