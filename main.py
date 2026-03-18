import os
import time
import requests

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

BASE_URL = "https://api.hyperliquid.xyz"

SYMBOL = "BTC"
DROP_PERCENT = 0.35   # compra após queda de 0.35%
RISE_PERCENT = 0.55   # vende após alta de 0.55%
USD_AMOUNT = 50       # valor por operação

last_price = None


def get_price():
    try:
        response = requests.get(f"{BASE_URL}/info")
        data = response
