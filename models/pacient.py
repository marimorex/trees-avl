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
