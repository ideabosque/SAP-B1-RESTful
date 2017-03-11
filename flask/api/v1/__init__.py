from flask import Blueprint, g, Flask, jsonify, abort, make_response, request
from flask_restful import Api, reqparse, fields, marshal
from ..errors import ValidationError, bad_request, not_found

api_v1_bp = Blueprint('api_v1', __name__)
api_v1 = Api(api_v1_bp)

@api_v1_bp.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(str(e))


@api_v1_bp.errorhandler(400)
def bad_request_error(e):
    return bad_request('invalid request')


#@api_v2_bp.before_request
#@auth.login_required
#def before_request():
#    pass


from .sapb1api import InfoAPI, CodeAPI, OrdersAPI, ContactsAPI, ShipmentsAPI

api_v1.add_resource(InfoAPI, '/info', endpoint='info')
api_v1.add_resource(CodeAPI, '/code', endpoint='code')
api_v1.add_resource(OrdersAPI, '/orders/<function>')
api_v1.add_resource(ContactsAPI, '/contacts/<function>')
api_v1.add_resource(ShipmentsAPI, '/shipments/<function>')
