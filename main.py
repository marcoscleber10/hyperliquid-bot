import time
import requests

SYMBOL = "BTC"
BASE_URL = "https://api.hyperliquid.xyz/info"

def get_price():
    try:
        response = requests.post(BASE_URL, json={"type": "meta"})
        data = response.json()

        response2 = requests.post(BASE_URL, json={"type": "allMids"})
        mids = response2.json()

        if SYMBOL in mids:
            return float(mids[SYMBOL])
    except Exception as e:
        print("Erro ao buscar preço:", e)

    return None


while True:
    price = get_price()

    if price:
        print("Preço atual:", price)
    else:
        print("Não conseguiu pegar preço")

    time.sleep(10)
