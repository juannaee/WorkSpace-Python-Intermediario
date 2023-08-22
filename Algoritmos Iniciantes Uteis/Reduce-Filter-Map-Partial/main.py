import random
import pprint
from functools import reduce


MIN_PRECO = 50
MAX_PRECO = 5000


def imprimir(objeto):
    pprint.pprint(list(objeto), sort_dicts=False)


def gerar_produtos(quantidade):
    produtos = [f"produto {i}" for i in range(1, quantidade + 1)]
    return produtos


def gerar_precos_aleatorios(lista):
    for i, item in enumerate(lista):
        preco = round(random.uniform(MIN_PRECO, MAX_PRECO), 2)
        lista[i] = {"Nome": item, "Preco": preco}
    return lista


def filtrar_produtos_precos(produto, expressao, valor):
    if expressao == "<":
        return produto["Preco"] <= valor
    if expressao == ">":
        return produto["Preco"] >= valor


def adicionar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)


def funcao_reduce_valor_total(acumulador, produto):
    return acumulador + produto["Preco"]


# não to utilizando essa logica pois fica mais "complexo" o codigo porém compensa manter para lembrar.
# def mudar_preco_produtos(produtos):
#    return {**produtos, "Preco": aumentar_preco_produtos(produtos["Preco"])}


quantidade_de_produtos = 3
produtos = gerar_produtos(quantidade_de_produtos)
lista_produtos = gerar_precos_aleatorios(produtos)
imprimir(lista_produtos)

print("================================================================")
print("## Filtrando Precos ##")

valor_limite = 1000
lista_produtos_precos_filtrados = filter(
    lambda produto: filtrar_produtos_precos(produto, "<", valor_limite), lista_produtos
)
imprimir(lista_produtos_precos_filtrados)


print("================================================================")
print("## Aumentando 10'%' aos valores ##")

# aumentar_preco_produtos = partial(adicionar_porcentagem, porcentagem_aumento)
# lista_produtos_precos_atualizados = map(mudar_preco_produtos, lista_produtos)
# imprimir(lista_produtos_precos_atualizados)

porcentagem_aumento = 1.1
lista_produtos_precos_atualizados = [
    {**produto, "Preco": adicionar_porcentagem(produto["Preco"], porcentagem_aumento)}
    for produto in lista_produtos
]
imprimir(lista_produtos_precos_atualizados)

print("================================================================")
print("## Preco total ##")
preco_total = reduce(funcao_reduce_valor_total, lista_produtos, 0)
print(round(preco_total, 2))
