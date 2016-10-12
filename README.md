# SAP B1 RESTful
==========

## Synopsis
The python flask application is top on the SAP B1 DI API interface to provide the RESTful capability with the following functions.
  1. Show the system information.
  2. Retrieve orders.
  3. Insert an order.
  4. Retrieve contacts of a business partner.


## Architecture

## Configuration

## Prerequisites
  1. Python 2.7.
  2. Python for Windows Extension.
  3. pymssql.

## API

#### InfoAPI
  ```
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
  ```
  POST /v1/orders
  ```
  Retrieve orders by parameters.

  Request Parameters:
  * num(option): The amount of the records will be contained in the result.  IF not specified, only one record will be fetched.
  * columns(option): Which columns will be in the response result.  If not specified, all columns will be used.
  * params(required): The query condition parameters.
  * ops(option): The operators for each condition.  If a condition doesn't specified an operator, equal "=" will be assigned.

  Example request body:
  ```javascript
  {
    "num": "1",
    "columns": ["DocNum", "CardName", "DocDate", "Address", "Address2"],
    "params": {"DocDate": "2016-01-01"},
    "ops": {"DocDate": ">="}
  }
  ```

  Example response body:
  ```javascript
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

#### OrderAPI
  ```
  POST /v1/order
  ```
  Insert an order into SAP B1.

  Request Parameters:
  * doc_due_date: Order due date.
  * card_code: Customer code.
  * expenses_freightname: Freightname for shipping.
  * expenses_linetotal: Total of the shipping cost.
  * expenses_taxcode: Taxcode for shipping.
  * discount_percent: Discount percentage.
  * transport_name: Shipping method.
  * payment_method: Payment method.
  * fe_order_id: Front end order id.
  * fe_order_id_udf: Front end order id UDF if it is set.
  * billto_firstname: Bill to first name.
  * billto_lastname: Bill to last name.
  * billto_email: Bill to email.
  * billto_companyname: Bill to company name.
  * billto_city: Bill to city.
  * billto_country: Bill to country.
  * billto_county: Bill to county.
  * billto_state: Bill to state.
  * billto_address: Bill to address.
  * billto_zipcode: Bill to zipcode.
  * billto_telephone: Bill to telephone.
  * shipto_firstname: Ship to first name.
  * shipto_lastname: Ship to last name.
  * shipto_companyname: Ship to company name.
  * shipto_city: Ship to city.
  * shipto_country: Ship to country.
  * shipto_county: Ship to county.
  * shipto_state: Ship to state.
  * shipto_address: Ship to address.
  * shipto_zipcode: Ship to zipcode.
  * shipto_telephone: Ship to telephone.
  * items: item[] The line item in the order.
    - itemcode: Product sku.
    - quantity: Total quantity of the line item.
    - price: Price of the line item.
    - taxcode: Taxcode of the line item.
    - linetotal: Subtotal of the line item.

  Example request body:
  ```javascript
  {
    "doc_due_date": "2016-12-12",
    "card_code": "C20000",
    "expenses_freightname": "Freight",
    "expenses_linetotal": "2",
    "expenses_taxcode": "Exempt",
    "transport_name": "Fedex ON",
    "payment_method": "Incoming BT 02",
    "fe_order_id": "00000002",
    "billto_firstname": "John",
    "billto_lastname": "Smith",
    "billto_email": "john.smith@xyz.net",
    "billto_companyname": "",
    "billto_city": "Los Angeles",
    "billto_country": "US",
    "billto_county": "",
    "billto_state": "CA",
    "billto_address": "3650 McClintock Avenue",
    "billto_zipcode": "90089",
    "billto_telephone": "(213) 740-8674",
    "shipto_firstname": "John",
    "shipto_lastname": "Smith",
    "shipto_companyname": "",
    "shipto_city": "Los Angeles",
    "shipto_country": "US",
    "shipto_county": "",
    "shipto_state": "CA",
    "shipto_address": "3650 McClintock Avenue",
    "shipto_zipcode": "90089",
    "shipto_telephone": "(213) 740-8674",
    "items": [
      {
        "itemcode": "I00001",
        "quantity": "10",
        "price": "12",
        "taxcode": "CA",
        "linetotal": "120"
      }
    ]
  }
  ```

  Example response body:
  ```javascript
  {
    "bo_order_id": "536"
  }
  ```

  Example script by curl:
  ```bash
  curl -u admin:secret -X POST -H 'Content-Type: application/json' http://192.168.44.148:5000/v1/order -d '{"doc_due_date": "2016-12-12", "card_code": "C20000", "expenses_freightname": "Freight", "expenses_linetotal": "2", "expenses_taxcode": "Exempt", "transport_name": "Fedex ON", "payment_method": "Incoming BT 02", "fe_order_id": "00000002", "billto_firstname": "John", "billto_lastname": "Smith", "billto_email": "john.smith@xyz.net", "billto_companyname": "", "billto_city": "Los Angeles", "billto_country": "US", "billto_county": "", "billto_state": "CA", "billto_address": "3650 McClintock Avenue", "billto_zipcode": "90089", "billto_telephone": "(213) 740-8674", "shipto_firstname": "John", "shipto_lastname": "Smith", "shipto_companyname": "", "shipto_city": "Los Angeles", "shipto_country": "US", "shipto_county": "", "shipto_state": "CA", "shipto_address": "3650 McClintock Avenue", "shipto_zipcode": "90089", "shipto_telephone": "(213) 740-8674", "items": [{"itemcode": "I00001", "quantity": "10", "price": "12", "taxcode": "CA", "linetotal": "120"}]}'
  ```

#### ContactsAPI
  ```
  POST /v1/contacts
  ```
  Retrieve contacts under a business partner (CardCode) with conditions.

  Request Parameters:
  * num(option): The amount of the records will be contained in the result.  IF not specified, only one record will be fetched.
  * columns(option): Which columns will be in the response result.  If not specified, all columns will be used.
  * card_code(required): The CardCode of a business partner.
  * contact(required): contact{} The query condition parameters.
    - FirstName: First name.
    - LastName: Last name.
    - E_MailL: Email.

  Example request body:
  ```javascript
  {
    "num": "1",
    "columns": ["cntctcode", "Name"],
    "card_code": "C20000",
    "contact": {
      "FirstName": "John",
      "LastName": "Smith",
      "E_MailL": "john.smith@xyz.net"
    }
  }
  ```

  Example response body:
  ```javascript
  [
    {
      "cntctcode": "60",
      "Name": "John Smith 1476166090.01"
    }
  ]
  ```

  Example script by curl:
  ```bash
  curl -u admin:secret -X POST -H 'Content-Type: application/json' http://192.168.44.148:5000/v1/contacts -d '{"num": "1", "columns": ["cntctcode", "Name"], "card_code": "C20000", "contact": {"FirstName": "John", "LastName": "Smith", "E_MailL": "john.smith@xyz.net"}}'
  ```

#### ContactsAPI
  ```
  POST /v1/contact
  ```
  Insert a contact under a business partner (CardCode) with conditions.

  Request Parameters:


  Example request body:
  ```javascript
  ```

  Example response body:
  ```javascript
  ```

  Example script by curl:
  ```bash
  ```
