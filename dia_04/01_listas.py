# %% 

idades = [28, 42, 43, 35, 39, 28, 38]
print(idades)

# %%

gustavo = ["Gustavo", "Mariano", 25, 1.73]

print(gustavo)

for item in gustavo:
    print(item)


# %%
type(gustavo)

# %%

print(gustavo[1])

# %%

print("Soma das idades:", sum(idades))

print("Quantidade de idades:", len(idades))

print("Média das idades:", sum(idades) / len(idades))

print("Menor idade:", min(idades))

print("Maior idade:", max(idades))

# %%

gustavo = ["Gustavo", 
           25, 
           "M", 
           "Grêmio",
           ["Estagiário", "Dev Trainee", "Dev Jr.", "Dev Pl.", "Dev Sr."],
           ["NDD Tech", "Kinvo", "Capgemini", "Questor Sistemas"]]

print(gustavo)

gustavo.remove(gustavo[4])

print(gustavo)

# %%

gustavo = ["Gustavo", 
           25, 
           "M", 
           "Grêmio",
           ["Estagiário", "Dev Trainee", "Dev Jr.", "Dev Pl.", "Dev Sr."],
           ["NDD Tech", "Kinvo", "Capgemini", "Questor Sistemas"]]

print(gustavo[-1])

# %%

gustavo[0:4]

# %%

gustavo[4][-2:]

# %%

cargos = gustavo[4]

# cargos[ start : stop : step]
cargos[::-1]