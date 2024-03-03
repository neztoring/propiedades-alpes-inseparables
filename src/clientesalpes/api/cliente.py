import src.clientesalpes.seedwork.presentacion.api as api
import json
from src.clientesalpes.modulos.cliente.aplicacion.servicios import ServicioCliente
from src.clientesalpes.seedwork.dominio.excepciones import ExcepcionDominio

from flask import request, jsonify
from flask import Response
from src.clientesalpes.modulos.cliente.aplicacion.mapeadores import MapeadorClienteDTOJson, MapeadorPropiedadDTOJson
from src.clientesalpes.modulos.cliente.aplicacion.comandos.crear_cliente import CrearCliente
from src.clientesalpes.modulos.cliente.aplicacion.comandos.crear_propiedad import CrearPropiedad
from src.clientesalpes.modulos.cliente.aplicacion.queries.obtener_cliente import ObtenerCliente
from src.clientesalpes.seedwork.aplicacion.comandos import ejecutar_comando
from src.clientesalpes.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('cliente', '/cliente')


@bp.route('/cliente', methods=('POST',))
def registrar_cliente():
    try:
        transaction_dict = request.json
        propiedad=transaction_dict.get("propiedad")
        print('********** '+str(propiedad)+' **********', flush=True)

        map_transaction = MapeadorClienteDTOJson()
        transaction_dto = map_transaction.externo_a_dto(transaction_dict)
        st = ServicioCliente()
        dto_final = st.crear_cliente(transaction_dto)

        return map_transaction.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route("/cliente-asincrona", methods=('POST',))
def registrar_cliente_asincrona():
    try:

        transaction_dict = request.json

        map_transaction = MapeadorClienteDTOJson()
        transaction_dto = map_transaction.externo_a_dto(transaction_dict)

        comando = CrearCliente(transaction_dto.fecha_creacion, transaction_dto.fecha_actualizacion, transaction_dto.id, transaction_dto.id_cliente, transaction_dto.nombre_cliente, transaction_dto.tipo_cliente)
        ejecutar_comando(comando)

        if "propiedad" in transaction_dict:
            propiedad_dict = transaction_dict.get("propiedad")
            propiedad_dict["cliente_propiedad"] = transaction_dto.id_cliente
            map_propiedad = MapeadorPropiedadDTOJson()
            propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)
        
            comando_propiedad = CrearPropiedad(propiedad_dto.cliente_propiedad, propiedad_dto.nombre_propiedad, propiedad_dto.estado_propiedad, propiedad_dto.id_propiedad)
            ejecutar_comando(comando_propiedad)


        return Response({}, status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')


@bp.route('/cliente', methods=('GET',))
@bp.route('/cliente/<id>', methods=('GET',))
def dar_cliente(id=None):
    st = ServicioCliente()
    if id:
        return st.obtener_cliente_por_id(id)
    else:
        return jsonify(st.obtener_todos())


@bp.route('/cliente-query', methods=('GET',))
@bp.route('/cliente-query/<id>', methods=('GET',))
def dar_cliente_query(id=None):
    st = ServicioCliente()
    if id:
        query_resultado = ejecutar_query(ObtenerCliente(id))
        map_cliente = MapeadorClienteDTOJson()

        return map_cliente.dto_a_externo(query_resultado.resultado)
    else:
        return [{"message": "GET"}]

