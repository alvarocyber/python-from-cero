# 1. Introduccion a las clases en Python
# Las clases son plantillas para crear objetos. Un objeto es una instancia de una clase
# Nos permite agrupar datos y funciones en solo un lugar

#Ejemplo basico
import requests

class Coche:
    tipo = "vehiculo de 4 ruedas"

    #metodo especial que es el constructor del objeto
    #se llama automaticamente cuando creamos un objeto
    def __init__(self, marca,modelo,color) -> None:
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def arrancar(self):
        """Muestra si el coche arranca o no"""
        print(f"El coche {self.marca} {self.modelo} de color {self.color} arranco")

    def info(self):
        print(self.marca,self.modelo,self.color)

mi_coche = Coche("Nissan","Primera","Gris")

mi_coche.arrancar()
mi_coche.info()
print(mi_coche.marca)

class Moto (Coche):
    tipo = "Esto es un vehiculo de 2 ruedas"

    def arrancar(self):
        print(f"La moto de marca {self.marca} y modelo {self.modelo}, ha sido arrancada")

mi_moto = Moto("Yamaha","R7","negra")
mi_moto.arrancar()
mi_moto.info()

# Encapsulacion: es ocultar los detalles internos de una clase y exponer solo la interfaz publica

# Crear una clase para llamar a la AI de Open AI o Deepseek

class API:
    def __init__(self, api_key,url,model) -> None:
        self.api_key = api_key
        self.url = url
        self.model = model

    def call_AI(self,prompt):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        data = {
            "model":self.model,
            "mesagges":[{"role": "user","content":prompt}]  
        }
        
        response = requests.post(self.url,json=data,headers=headers)
        res_json = response.json()
        print(res_json["choices"][0]["message"]["content"])

    
key = "sk-479a5c6ce18646df98550f7fafb35c4a"
ia = API(key,"https://api.deepseek/chat/completions", "deepseek-chat")

ia.call_AI("Dame un poema breve sobre computacion")
