import requests

# waluta_z
# waluta_na
# kwote
def przelicz(kwote: float, waluta_z:str, waluta_na:str) -> float:
    url = f"https://v6.exchangerate-api.com/v6/563075f9e11695fd9ef35c70/latest/{waluta_z}"
    respones = requests.get(url)
    lista_walut = respones.json()['conversion_rates']
    wynik = kwote * lista_walut[waluta_na]
    return wynik


print(przelicz(100,'USD','PLN'))

