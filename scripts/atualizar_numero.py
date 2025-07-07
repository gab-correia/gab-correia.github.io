# atualizar_numero.py
import re

arquivo = "_data/contador.md"

with open(arquivo, "r") as f:
    conteudo = f.read()

match = re.search(r"(\d+)", conteudo)
numero = int(match.group(1)) if match else 0
novo_numero = numero + 1

with open(arquivo, "w") as f:
    f.write(f"Último número: {novo_numero}\n")

print(f"Atualizado para: {novo_numero}")
