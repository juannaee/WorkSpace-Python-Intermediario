import os


caminho_teste = os.path.join("teste\sub_teste", "arquivo_teste.txt")
print(caminho_teste)

diretorio, arquivo = os.path.split(caminho_teste)
print(diretorio)


caminho_teste, extensao_arquivo = os.path.splitext(caminho_teste)
print(extensao_arquivo)
