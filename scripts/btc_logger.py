# btc_logger.py
import requests
import pandas as pd
from datetime import datetime
import os

CSV_PATH = "files/precos_btc.csv"  # salvar dentro da pasta `files/` para acesso web

def obter_preco_atual():
    url = "https://api.coinbase.com/v2/prices/spot?currency=USD"
    response = requests.get(url)
    data = response.json()
    valor = float(data["data"]["amount"])
    return datetime.now(), valor

# Cria pasta files se não existir
os.makedirs("files", exist_ok=True)

# Salva no CSV
agora, preco = obter_preco_atual()

try:
    historico = pd.read_csv(CSV_PATH, parse_dates=['timestamp'])
except FileNotFoundError:
    historico = pd.DataFrame(columns=["timestamp", "preco"])

novo_dado = pd.DataFrame([{"timestamp": agora, "preco": preco}])
historico = pd.concat([historico, novo_dado]).drop_duplicates(subset=["timestamp"])

historico.to_csv(CSV_PATH, index=False)
print(f"[{agora}] Preço salvo: ${preco}")
