import json

caminho_completo = "C:\\Users\\MICRO\\OneDrive\\Área de Trabalho\\WorkSpace Python Intermediario\\Context Manager JSON\\"
caminho_completo += "Arquivo_teste1.json"


usuario = {
    "Nome": "Juan Guilherme",
    "Sobrenome": "Silva Lemos",
    "Idade": 21,
    "Endereco": [
        {"Endereco_1": "Rua 84"},
        {"Endereco_2": "Rua 112"},
    ],
    "Desenvolvedor": True,
}


with open(caminho_completo, "w+") as arquivo:
    json.dump(
        usuario,
        arquivo,
        indent=2,
    )
