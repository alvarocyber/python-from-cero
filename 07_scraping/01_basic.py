import requests
import re

url = 'https://www.apple.com/es/shop/buy-mac/macbook-air/13-pulgadas-medianoche-chip-m5-cpu-de-10-núcleos-gpu-de-8-núcleos-16-gb-de-memoria-512gb-de-capacidad'

response = requests.get(url)

if response.status_code == 200:
    print("La peticion fue exitosa")

    html = response.text
    price_pattern = r'<div class="typography-eyebrow" data-autom="summaryHeroPrice">1.429,00&nbsp;€</div>'
    match = re.search(price_pattern,html)

    if match:
        print(f"El precio del producto es {match.group(1)}")