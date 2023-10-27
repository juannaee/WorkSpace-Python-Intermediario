IDADE_MAX = 70
IDADE_MIN = 18


while True:
    nome = input("Digite seu Nome: ")
    idade = input("Digite sua idade: ")
    nome = nome.strip()
    # if not nome or len(nome) < 3 or any(letra.isdigit() for letra in nome):
    if not nome or len(nome) < 3 or not nome.isalpha():
        print("Você deve digitar um nome valido")
    try:
        idade = int(idade)
        if idade < IDADE_MIN or idade > IDADE_MAX:
            print(
                f"Sua idade é incompativel com o sistema!!! a idade deve ser entre {IDADE_MIN} a {IDADE_MAX} Anos"
            )

    except ValueError:
        print("Você deve digitar um valor numerico para campo idade!!")
    except Exception as e:
        print(f"Error:{e}")

    print(f"Bem vindo ao sistema segue seus dados\nNome: {nome}\nIdade: {idade}")
    break
