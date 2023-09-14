import json

CAMINHO_COMPLETO = "C:\\Users\\MICRO\\OneDrive\\Área de Trabalho\\WorkSpace Python Intermediario\\Orientação_a_Objetos\\Exercicios\\Salvando_dados_da_classe_em_JSON\\"
CAMINHO_COMPLETO += "Arquivo_1.json"


class Pessoa:
    def __init__(self, nome):
        self.nome = nome


p1 = Pessoa("Juan")
p2 = Pessoa("Bianca")
p3 = Pessoa("Alana")

lista_de_pessoas = [vars(p1), vars(p2), vars(p3)]


def escrever_arquivo():
    with open(CAMINHO_COMPLETO, "w", encoding="utf-8") as arquivo:
        json.dump(lista_de_pessoas, arquivo, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    print("Fazendo arquivo.............")
    escrever_arquivo()
