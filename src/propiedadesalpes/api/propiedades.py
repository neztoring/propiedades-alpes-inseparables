import src.propiedadesalpes.seedwork.presentacion.api as api
import json
from src.propiedadesalpes.modulos.propiedades.aplicacion.servicios import ServicioTransaccion
from src.propiedadesalpes.seedwork.dominio.excepciones import ExcepcionDominio

from flask import request
from flask import Response
from src.propiedadesalpes.modulos.propiedades.aplicacion.mapeadores import MapeadorTransaccionDTOJson

bp = api.crear_blueprint('propiedades', '/propiedades')

@bp.route('/transaccion', methods=('POST',))
def reservar():
    try:
        transaction_dict = request.json

        map_transaction = MapeadorTransaccionDTOJson()
        transaction_dto = map_transaction.externo_a_dto(transaction_dict)

        st = ServicioTransaccion()
        dto_final = st.crear_transaccion(transaction_dto)

        return map_transaction.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/transaccion', methods=('GET',))
@bp.route('/transaccion/<id>', methods=('GET',))
def dar_reserva(id=None):
    if id:
        st = ServicioTransaccion()
        
        return st.obtener_transaccion_por_id(id)
    else:
        return [{'message': 'GET!'}]