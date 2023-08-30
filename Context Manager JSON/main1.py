import json
import pprint

caminho_completo = "C:\\Users\\MICRO\\OneDrive\\Área de Trabalho\\WorkSpace Python Intermediario\\Context Manager JSON\\"
caminho_completo += "Arquivo_teste1.json"


def p(obj):
    return pprint.pprint(obj)


usuario = {
    "Nome": "Juan Guilherme",
    "Sobrenome": "Silva Lemosss",
    "Idade": 21,
    "Endereco": [
        {"Endereco_1": "Rua 84"},
        {"Endereco_2": "Rua 112"},
    ],
    "Desenvolvedor": True,
}


with open(caminho_completo, "w+", encoding="utf8") as arquivo:
    json.dump(
        usuario,
        arquivo,
        indent=2,
    )

with open(caminho_completo, "r") as arquivo_2:
    pessoa = json.load(arquivo_2)
    p(pessoa)
