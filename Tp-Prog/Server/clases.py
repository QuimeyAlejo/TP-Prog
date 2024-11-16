class Moneda():
    def __init__(self, moneda):
        self.cargar_moneda(moneda)
    def cargar_moneda(self, moneda):
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

class Cotizacion(Tipo):
    def __init__(self,nombre_moneda, nombre, compra, venta, fecha):
        super().__init__(nombre_moneda, nombre)
        self.cargar_compra(compra)
        self.cargar_venta(venta)
        self.cargar_fecha(fecha)
    def cargar_compra(self, compra):
        self.compra = compra
    def mostrar_compra(self):
        return self.compra
    def cargar_venta(self, venta):
        self.venta = venta
    def mostrar_venta(self):
        return self.venta
    def cargar_fecha(self, fecha):
        self.fecha = fecha
    def mostrar_fecha(self):
        return self.fecha
    def str(self):
        return f"{self.mostrar_moneda()}, {self.mostrar_nombre()}, {self.mostrar_compra()}, {self.mostrar_venta()}, {self.mostrar_fecha()}"    