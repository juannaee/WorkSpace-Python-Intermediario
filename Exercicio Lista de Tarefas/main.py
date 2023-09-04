import pprint
import os


def printer(obj):
    pprint.pprint(f"{obj} Quantidade de Itens: {len(obj)}")


def adicionar_produto(produto, lista_produtos):
    print()
    if produto == str(produto):
        produto = produto.strip()
    if not produto:
        print("Você não digitou nada!")
        return
    lista_produtos.append(produto)


def listar_produtos(lista_produtos):
    print()
    if not lista_produtos:
        print("Lista vazia.....")
        return
    print("Lista de produtos:")
    printer(lista_produtos)


def desfazer_mudanca_lista(lista_produtos, lista_de_controle):
    print()
    if not lista_produtos:
        print("Lista vazia nada para desfazer.....")
        return
    produto = lista_produtos.pop()
    lista_de_controle.append(produto)


def refazer_mudanca_lista(lista_produtos, lista_de_controle):
    print()
    if not lista_de_controle:
        print("Lista vazia nada para refazer.....")
        return
    produto = lista_de_controle.pop()
    lista_produtos.append(produto)


lista_produtos = []
lista_de_controle = []

while True:
    print("--------------------------------")
    print("Escolha uma opção")
    print("1 - Lista Produtos")
    print("2 - Desfazer")
    print("3 - Refazer")
    print("4 - Adicionar Produtos")
    print("5 - Limpar terminal")
    print("6 - Sair")
    print("--------------------------------")

    try:
        opcao_menu = int(input("Opção Digitada: "))

    except ValueError:
        print("Por favor, digite um valor númerico válido.")
        continue

    except Exception as error:
        print(f"Ocorreu um error: {error}")

    if opcao_menu == 1:
        listar_produtos(lista_produtos)
        continue

    elif opcao_menu == 2:
        desfazer_mudanca_lista(lista_produtos, lista_de_controle)
        listar_produtos(lista_produtos)
        continue

    elif opcao_menu == 3:
        refazer_mudanca_lista(lista_produtos, lista_de_controle)
        listar_produtos(lista_produtos)
        continue

    elif opcao_menu == 4:
        produto = input("Digite um produto: ")
        adicionar_produto(produto, lista_produtos)
        listar_produtos(lista_produtos)
        continue

    elif opcao_menu == 5:
        os.system("cls")
        print("Terminal limpo")
        continue

    elif opcao_menu == 6:
        print("Sair...........")
        break
    else:
        print("Opção inválida. Escolha uma das opções listadas.")
        continue
