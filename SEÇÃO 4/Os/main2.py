import os
from itertools import count

caminho_completo = r"C:\\Users\\User\\Desktop\\WorkSpace Intermediario\\SEÇÃO 4\\Os"

contador = count()

for root, dirs, files in os.walk(caminho_completo):
    next_count = next(contador)
    print(f"{ next_count} Roots:{root}")
    for dir in dirs:
        print(f" { next_count} Dirs:{dir}")
    for file in files:
        print(f"  { next_count} Files:{files}")
