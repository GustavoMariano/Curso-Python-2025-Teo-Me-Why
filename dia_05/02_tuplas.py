# %% List
dados = ["Gustavo", 25, "Brasil"]

# %% Tuple
tupla1 = "Gustavo", 25, "Brasil"
tupla2 = ("Gustavo", 25, "Brasil")

print("Tipo Tupla 1", type(tupla1))
print(tupla1)

print("Tipo Tupla 2", type(tupla2))
print(tupla2)

# %% 

tuplaComLista = ("Gustavo", 25, ["item 1", "item 2"])
print(tuplaComLista)

tuplaComLista[-1].append("Item 3")
print(tuplaComLista)