import os
from dotenv import load_dotenv
from binance.client import Client

# Carrega as variáveis do arquivo .env
load_dotenv()

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

if not api_key or not api_secret:
    print("❌ Chaves não carregadas. Verifique o arquivo .env")
    exit()

# Conectar na Binance TESTNET
client = Client(api_key, api_secret)
client.API_URL = "https://testnet.binance.vision/api"

try:
    account = client.get_account()
    print("✅ Conectado à Binance TESTNET com sucesso!")
    print("Saldo disponível:")

    for asset in account["balances"]:
        if float(asset["free"]) > 0:
            print(asset["asset"], asset["free"])

except Exception as e:
    print("❌ Erro ao conectar:")
    print(e)
