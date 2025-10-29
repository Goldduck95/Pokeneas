# app/models.py
import random

class Pokenea:
    """Modelo para representar un Pokenea"""
    
    def __init__(self, id, nombre, altura, habilidad, imagen, frase):
        self.id = id
        self.nombre = nombre
        self.altura = altura
        self.habilidad = habilidad
        self.imagen = imagen
        self.frase = frase
    
    def to_dict(self):
        """Convierte el Pokenea a diccionario"""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'altura': self.altura,
            'habilidad': self.habilidad,
            'imagen': self.imagen,
            'frase': self.frase
        }
    
    def to_json_response(self):
        """Devuelve solo los campos para la ruta JSON"""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'altura': self.altura,
            'habilidad': self.habilidad
        }


# Base de datos simulada (arreglo quemado)
POKENEAS_DATA = [
    Pokenea(
        id=1,
        nombre="Bandejon",
        altura=1.5,
        habilidad="Servir porciones abundantes",
        imagen="bandejon.png",
        frase="La vida es como un bandejo paisa, hay que disfrutarla completa"
    ),
    Pokenea(
        id=2,
        nombre="Arrepiso",
        altura=0.8,
        habilidad="Calentar recuerdos",
        imagen="arrepiso.png",
        frase="Del arrepentimiento nace la sabiduría"
    ),
    Pokenea(
        id=3,
        nombre="Mazamorra",
        altura=0.6,
        habilidad="Endulzar el alma",
        imagen="mazamorra.png",
        frase="La paciencia es la madre de todas las virtudes"
    ),
    Pokenea(
        id=4,
        nombre="Paisamon",
        altura=2.1,
        habilidad="Representar la cultura paisa",
        imagen="paisamon.png",
        frase="Parcero, la vida es muy berraca para no disfrutarla"
    ),
    Pokenea(
        id=5,
        nombre="Arepon",
        altura=0.3,
        habilidad="Acompañar cualquier comida",
        imagen="arepon.png",
        frase="Lo importante no es el tamaño, sino el sabor que aportas"
    ),
    Pokenea(
        id=6,
        nombre="Choripaisa",
        altura=1.2,
        habilidad="Alegrar las tardes",
        imagen="choripaisa.png",
        frase="Con chimichurri todo sabe mejor"
    ),
    Pokenea(
        id=7,
        nombre="Empanador",
        altura=0.9,
        habilidad="Crujir perfectamente",
        imagen="empanador.png",
        frase="Por fuera crujiente, por dentro suave, así es la vida"
    ),
]


def get_random_pokenea():
    """Obtiene un Pokenea aleatorio"""
    return random.choice(POKENEAS_DATA)


def get_pokenea_by_id(pokenea_id):
    """Busca un Pokenea por ID"""
    for pokenea in POKENEAS_DATA:
        if pokenea.id == pokenea_id:
            return pokenea
    return None


def get_all_pokeneas():
    """Devuelve todos los Pokeneas"""
    return POKENEAS_DATA
