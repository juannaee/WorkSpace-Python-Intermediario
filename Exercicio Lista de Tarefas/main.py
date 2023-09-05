import pprint
import os
import json

# Caminho completo para o arquivo JSON onde os dados serão armazenados
# Lembra de mudar o caminho de acordo com a maquina onde será executado

# CASA #
# caminho_completo = "C:\\Users\\MICRO\\OneDrive\\Área de Trabalho\\WorkSpace Python Intermediario\\Exercicio Lista de Tarefas\\"
# caminho_completo += "lista.json"

# TRABALHO #
caminho_completo = (
    "C:\\Users\\User\\Desktop\\WorkSpace Intermediario\\Exercicio Lista de Tarefas\\"
)
caminho_completo += "lista.json"


def printer(obj):
    """
    Função para imprimir um objeto formatado usando a biblioteca pprint.

    Args:
        obj : O objeto a ser impresso.

    Returns:
        None
    """
    pprint.pprint(f"{obj} Quantidade de Itens: {len(obj)}")


def adicionar_produto(produto, lista_produtos):
    """
    Função para adicionar um produto à lista de produtos.

    Args:
        produto (str): O produto a ser adicionado.
        lista_produtos (list): A lista de produtos à qual o produto será adicionado.

    Returns:
        None
    """
    print()
    # Fiz esse if para poder controlar a entrada de inteiros ou strings
    if produto == str(produto):
        produto = produto.strip()
    # Verificando se o usuario escreveu algo
    if not produto:
        print("Você não digitou nada!")
        return
    lista_produtos.append(produto)


def listar_produtos(lista_produtos):
    """
    Função para listar os produtos da lista.......

    Args:
        lista_produtos (list): A lista de produtos a ser listada.

    Returns:
        None
    """
    print()
    if not lista_produtos:
        print("Lista vazia.....")
        return
    print("Lista de produtos:")
    printer(lista_produtos)


def desfazer_mudanca_lista(lista_produtos, lista_de_controle):
    """
    Função para desfazer a última mudança na lista de produtos.

    Args:
        lista_produtos (list): A lista de produtos da qual a mudança será desfeita.
        lista_de_controle (list): A lista de controle onde os itens removidos serão armazenados.

    Returns:
        None
    """
    print()
    if not lista_produtos:
        print("Lista vazia, nada para desfazer.....")
        return
    produto = lista_produtos.pop()
    lista_de_controle.append(produto)


def refazer_mudanca_lista(lista_produtos, lista_de_controle):
    """
    Função para refazer a última mudança na lista de produtos.

    Args:
        lista_produtos (list): A lista de produtos na qual a mudança será refeita.
        lista_de_controle (list): A lista de controle onde os itens a serem refeitos estão armazenados.

    Returns:
        None
    """
    print()
    if not lista_de_controle:
        print("Lista vazia, nada para refazer.....")
        return
    produto = lista_de_controle.pop()
    lista_produtos.append(produto)


def main():
    """
    Função principal para controle da execução do programa.

    Returns:
        None
    """
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
            print("Por favor, digite um valor numérico válido.")
            continue

        except Exception as error:
            print(f"Ocorreu um erro: {error}")

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
            print("Saindo.....")
            break

        else:
            print("Opção inválida. Escolha uma das opções listadas.")
            continue


def carregar_arquivo():
    """
    Função para carregar dados do arquivo JSON, se existir.

    Returns:
        list: A lista de produtos carregada do arquivo ou uma lista vazia se o arquivo não existir.
    """
    if os.path.exists(caminho_completo):
        try:
            with open(caminho_completo, "r", encoding="utf8") as arquivo:
                return json.load(arquivo)
        except (json.JSONDecodeError, FileNotFoundError):
            pass
    return []


def salvar_arquivo(lista_produtos):
    """
    Função para salvar a lista de produtos em um arquivo JSON.

    Args:
        lista_produtos (list): A lista de produtos a ser salva.

    Returns:
        None
    """
    with open(caminho_completo, "w", encoding="utf8") as arquivo:
        json.dump(lista_produtos, arquivo, indent=2)


def limpar_terminal():
    """
    Função para limpar o terminal com base no sistema operacional.

    Returns:
        None
    """
    sistema_operacional = os.name
    if sistema_operacional == "posix":
        os.system("clear")
    elif sistema_operacional == "nt":
        os.system("cls")
    else:
        print("Não foi possível limpar o terminal.")


if __name__ == "__main__":
    main()
