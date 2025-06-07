# %%
lista = [1, 2, 3, "ABC", ['A', 'B', 'C']]

# %%
dados = {
    "nome":"Gustavo", 
    "sobrenome":"Mariano",
    "idade":25,
    "formacao":[
        {"instituicao":"Universidade do Planalto Catarinense", "nivel":"Bacharel", "curso":"Sistemas de Informação"},
        {"instituicao":"Pontifícia Universidade Católica de Minas Gerais", "nivel":"Pós Graduação", "curso":"Engenharia de Software"}
    ],
    "cargos":[
        {"cargo":"Desenvolvedor Trainee.", "empresa":"NDD Tech"},
        {"cargo":"Desenvolvedor Jr.", "empresa":"NDD Tech"},
        {"cargo":"Desenvolvedor Pl.", "empresa":"Kinvo"},
        {"cargo":"Desenvolvedor Pl.", "empresa":"Capgemini"},
        {"cargo":"Desenvolvedor Sr.", "empresa":"Questor Sistemas"}
    ]
}

print(dados)

# %%
print(dados["formacao"][-1])

# %%
print(dados["cargos"][-1]["cargo"])

# %% 
dados["cidade"] = "Lages"

print(dados)

# %%
print(dados.keys())
print(dados.values())
print(dados.items())

# %%
for i in dados:
    print(i)

# %%
for i in dados:
    print(i, "->", dados[i])

# %%
for chave, valor in dados.items():
    print(chave, "->", valor)