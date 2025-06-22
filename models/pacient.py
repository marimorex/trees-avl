# paciente.py
from datetime import datetime
from copy import deepcopy

class Paciente:
    """Representa un paciente con información médica relevante."""

    def __init__(self, dni, nombre, sexo, edad, diagnosticos, alergias, fecha_ultima_visita):
        self.dni = dni
        self.nombre = nombre
        self.sexo = sexo
        self.edad = int(edad)
        self.diagnosticos = diagnosticos.split('|')
        self.alergias = alergias.split('|')
        self.fecha_ultima_visita = datetime.strptime(fecha_ultima_visita, "%Y-%m-%d")


    def __lt__(self, other):
        return self.dni < other.dni

    def __eq__(self, other):
        return self.dni == other.dni

    def __str__(self):
        return f"{self.dni}: {self.nombre}, {self.edad} años, visita: {self.fecha_ultima_visita.date()}"

    @staticmethod
    def combinar_listas_sin_repetidos(lista1, lista2):
        resultado = []
        for item in lista1:
            if item not in resultado:
                resultado.append(item)
        for item in lista2:
            if item not in resultado:
                resultado.append(item)
        return resultado

    def combinar_con(self, otro):
        """Fusiona los datos de este paciente con otro (por el mismo DNI)."""
        if self.fecha_ultima_visita >= otro.fecha_ultima_visita:
            preferido, auxiliar = self, otro
        else:
            preferido, auxiliar = otro, self

        nuevo = deepcopy(preferido)
        nuevo.diagnosticos = self.combinar_listas_sin_repetidos(preferido.diagnosticos, auxiliar.diagnosticos)
        nuevo.alergias = self.combinar_listas_sin_repetidos(preferido.alergias, auxiliar.alergias)
        nuevo.fecha_ultima_visita = max(self.fecha_ultima_visita, otro.fecha_ultima_visita)

        return nuevo