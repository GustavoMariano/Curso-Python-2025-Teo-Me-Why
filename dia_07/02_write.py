# %%

txt = "Meu novo arquivo de texto\n"

nomeArquivo = "historia_02.txt"

with open(nomeArquivo, mode="+a") as openFile:
    openFile.write(txt)
