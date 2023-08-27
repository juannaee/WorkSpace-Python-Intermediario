caminho_completo = "C:\\Users\\MICRO\\OneDrive\\Área de Trabalho\\WorkSpace Python Intermediario\\Context Manager\\"
caminho_completo += "Arquivo_teste2.txt"


with open(caminho_completo, "a+") as arquivo:
    arquivo.write("\n")
    print("Fechando arquivo...")
