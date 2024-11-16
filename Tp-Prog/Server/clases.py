class Moneda:
    def __init__(self, moneda):
        self.moneda = moneda

    def mostrar_moneda(self):
        return self.moneda

class Tipo(Moneda):
    def __init__(self, nombre_moneda, nombre,):
         super().__init__(nombre_moneda)
         self.cargar_nombre(nombre)
    def cargar_nombre(self, nombre):
         self.nombre = nombre
    def mostrar_nombre(self):
        return self.nombre
    def str(self):
         return f"{self.mostrar_moneda()}, {self.mostrar_nombre()}"

class Cotizacion:
    def __init__(self, nombre_moneda, nombre, compra, venta, fecha):
        self.tipo = Tipo(nombre_moneda, nombre) 
        self.compra = compra
        self.venta = venta
        self.fecha = fecha

    def mostrar_moneda(self):
        return self.tipo.mostrar_moneda() 

    def mostrar_nombre(self):
        return self.tipo.mostrar_nombre()  

    def mostrar_compra(self):
        return self.compra

    def mostrar_venta(self):
        return self.venta

    def mostrar_fecha(self):
        return self.fecha

    def str(self):
        return f"{self.mostrar_moneda()}, {self.mostrar_nombre()}, {self.mostrar_compra()}, {self.mostrar_venta()}, {self.mostrar_fecha()}"