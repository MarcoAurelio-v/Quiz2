class Empleado:
    def __init__(self, nombre, apellido, cedula, tipo, horas_trabajadas):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.tipo = tipo
        self.horas_trabajadas = horas_trabajadas
        self.tarifa = self.asignar_tarifa()
        self.monto_total = self.calcular_monto_total()

    def asignar_tarifa(self):
        tarifas = {
            'Ingeniero': 25,
            'Arquitecto': 10,
            'Obrero': 5
        }
        return tarifas.get(self.tipo, 0)

    def calcular_monto_total(self):
        monto = self.horas_trabajadas * self.tarifa
        if self.es_numero_primo(self.horas_trabajadas):
            monto *= 1.05
        if self.es_numero_deficiente(monto):
            monto *= 1.10 
        return monto


    def es_numero_primo(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def es_numero_deficiente(n):
        suma_divisores = sum(i for i in range(1, n) if n % i == 0)
        return suma_divisores < n


class Ingeniero(Empleado):
    def __init__(self, nombre, apellido, cedula, horas_trabajadas, especialidad):
        super().__init__(nombre, apellido, cedula, 'Ingeniero', horas_trabajadas)
        self.especialidad = especialidad


class Arquitecto(Empleado):
    def __init__(self, nombre, apellido, cedula, horas_trabajadas, especialidad):
        super().__init__(nombre, apellido, cedula, 'Arquitecto', horas_trabajadas)
        self.especialidad = especialidad


class Obrero(Empleado):
    def __init__(self, nombre, apellido, cedula, horas_trabajadas, tipo_obrero):
        super().__init__(nombre, apellido, cedula, 'Obrero', horas_trabajadas)
        self.tipo_obrero = tipo_obrero


class ControlHoras:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def total_pagado(self):
        return sum(empleado.monto_total for empleado in self.empleados)

    def cantidad_empleados_por_tipo(self):
        conteo = {}
        for empleado in self.empleados:
            if empleado.tipo not in conteo:
                conteo[empleado.tipo] = 0
            conteo[empleado.tipo] += 1
        return conteo

    def promedio_pago_por_tipo(self):
        total_por_tipo = {}
        conteo_por_tipo = self.cantidad_empleados_por_tipo()

        for empleado in self.empleados:
            if empleado.tipo not in total_por_tipo:
                total_por_tipo[empleado.tipo] = 0
            total_por_tipo[empleado.tipo] += empleado.monto_total

        promedio = {tipo: total / conteo for tipo, total in total_por_tipo.items() for conteo in [conteo_por_tipo[tipo]]}
        return promedio

    def empleado_con_mayor_pago_por_tipo(self):
        max_pago = {}
        for empleado in self.empleados:
            if empleado.tipo not in max_pago or empleado.monto_total > max_pago[empleado.tipo].monto_total:
                max_pago[empleado.tipo] = empleado
        return max_pago