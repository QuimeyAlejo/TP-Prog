from abc import ABC, abstractmethod
from datetime import datetime
import requests

class Moneda(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def cargar_nombre(self, nombre):
        pass
    
    @abstractmethod
    def mostrar_nombre(self):
        pass


class MonedaConcreta(Moneda):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.tipo_casas = []  # Definimos tipo_casas para almacenar diferentes tipos de cotizaciones

    def cargar_nombre(self, nombre):
        self.nombre = nombre
    
    def mostrar_nombre(self):
        return self.nombre


class Cotizacion(ABC):
    def __init__(self, fecha_actualizacion, valor_compra, valor_venta):
        self.fecha_actualizacion = fecha_actualizacion
        self.valor_compra = valor_compra
        self.valor_venta = valor_venta

    @abstractmethod
    def cargar_actualizacion(self, fecha):
        pass
    
    @abstractmethod
    def cargar_compra(self, valor_compra):
        pass
    
    @abstractmethod
    def cargar_venta(self, valor_venta):
        pass
    
    @abstractmethod
    def mostrar_actualizacion(self):
        pass
    
    @abstractmethod
    def mostrar_compra(self):
        pass
    
    @abstractmethod
    def mostrar_venta(self):
        pass


class CotizacionConcreta(Cotizacion):
    def cargar_actualizacion(self, fecha):
        self.fecha_actualizacion = fecha
    
    def cargar_compra(self, valor_compra):
        self.valor_compra = valor_compra
    
    def cargar_venta(self, valor_venta):
        self.valor_venta = valor_venta
    
    def mostrar_actualizacion(self):
        return self.fecha_actualizacion
    
    def mostrar_compra(self):
        return self.valor_compra
    
    def mostrar_venta(self):
        return self.valor_venta


class Tipo(ABC):
    def __init__(self, nombre_tipo):
        self.nombre_tipo = nombre_tipo
        self.cotizaciones = []
    
    @abstractmethod
    def cargar_nombre_tipo(self, nombre_tipo):
        pass
    
    @abstractmethod
    def mostrar_nombre_tipo(self):
        pass
    
    @abstractmethod
    def cargar_cotizaciones(self, cotizacion):
        pass
    
    @abstractmethod
    def mostrar_cotizaciones(self):
        pass


class TipoConcreto(Tipo):
    def cargar_nombre_tipo(self, nombre_tipo):
        self.nombre_tipo = nombre_tipo
    
    def mostrar_nombre_tipo(self):
        return self.nombre_tipo
    
    def cargar_cotizaciones(self, cotizacion):
        self.cotizaciones.append(cotizacion)
    
    def mostrar_cotizaciones(self):
        return self.cotizaciones


# Funciones para obtener datos desde la API y crear instancias

def obtener_datos_api_dolar():
    url = "https://dolarapi.com/v1/dolares"
    response = requests.get(url)
    datos = response.json()
    return datos

def obtener_datos_api_cotizaciones():
    url = "https://dolarapi.com/v1/cotizaciones"
    response = requests.get(url)
    datos = response.json()
    return datos

def crear_instancias_dolar_desde_api():
    datos = obtener_datos_api_dolar()
    monedas = {}

    for dato in datos:
        nombre_moneda = dato["moneda"]
        nombre_tipo = dato["nombre"]
        valor_compra = dato["compra"]
        valor_venta = dato["venta"]
        fecha_actualizacion = datetime.fromisoformat(dato["fechaActualizacion"].replace("Z", "+00:00"))

        # Crear o recuperar instancia de Moneda
        if nombre_moneda not in monedas:
            monedas[nombre_moneda] = MonedaConcreta(nombre_moneda)
        
        moneda = monedas[nombre_moneda]
        
        # Crear instancia de Cotizacion
        cotizacion = CotizacionConcreta(fecha_actualizacion, valor_compra, valor_venta)

        # Crear o recuperar instancia de Tipo y agregar cotización
        tipo_existente = None
        for tipo in moneda.tipo_casas:
            if tipo.mostrar_nombre_tipo() == nombre_tipo:
                tipo_existente = tipo
                break
        
        if not tipo_existente:
            tipo_existente = TipoConcreto(nombre_tipo)
            moneda.tipo_casas.append(tipo_existente)
        
        tipo_existente.cargar_cotizaciones(cotizacion)
    
    return monedas

def crear_instancias_cotizaciones_desde_api():
    datos = obtener_datos_api_cotizaciones()
    monedas = {}

    for dato in datos:
        casa=dato["casa"]
        nombre_moneda = dato["moneda"]
        nombre_tipo = dato["nombre"]
        valor_compra = dato["compra"]
        valor_venta = dato["venta"]
        fecha_actualizacion = datetime.fromisoformat(dato["fechaActualizacion"].replace("Z", "+00:00"))

        # Crear o recuperar instancia de Moneda
        if nombre_moneda not in monedas:
            monedas[nombre_moneda] = MonedaConcreta(nombre_moneda)
        
        moneda = monedas[nombre_moneda]
        
        # Crear instancia de Cotizacion
        cotizacion = CotizacionConcreta(fecha_actualizacion, valor_compra, valor_venta)

        # Crear o recuperar instancia de Tipo y agregar cotización
        tipo_existente = None
        for tipo in moneda.tipo_casas:
            if tipo.mostrar_nombre_tipo() == nombre_tipo:
                tipo_existente = tipo
                break
        
        if not tipo_existente:
            tipo_existente = TipoConcreto(nombre_tipo)
            moneda.tipo_casas.append(tipo_existente)
        
        tipo_existente.cargar_cotizaciones(cotizacion)
    
    return monedas
