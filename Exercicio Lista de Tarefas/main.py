import pprint
import os
import json


caminho_completo = (
    "C:\\Users\\User\\Desktop\\WorkSpace Intermediario\\Exercicio Lista de Tarefas\\"
)
caminho_completo += "lista.json"


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


def main():
    lista_produtos = carregar_arquivo()
    lista_de_controle = []
    while True:
        print("--------------------------------")
        print("Escolha uma opção")
        print("1 - Lista Produtos")
        print("2 - Desfazer")
        print("3 - Refazer")
        print("4 - Adicionar Produtos")
        print("5 - Limpar terminal")
        print("6 - Salvar")
        print("7 - Sair")
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
            limpar_terminal()
            continue

        elif opcao_menu == 6:
            print("Salvando...........")
            salvar_arquivo(lista_produtos)
            continue
        elif opcao_menu == 7:
            print("saindo.....")
            break

        else:
            print("Opção inválida. Escolha uma das opções listadas.")
            continue


def carregar_arquivo():
    if os.path.exists(caminho_completo):
        try:
            with open(caminho_completo, "r", encoding="utf8") as arquivo:
                return json.load(arquivo)
        except (json.JSONDecodeError, FileNotFoundError):
            pass
    return []


def salvar_arquivo(lista_produtos):
    with open(caminho_completo, "w", encoding="utf8") as arquivo:
        json.dump(lista_produtos, arquivo, indent=2)


def limpar_terminal():
    sistema_operacional = os.name
    if sistema_operacional == "posix":
        os.system("clear")
    elif sistema_operacional == "nt":
        os.system("cls")
    else:
        print("Não foi possível limpar o terminal.")


if __name__ == "__main__":
    main()
