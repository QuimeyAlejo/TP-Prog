import requests

class Moneda:
    def __init__(self,nombre,casa,compra,venta,moneda,fecha_actualizacion): #__init__ es el constructor, es un metodo
        self.nombre=nombre
        self.casa=casa
        self.compra=compra
        self.moneda=moneda
        self.venta=venta
        self.fecha_actualizacion=fecha_actualizacion

class Dolar(Moneda):
    def __init__(self, nombre, casa, compra, venta, moneda, fecha_actualizacion):
        super().__init__(nombre, casa, compra, venta, moneda, fecha_actualizacion)

    @staticmethod
    def obtener_datos():
        api_url = "https://dolarapi.com/v1/dolares"
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
          #  print("Get Dolar",data)
            return [
                Dolar(
                    nombre=item['nombre'],
                    casa=item['casa'],
                    compra=item['compra'],
                    venta=item['venta'],
                    moneda=item['moneda'],
                    fecha_actualizacion=item['fechaActualizacion'],
                )
                for item in data
            ]
        else:
            raise Exception(f"Error al obtener datos de Dólar: {response.status_code}")

    def mostrar_info(self):
        return {
            "moneda":self.moneda,
            "casa":self.casa,
            "nombre":self.nombre,
            "compra":self.compra,
            "venta":self.venta,
            "fecha_actualizacion":self.fecha_actualizacion    
        }    
        
class Cotizacion(Moneda):
    def __init__(self, nombre, casa, compra, venta, moneda, fecha_actualizacion):
        super().__init__(nombre, casa, compra, venta, moneda, fecha_actualizacion)

    @staticmethod
    def obtener_datos():
        api_url = "https://dolarapi.com/v1/cotizaciones"
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            return [
                Dolar(
                    nombre=item['nombre'],
                    casa=item['casa'],
                    compra=item['compra'],
                    venta=item['venta'],
                    moneda=item['moneda'],
                    fecha_actualizacion=item['fechaActualizacion'],
                )
                for item in data
            ]
        else:
            raise Exception(f"Error al obtener datos de las cotizaciones: {response.status_code}")

    def mostrar_info(self):
        return {
            "moneda":self.moneda,
            "casa":self.casa,
            "nombre":self.nombre,
            "compra":self.compra,
            "venta":self.venta,
            "fecha_actualizacion":self.fecha_actualizacion    
        }    