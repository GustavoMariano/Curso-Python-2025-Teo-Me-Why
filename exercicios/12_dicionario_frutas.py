frutas = {
    "Maça":1.50, 
    "Banana":2.75,
    "Uva":1.90,
    "Pera":1.25,
    "Laranja":0.65,
    "Limão":1.25,
    "Goiaba":2.15,
    "Abacaxi":3.20,
    "Jaca":5.80,
    }

fruta = input("Digite o nome da fruta desejada: ")

if fruta in frutas:
    print("A", fruta ,"custa: R$", frutas[fruta])
else:
    print("Entre com um valor válido!")