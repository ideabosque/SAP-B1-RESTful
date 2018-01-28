from flask import request, current_app
from ..app import sapb1Adaptor
from flask_jwt import jwt_required, current_identity
from flask_restful import Resource
import json
import traceback

class InfoAPI(Resource):

    def __init__(self):
        super(InfoAPI, self).__init__()

    @jwt_required()
    def get(self):
        info = sapb1Adaptor.info()
        return info, 201

class CodeAPI(Resource):

    def __init__(self):
        super(CodeAPI, self).__init__()

    @jwt_required()
    def get(self):
        type = request.args.get("type")
        codes = []
        if type == "ExpnsName":
            codes = sapb1Adaptor.getExpnsNames()
        elif type == "TrnspName":
            codes = sapb1Adaptor.getTrnspNames()
        elif type == "PayMethCod":
            codes = sapb1Adaptor.getPayMethCods()
        elif type == "TaxCode":
            codes = sapb1Adaptor.getTaxCodes()
        return codes, 201

class OrdersAPI(Resource):

    def __init__(self):
        super(OrdersAPI, self).__init__()

    @jwt_required()
    def put(self, function):
        try:
            if function == "fetch":
                _num = request.args.get("num")
                _num = 100 if _num is None else int(_num)
                num = 100 if _num > 100 else _num
                data = request.get_json(force=True)
                columns = data['columns'] if 'columns' in data.keys() else {}
                params = data['params']
                orders = sapb1Adaptor.getOrders(num=num, columns=columns, params=params)
                return orders, 201
            else:
                log = "No such function({0})!!!".format(function)
                current_app.logger.error(log)
                raise Exception(log)
        except Exception as e:
            log = traceback.format_exc()
            current_app.logger.exception(e)
            return log, 501

    @jwt_required()
    def post(self, function):
        try:
            orders = request.get_json(force=True)
            if function == "insert":
                for order in orders:
                    try:
                        order["bo_order_id"] = sapb1Adaptor.insertOrder(order)
                        order["tx_status"] = 'S'
                    except Exception as e:
                        log = traceback.format_exc()
                        order["bo_order_id"] = "####"
                        order["tx_status"] = 'F'
                        order["tx_note"] = log
                        current_app.logger.exception(e)
            elif function == "cancel":
                for order in orders:
                    try:
                        order["bo_order_id"] = sapb1Adaptor.cancelOrder(order)
                        order["tx_status"] = 'X'
                    except Exception as e:
                        log = traceback.format_exc()
                        order["tx_status"] = 'F'
                        order["tx_note"] = log
                        current_app.logger.exception(e)
            else:
                log = "No such function({0})!!!".format(function)
                current_app.logger.error(log)
                raise Exception(log)
            return orders, 201
        except Exception as e:
            log = traceback.format_exc()
            current_app.logger.exception(e)
            return log, 501

# Retrieve contacts by CardCode.
class ContactsAPI(Resource):

    def __init__(self):
        super(ContactsAPI, self).__init__()

    @jwt_required()
    def put(self, function):
        try:
            if function == "fetch":
                _num = request.args.get("num")
                _num = 100 if _num is None else int(_num)
                num = 100 if _num > 100 else _num
                data = request.get_json(force=True)
                columns = data['columns'] if 'columns' in data.keys() else {}
                cardCode = data['card_code']
                contact = data['contact']
                contacts = sapb1Adaptor.getContacts(num=num, columns=columns, cardCode=cardCode, contact=contact)
                return contacts, 201
            else:
                log = "No such function({0})!!!".format(function)
                current_app.logger.error(log)
                raise Exception(log)
        except Exception as e:
            log = traceback.format_exc()
            current_app.logger.exception(e)
            return log, 501

    @jwt_required()
    def post(self, function):
        try:
            if function == "insert":
                data = request.get_json(force=True)
                cardCode = data['card_code']
                contacts = data['contacts']
                for contact in contacts:
                    contactCode = sapb1Adaptor.insertContact(cardCode, contact)
                    contact["contact_code"] = contactCode
                return contacts, 201
            else:
                log = "No such function({0})!!!".format(function)
                current_app.logger.error(log)
                raise Exception(log)
        except Exception as e:
            log = traceback.format_exc()
            current_app.logger.exception(e)
            return log, 501

#Retrive Shipments
class ShipmentsAPI(Resource):

    def __init__(self):
        super(ShipmentsAPI, self).__init__()

    @jwt_required()
    def put(self, function):
        try:
            if function == "fetch":
                _num = request.args.get("num")
                _num = 100 if _num is None else int(_num)
                num = 100 if _num > 100 else _num
                data = request.get_json(force=True)
                columns = data['columns'] if 'columns' in data.keys() else {}
                itemColumns = data['itemcolumns'] if 'itemcolumns' in data.keys() else {}
                params = data['params']
                shipments = sapb1Adaptor.getShipments(num=num, columns=columns, params=params, itemColumns=itemColumns)
                return shipments, 201
            else:
                log = "No such function({0})!!!".format(function)
                current_app.logger.error(log)
                raise Exception(log)
        except Exception as e:
            log = traceback.format_exc()
            current_app.logger.exception(e)
            return log, 501
