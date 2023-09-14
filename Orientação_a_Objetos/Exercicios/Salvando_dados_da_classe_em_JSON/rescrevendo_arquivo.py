import json
import pprint


def printer(obj):
    pprint.pprint(obj)


from criando_arquivo import CAMINHO_COMPLETO, Pessoa, escrever_arquivo

escrever_arquivo()

with open(CAMINHO_COMPLETO, "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
    p1 = Pessoa(**dados[0])
    p2 = Pessoa(**dados[1])
    p3 = Pessoa(**dados[2])

p1.nome = "Outro nome"

printer(p1.nome)
printer(p2.nome)
printer(p3.nome)
