import requests

class Moneda:
    def __init__(self,nombre,casa,compra,venta,moneda,fecha_actualizacion): #__init__ es el constructor, es un metodo
        self.nombre=nombre
        self.casa=casa
        self.compra=compra
        self.moneda=moneda
        self.venta=venta
        self.fecha_actualizacion=fecha_actualizacion
    
    def mostrar_info(self):
        return {
            "moneda": self.moneda,
            "casa": self.casa,
            "nombre": self.nombre,
            "compra": self.compra,
            "venta": self.venta,
            "fecha_actualizacion": self.fecha_actualizacion    
        }    

class Dolar(Tipo):
    @staticmethod
    def obtener_datos():
        api_url = "https://dolarapi.com/v1/dolares"  # La URL de la API
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            dolares = []
            for item in data:
                # Creamos una instancia de Dolar para cada tipo de cotización
                dolar = Dolar(nombre_moneda=item["moneda"], tipo=item["nombre"])
                
                # Agregamos la cotización correspondiente
                dolar.cargar_cotizacion(Cotizacion(
                    actualizacion=item["fechaActualizacion"],
                    valor_compra=item["compra"],
                    valor_venta=item["venta"]
                ))
                dolares.append(dolar)
            return dolares
        else:
            raise Exception(f"Error al obtener datos: {response.status_code}")
        
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