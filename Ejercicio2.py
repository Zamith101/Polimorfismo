class Empleado:
    # Clase principal para los empleados del ejercicio
    def __init__(self, nombre, sueldo_base): # metodo constructor
        self._nombre = nombre
        self._sueldo_base = sueldo_base

    @property
    def sueldo_base(self): # getter
        return self._sueldo_base

    @sueldo_base.setter
    def sueldo_base(self, nuevo_sueldo):  # Setter para cambiar el sueldo base (validando que no sea negativo)
        if nuevo_sueldo >= 0:
            self._sueldo_base = nuevo_sueldo
        else:
            print("Sueldo no válido")

    def calcular_salario(self): # Método que devuelve el sueldo base (puede ser sobreescrito por clases hijas)
        return self._sueldo_base


class EmpleadoFijo(Empleado):
    def calcular_salario(self):
        # El empleado fijo recibe un bono extra de 2000
        return self.sueldo_base + 2000


class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, sueldo_base, horas):
        super().__init__(nombre, sueldo_base)
        self.horas = horas

    def calcular_salario(self):
        # El salario del empleado por horas se calcula multiplicando el sueldo base por las horas trabajadas
        return self.sueldo_base * self.horas


class EmpleadoTemporal(Empleado):
    def calcular_salario(self):
        # El empleado temporal tiene un descuento en su salario de 1000
        return self.sueldo_base - 1000


# Lista de empleados creada con diferentes tipos
empleados = [
    EmpleadoFijo("Ana", 3000),
    EmpleadoPorHoras("Luis", 20, 160),
    EmpleadoTemporal("Sofia", 2500)
]

# Se recorre la lista para calcular y mostrar el salario de cada empleado
for empleado in empleados:
    print("Nombre:", empleado._nombre)
    print("Salario calculado:", empleado.calcular_salario())
    print("------")
