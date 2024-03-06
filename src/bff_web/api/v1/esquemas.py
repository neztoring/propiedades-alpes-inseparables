import typing
import strawberry
import requests
import os

from datetime import datetime


PROPIEDADES_HOST = os.getenv("PRORIEDADES_ADDRESS", default="localhost")

def obtener_propiedades(root) -> typing.List["Propiedad"]:
    propiedades_json = requests.get(f'http://{PROPIEDADES_HOST}:5002/propiedades/propiedades-query').json()
    propiedades = []

    for propiedad in propiedades_json:
        propiedades.append(
            Propiedad(
                id_propiedad=propiedad.get('id_propiedad'), 
                nombre_propiedad=propiedad.get('nombre_propiedad'), 
                estado_propiedad=propiedad.get('estado_propiedad'), 
                cliente_propiedad=propiedad.get('cliente_propiedad')
            )
        )

    return propiedades



@strawberry.type
class Propiedad:
    id_propiedad: str
    nombre_propiedad: str
    estado_propiedad: str
    cliente_propiedad: str



@strawberry.type
class PropiedadRespuesta:
    mensaje: str
    codigo: int






