# %%
nomeArquivo = "historia.txt"

openFile = open(nomeArquivo)

conteudo = openFile.read()
print(conteudo)

openFile.close()

# %%

with open(nomeArquivo) as openFile:
    conteudo = openFile.read()

print(conteudo)