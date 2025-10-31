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
        nombre="Soplete",
        altura=1.6,
        habilidad="Inhalar mas que una aspiradora",
        imagen="soplete.jpg",
        frase="Donde es hoy manito que estoy que me soplo"
    ),
    Pokenea(
        id=2,
        nombre="El 420",
        altura=0.8,
        habilidad="Weed Master",
        imagen="420.jpg",
        frase="Vamos a pegarlo"
    ),
    Pokenea(
        id=3,
        nombre="Vizajoso",
        altura=0.6,
        habilidad="Intimidación",
        imagen="vizajoso.jpg",
        frase="Cucho decime la hora"
    ),
    Pokenea(
        id=4,
        nombre="Celador",
        altura=2.1,
        habilidad="Alta visición",
        imagen="celador.jpg",
        frase="Manito va colaborar pa la celada"
    ),
    Pokenea(
        id=5,
        nombre="Gota gota",
        altura=0.3,
        habilidad="Robo",
        imagen="gota.jpg",
        frase="Chuga ya reunio lo del patron"
    ),
    Pokenea(
        id=6,
        nombre="Barrista",
        altura=1.2,
        habilidad="Alta fidelidad",
        imagen="barrista.jpg",
        frase="Uy niño el que se meta con mi equipo se mete conmigo"
    ),
    Pokenea(
        id=7,
        nombre="Pampara",
        altura=0.9,
        habilidad="Luminiscencia",
        imagen="pampara.jpg",
        frase="Manito no me ves estas pintas yo soy la pampara"
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
