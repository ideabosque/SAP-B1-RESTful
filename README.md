# SAP B1 RESTful
==========

## Synopsis
The python flask application is top on the SAP B1 DI API interface to provide the RESTful capability with the following functions.
  1. Show the system information.
  2. Retrieve orders.
  3. Insert an order.


## Architecture

## Class Structure

## Configuration

## Prerequisites
  1. Python 2.7.
  2. Python for Windows Extension.
  3. pymssql.

## API

#### InfoAPI
  ```bash
  GET /v1/info
  ```
  Return the information of the system.

  Example response body:
  ```bash
  {
    "diapi": "SAPbobsCOM90",
    "company_db": "SBODEMOUS",
    "company_name": "OEC Computers",
    "server": "SAPB191"
  }
  ```

  Example script by curl:
  ```bash
  curl -u admin:secret -X GET -H 'Content-Type: application/json' http://192.168.44.148:5000/v1/info
  ```

#### OrdersAPI
  ```bash
  POST /v1/orders
  ```
  Retrieve orders by parameters.

  Request Parameters:
  num(option): The amount of the records will be contained in the result.  IF not specified, only one record will be fetched.
  columns(option): Which columns will be in the response result.  If not specified, all columns will be used.
  params(required): The query condition parameters.
  ops(option): The operators for each condition.  If a condition doesn't specified an operator, equal "=" will be assigned.

  Example request body:
  ```bash
  {
    "num": "1",
    "columns": ["DocNum", "CardName", "DocDate", "Address", "Address2"],
    "params": {"DocDate": "2016-01-01"},
    "ops": {"DocDate": ">="}
  }
  ```

  Example response body:
  ```bash
  [
    {
      "DocDate": "2016-06-20 00:00:00",
      "Address2": "3921 W Collins St\r\r3921 W Collins St FL  33607\rUSA",
      "CardName": "Werner Richter",
      "DocNum": "491",
      "Address": "3921 W Collins St\r\rTampa FL  33607\rUSA"
    }
  ]
  ```

  Example script by curl:
  ```bash
  curl -u admin:secret -X POST -H 'Content-Type: application/json' http://192.168.44.148:5000/v1/orders -d '{"num": "1", "columns": ["DocNum", "CardName", "DocDate", "Address", "Address2"], "params": {"DocDate": "2016-01-01 00:00:00"}, "ops": {"DocDate": ">="}}'
  ```
