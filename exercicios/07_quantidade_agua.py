texto = """
Escolha a sua água para comprar
(1) Água mineral natural - R$ 1.50
(2) Água mineral com gás - R$ 2.50
"""

opcao = int(input(texto))

valorItem = 0
if(opcao == 1):
    valorItem = 1.5
elif(opcao == 2):
    valorItem = 2.5

if valorItem == 0:
    print("Sua conta é: R$", valorItem)
else:
    quantidade = int(input("Insira a quantidade de garrafas que deseja "))
    valorTotal = valorItem * quantidade
    print("Sua conta deu: R$", valorTotal)