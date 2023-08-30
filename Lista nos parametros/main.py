import pprint


def p(obj):
    return pprint.pprint(obj)


def gerador_listas(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente_1 = gerador_listas("Juan")
gerador_listas("Bianca", cliente_1)
p(cliente_1)

cliente_2 = []
gerador_listas("dasd", cliente_2)
gerador_listas("Biancsdfsdfa", cliente_2)
p(cliente_2)
