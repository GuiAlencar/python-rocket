# pip3 install requests==2.31.0
print('\nImportado modulo de terceiro')
import requests

url = "https://www.google.com"
responde = requests.get(url)
print(f"Solicitação HTTP para {url} retornou o status {responde.status_code}")