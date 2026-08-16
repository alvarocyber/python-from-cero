from bs4 import BeautifulSoup
import requests

url = 'https://www.apple.com/es/shop/buy-mac/macbook-air/13-pulgadas-medianoche-chip-m5-cpu-de-10-núcleos-gpu-de-8-núcleos-16-gb-de-memoria-512gb-de-capacidad'

response = requests.get(url)

if response.status_code == 200:
    print("La peticion fue exitosa")

    soup = BeautifulSoup(response.text, 'html.parser')

    tittle_tag = soup.tittle
    if tittle_tag:
        print(f"El tituilo de la web es: {tittle_tag.text}")

    metas = soup.title.parent.find_all('meta')
    print(metas)

    price_span = soup.find('span', class_= 'rc-prices-fullprice')
    if price_span:
        print(f"El precio del producto es {price_span}")