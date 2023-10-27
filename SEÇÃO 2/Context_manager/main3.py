import os

caminho_completo = "C:\\Users\\MICRO\\OneDrive\\Área de Trabalho\\WorkSpace Python Intermediario\\Context Manager\\"
caminho_completo += "Arquivo_teste3.txt"


with open(caminho_completo, "w+") as arquivo:
    arquivo.writelines(
        (
            "Linha_1\n",
            "Linha_2\n",
            "Linha_3\n",
            "Linha_4\n",
            "Linha_5\n",
            "Linha_6\n",
            "Linha_7\n",
            "Linha_8\n",
            "Linha_9\n",
            "Linha_10\n",
        )
    )
    arquivo.seek(0, 0)
    print(arquivo.read().strip())

# os.remove(caminho_completo)
