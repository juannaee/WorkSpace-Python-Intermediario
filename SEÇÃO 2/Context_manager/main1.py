caminho_completo = "C:\\Users\\MICRO\\OneDrive\\Área de Trabalho\\WorkSpace Python Intermediario\\Context Manager\\"
caminho_completo += "Arquivo_teste1.txt"


with open(caminho_completo, "w+", encoding="utf8") as arquivo:
    arquivo.write("ATENÇÃO\n")
    arquivo.write("linha_1\n")
    arquivo.write("linha_2\n")
    arquivo.writelines(("linha_3\n", "linha_4\n", "linha_5\n", "linha_6\n"))
    arquivo.seek(0, 0)
    print(arquivo.read())
    arquivo.seek(0, 0)
    print("ReadLine")
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print("#" * 20)
    print("ReadLines")
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())
    print("Arquivo fechado......")
