# %%

def juros_compostos(aporte:int, taxa:float, anos:int)->float:
    """juros_compostos serve para calcular o retorno financeiro de um aporte.
    Deve-se considerar o valor, a taxa de juros atual e o tempo (em anos) para calcular o valor do retorno do investimento.
    
    aporte:
    Um número inteiro, que represente o valor em R$.

    taxa:
    Um número float entre 0 e 1 que represente o valor da taxa de juros.

    anos:
    Um número inteiro >= 1 que represente o tempo que o investimento terá liquidez.
    """
    return aporte * (1 + taxa) ** anos

# %%
juros_compostos(aporte=1000, taxa=0.8, anos=5)

#print(resultado)