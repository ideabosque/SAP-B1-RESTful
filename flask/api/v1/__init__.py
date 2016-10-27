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


from .sapb1api import InfoAPI, OrdersAPI, OrderAPI, ContactsAPI, ContactAPI, OrderCancelAPI, ShipmentsAPI

api_v1.add_resource(InfoAPI, '/info', endpoint='info')
api_v1.add_resource(OrdersAPI, '/orders', endpoint='orders')
api_v1.add_resource(OrderAPI, '/order', endpoint='order')
api_v1.add_resource(ContactsAPI, '/contacts', endpoint='contacts')
api_v1.add_resource(ContactAPI, '/contact', endpoint='contact')
api_v1.add_resource(OrderCancelAPI, '/cancelorder', endpoint='cancelorder')
api_v1.add_resource(ShipmentsAPI, '/shipments', endpoint='shipments')
