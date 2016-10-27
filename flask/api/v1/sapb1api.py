from flask import request, current_app
from ..auth import auth
from ..app import sapb1Adaptor
from flask_restful import Resource
import json
import traceback

class InfoAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        super(InfoAPI, self).__init__()

    def get(self):
        info = sapb1Adaptor.info()
        return info, 201

class OrdersAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        super(OrdersAPI, self).__init__()

    def post(self):
        data = request.get_json(force=True)
        num = data['num'] if 'num' in data.keys() else 1
        columns = data['columns'] if 'columns' in data.keys() else {}
        params = data['params']
        orders = sapb1Adaptor.getOrders(num=num, columns=columns, params=params)
        return orders, 201

# Insert an order into B1.
class OrderAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        super(OrderAPI, self).__init__()

    def post(self):
        order = request.get_json(force=True)
        try:
            boOrderId = sapb1Adaptor.insertOrder(order)
            return {'bo_order_id': boOrderId}, 201
        except Exception as e:
            log = traceback.format_exc()
            current_app.logger.exception(e)
            return log, 501

# Retrieve contacts by CardCode.
class ContactsAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        super(ContactsAPI, self).__init__()

    def post(self):
        data = request.get_json(force=True)
        num = data['num'] if 'num' in data.keys() else 1
        columns = data['columns'] if 'columns' in data.keys() else {}
        cardCode = data['card_code']
        contact = data['contact']
        contacts = sapb1Adaptor.getContacts(num=num, columns=columns, cardCode=cardCode, contact=contact)
        return contacts, 201

# Insert contact by CardCode.
class ContactAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        super(ContactAPI, self).__init__()

    def post(self):
        data = request.get_json(force=True)
        cardCode = data['card_code']
        contact = data['contact']
        try:
            contactCode = sapb1Adaptor.insertContact(cardCode, contact)
            return {"contact_code": contactCode}, 201
        except Exception as e:
            log = traceback.format_exc()
            current_app.logger.exception(e)
            return log, 501

# Cancel an order in B1.
class OrderCancelAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        super(OrderCancelAPI, self).__init__()

    def post(self):
        order = request.get_json(force=True)
        try:
            boOrderId = sapb1Adaptor.cancelOrder(order)
            return {'bo_order_id': boOrderId}, 201
        except Exception as e:
            log = traceback.format_exc()
            current_app.logger.exception(e)
            return log, 501

#Retrive Shipments
class ShipmentsAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        super(ShipmentsAPI, self).__init__()

    def post(self):
        data = request.get_json(force=True)
        num = data['num'] if 'num' in data.keys() else 100
        columns = data['columns'] if 'columns' in data.keys() else {}
        itemColumns = data['itemcolumns'] if 'itemcolumns' in data.keys() else {}
        params = data['params']
        shipments = sapb1Adaptor.getShipments(num=num, columns=columns, params=params, itemColumns=itemColumns)
        return shipments, 201
