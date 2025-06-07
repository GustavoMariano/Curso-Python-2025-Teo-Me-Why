idade = int(input("Digite a sua idade para verificar se pode beber bebida alcólica "))

if idade >= 18 and idade <= 70:
    print("Pode beber!")
    print("Beba com moderação")
elif idade > 70:
    print("Cuidado com a bebida alcólica")
    print("Consulte o seu médico")
else:
    print("Não pode beber")
    print("Vá para casa beber água")