import os
import math
from itertools import count


def formata_tamanho(tamanho_b: int, base: int = 1000):
    if tamanho_b <= 0:
        return "0B"

    abrevi_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"

    indice_abrevi_tamanho = int(math.log(tamanho_b, base))
    potencia = base**indice_abrevi_tamanho

    tamanho_real = tamanho_b / potencia
    abreviacao_tamanho = abrevi_tamanhos[indice_abrevi_tamanho]
    return f"{tamanho_real:.2f} {abreviacao_tamanho}"


# caminho_completo = r"C:\\Users\\User\\Desktop\\WorkSpace Intermediario\\SEÇÃO 4\\Os"

# contador = count()

# for root, dirs, files in os.walk(caminho_completo):
#     next_count = next(contador)
#     print(f"{ next_count} Roots:{root}")
#     for dir in dirs:
#         print(f" { next_count} Dirs:{dir}")
#     for file in files:
#         print(f"  { next_count} Files:{files}")
