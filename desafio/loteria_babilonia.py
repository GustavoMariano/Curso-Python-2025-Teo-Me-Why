import random

numeroSorteio = random.randint(1, 15)

def get_input():
    while True:
        try:
            numeroUsuario = int(input("Entre com um número: "))
        
        except ValueError as err:
            print("Valor inválido!")
            continue
        
        if 1 <= numeroUsuario <= 15:
            return numeroUsuario

        print("Valor inválido! O valor deve ser entre 1 e 15")

def check_numbers(sorteio, usuario):
    if usuario == sorteio:
        print("Parabéns, você acertou!")
        return True
    elif usuario > sorteio:
        print("Número muito alto. Tente um número menor!")
        return False
    elif usuario < sorteio:
        print("Número muito baixo. Tente um número maior!")
        return False

for i in range(3):
    numeroUsuario = get_input()

    if check_numbers(sorteio=numeroSorteio, usuario=numeroUsuario):
        break
    
else:
    print("Suas tentativas acabaram! O número era:", numeroSorteio)