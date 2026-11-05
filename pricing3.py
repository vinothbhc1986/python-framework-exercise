import httpx

API = "https://api.exhangerate.host/latest"

def eur_to_usd(amount):
    response = httpx.get(API, params={"base": "EUR"})
    rate = response.json()["rates"]["USD"]
    return round(amount * rate, 2)