import src.propiedadesalpes.seedwork.presentacion.api as api

from src.propiedadesalpes.seedwork.aplicacion.comandos import ejecutar_comando
from src.propiedadesalpes.seedwork.dominio.excepciones import ExcepcionDominio

from src.propiedadesalpes.modulos.propiedad.aplicacion.mapeadores import MapeadorPropiedadDTOJson
from src.propiedadesalpes.modulos.propiedad.aplicacion.comandos.crear_propiedad import CrearPropiedad

from flask import request, Response

import json

bp = api.crear_blueprint('propiedades', '/propiedades')

@bp.route("/registrar-propiedad-asincrona", methods=('POST',))
def registrar_propiedad_asincrona():
    try:

        propiedad_dict = request.json

        map_transaction = MapeadorPropiedadDTOJson()
        transaction_dto = map_transaction.externo_a_dto(propiedad_dict)

        comando = CrearPropiedad(
                                 fecha_creacion=transaction_dto.fecha_creacion,
                                 fecha_actualizacion=transaction_dto.fecha_actualizacion,
                                 id=transaction_dto.id,
                                 id_propiedad=transaction_dto.id_propiedad,
                                 nombre_propiedad=transaction_dto.nombre_propiedad,
                                 estado_propiedad=transaction_dto.estado_propiedad,
                                 cliente_propiedad=transaction_dto.cliente_propiedad)
        ejecutar_comando(comando)
        return Response({}, status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
