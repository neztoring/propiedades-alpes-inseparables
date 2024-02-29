import src.propiedadesalpes.seedwork.presentacion.api as api

from src.propiedadesalpes.seedwork.aplicacion.comandos import ejecutar_comando
from src.propiedadesalpes.seedwork.aplicacion.queries import ejecutar_query
from src.propiedadesalpes.seedwork.dominio.excepciones import ExcepcionDominio

from src.propiedadesalpes.modulos.propiedad.aplicacion.mapeadores import MapeadorPropiedadDTOJson, MapeadorListaPropiedadToJSON
from src.propiedadesalpes.modulos.propiedad.aplicacion.comandos.crear_propiedad import CrearPropiedad
from src.propiedadesalpes.modulos.propiedad.aplicacion.queries.obtener_propiedades import ObtenerPropiedades


from flask import request, Response

import json

bp = api.crear_blueprint('propiedades', '/propiedades')

@bp.route("/registrar-propiedad-asincrona", methods=('POST',))
def registrar_propiedad_asincrona():
    try:
        propiedad_dict = request.json

        map_propiedad = MapeadorPropiedadDTOJson()
        propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)

        comando = CrearPropiedad(
                                 fecha_creacion=propiedad_dto.fecha_creacion,
                                 fecha_actualizacion=propiedad_dto.fecha_actualizacion,
                                 id=propiedad_dto.id,
                                 id_propiedad=propiedad_dto.id_propiedad,
                                 nombre_propiedad=propiedad_dto.nombre_propiedad,
                                 estado_propiedad=propiedad_dto.estado_propiedad,
                                 cliente_propiedad=propiedad_dto.cliente_propiedad)
        ejecutar_comando(comando)
        return Response({}, status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/propiedades-query', methods=('GET',))
def dar_transaccion_query(id=None):

    query_resultado = ejecutar_query(ObtenerPropiedades("LIBRE"))
    map_propiedad = MapeadorListaPropiedadToJSON()

    return map_propiedad.dtos_a_externos(query_resultado.resultado)
