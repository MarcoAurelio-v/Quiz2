class Persona:
    def __init__(self, nombre: str, apellido: str, cedula: int, horas_trabajadas: float, tipo):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.horas_trabajadas = horas_trabajadas
        self.tipo = tipo
    def show(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Cedula: {self.cedula}")
        print(f"Horas trabajadas: {self.horas_trabajadas}")
        print(f"Tipo: {self.tipo}")
        
class Ingeniero(Persona):
    def __init__(self, nombre, apellido, cedula, horas_trabajadas, mes_trabajado, datos_especialidad, monto_factura):
        super().__init__(nombre, apellido, cedula, horas_trabajadas)
        self.mes_trabajado = mes_trabajado
        self.datos_especialidad = datos_especialidad
        self.monto_factura = monto_factura
        
    def show(self):
        print(f"Meses trabajados: {self.mes_trabajado}")
        print(f"Datos especialidad: {self.datos_especialidad}")
        print(f"Monto a facturar: {self.monto_factura}")
        
class Arquitecto(Persona):
    def __init__(self, nombre, apellido, cedula, horas_trabajadas, mes_trabajado, datos_especialidad, monto_factura):
        super().__init__(nombre, apellido, cedula, horas_trabajadas)
        self.mes_trabajado = mes_trabajado
        self.datos_especialidad = datos_especialidad
        self.monto_factura = monto_factura
        
    def show(self):
        print(f"Meses trabajados: {self.mes_trabajado}")
        print(f"Datos especialidad: {self.datos_especialidad}")
        print(f"Monto a facturar: {self.monto_factura}")
        
class Obrero(Persona):
    def __init__(self, nombre, apellido, cedula, horas_trabajadas, mes_trabajado, datos_especialidad, monto_factura):
        super().__init__(nombre, apellido, cedula, horas_trabajadas)
        self.mes_trabajado = mes_trabajado
        self.datos_especialidad = datos_especialidad
        self.monto_factura = monto_factura
        
    def show(self):
        print(f"Meses trabajados: {self.mes_trabajado}")
        print(f"Datos especialidad: {self.datos_especialidad}")
        print(f"Monto a facturar: {self.monto_factura}")