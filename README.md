# SAP B1 RESTful
=====================

## Synopsis
The python flask application is top on the SAP B1 DI API interface to provide the RESTful capability with the following functions.
  1. Show the system information.
  2. Retrieve orders.
  3. Insert an order.
  4. Retrieve contacts of a business partner.
  5. Insert a contact under a business partner.
  6. Retrieve shipments(deliveries).


## Architecture

![SAP B1 RESTful](/images/sap-b1-restful.png?raw=true "SAP B1 RESTful")

  * "SAP B1 RESTful" (Python Flask application) serves RESTful requests from external applications and returns RESTful responses.
  * "Flask-SAPB1" (Flask extension) performs as an adaptor to communicate with SAP B1 by the following two interfaces.
    - SAP B1 DI: insert and update any business objects such as Order, Delivery, AR Invoice and Downpayment Invoice.
    - mssql: read data only directly from MS SQL Server.

## Prerequisites
  1. Install Python 2.7.12 for Windows 64 bits (https://www.python.org/ftp/python/2.7.12/python-2.7.12.amd64.msi).
  2. Install Python for Windows Extensions (pywin32-220.win-amd64-py2.7.exe) (https://sourceforge.net/projects/pywin32/files/pywin32/Build%20220/pywin32-220.win-amd64-py2.7.exe/download)

## Installation
  1. Download and decompress the packages from the following url.
  https://github.com/ideabosque/SAP-B1-RESTful/zipball/0.0.1
  2. Install the required Python packages by pip.
  ```
  pip install -r requirements.txt
  ```

## Configuration and Launch

##### Configuration
  We could configure the service at "flask/config.py".
  ```
  USERNAME = 'admin'  # The RESTful basic username.
  PASSWORD = 'secret'  # The RESTful basic password.
  LOGGING_LOCATION = 'sapb1adaptor.log'  # The RESTful log file.
  LOGGING_LEVEL = logging.INFO    # The log level.
  LOGGING_FORMAT = '%(asctime)s %(levelname)-8s %(message)s'  # The log format.
  DIAPI = 'SAPbobsCOM90'  # The DI version.
  SERVER = 'SAP91'  # SAP B1 server name.
  LANGUAGE = 'ln_English'
  DBSERVERTYPE = 'dst_MSSQL2014'  # The MS SQL Server version.
  DBUSERNAME = 'sa'  # Database username.
  DBPASSWORD = 'XXXXXXXX'  # Database password.
  COMPANYDB = 'SBODEMOUS'  # Database name.
  B1USERNAME = 'manager'  # B1 username.
  B1PASSWORD = 'XXXXXXXX'  # B1 password.
  ```

#### Launch the Server
  You could launch the service by the following command at the command prompt.
  ```bash
  python flask/manage.py runserver -h 0.0.0.0 -p 5000
  ```
  * -h 0.0.0.0 : Bind any IP for the service. (If "-h 127.0.0.1" is used, the service could be accessible only in local.)
  * -p 5000 : Bind the service with port 5000.  Please check the port of Windows Firewall opened for the port.

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
  * num(optional): The amount of the records will be contained in the result.  IF not specified, only one record will be fetched.
  * columns(optional): Which columns will be in the response result.  If not specified, all columns will be used.
  * params: The query condition parameters.
    key: The column name.
    - op(optional): The condition operator.
    - value: The condition value.

  Example request body:
  ```javascript
  {
    "num": "1",
    "columns": ["DocNum", "CardName", "DocDate", "Address", "Address2"],
    "params": {
      "DocDate": {
        "op": ">=",
        "value": "2016-01-01"
      }
    }
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
  curl -u admin:secret -X POST -H 'Content-Type: application/json' http://192.168.44.148:5000/v1/orders -d '{"num": "1", "columns": ["DocNum", "CardName", "DocDate", "Address", "Address2"], "params": {"DocDate": {"op": ">=","value": "2016-01-01"}}}'
  ```

#### OrderAPI
  ```
  POST /v1/order
  ```
  Insert an order into SAP B1.

  Request Parameters:
  * doc_due_date: Order due date.
  * card_code: Customer code.
  * expenses_freightname(optional): Freightname for shipping.
  * expenses_linetotal(optional): Total of the shipping cost.
  * expenses_taxcode(optional): Taxcode for shipping.
  * discount_percent(optional): Discount percentage.
  * transport_name(optional): Shipping method.
  * payment_method(optional): Payment method.
  * fe_order_id: Front end order id.
  * fe_order_id_udf(optional): Front end order id UDF.
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
  * num(optional): The amount of the records will be contained in the result.  IF not specified, only one record will be fetched.
  * columns(optional): Which columns will be in the response result.  If not specified, all columns will be used.
  * card_code: The CardCode of a business partner.
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
  * card_code(required): The CardCode of a business partner.
  * contact(required): contact{}
    - FirstName: First name.
    - LastName: Last name.
    - Tel1: Telephone.
    - E_MailL: Email.
    - Address: Address.

  Example request body:
  ```javascript
  {
    "card_code": "C20000",
    "contact": {
      "FirstName": "Joe",
      "LastName": "Brown",
      "Tel1": "(213) 345-6789",
      "E_MailL": "joe.brown@xzy.net",
      "Address": "1st st. Los Angles, CA 90089"
    }
  }
  ```

  Example response body:
  ```javascript
  {
    "contact_code": "61"
  }
  ```

  Example script by curl:
  ```bash
  curl -u admin:secret -X POST -H 'Content-Type: application/json' http://192.168.44.148:5000/v1/contact -d '{"card_code": "C20000", "contact": {"FirstName": "Joe1", "LastName": "Brown", "Tel1": "(213) 345-6789", "E_MailL": "joe.brown@xzy.net", "Address": "1st st. Los Angles, CA 90089"}}'
  ```

#### OrderCancelAPI
  ```
  POST /v1/cancelorder
  ```
  Cancel an order by B1 order number.

  Request Parameters:
  * fe_order_id_udf(optional): Front end order id UDF.
  * fe_order_id: Front end order id.

  Example request body:
  ```javascript
  {
    "fe_order_id": "000000009"
  }
  ```

  Example response body:
  ```javascript
  {
    "bo_order_id": "535"
  }
  ```

  Example script by curl:
  ```bash
  curl -u admin:secret -X POST -H 'Content-Type: application/json' http://192.168.44.148:5000/v1/cancelorder -d '{"fe_order_id": "00000002"}'
  ```

#### ShipmentsAPI
  ```
  POST /v1/shipments
  ```

  Request Parameters:
  * num(optional): The amount of the records will be contained in the result.  IF not specified, only one record will be fetched.
  * columns(optional): Which columns will be in the response result.  If not specified, all columns will be used.
  * params: The query condition parameters.
    key: The column name.
    - op(optional): The condition operator.
    - value: The condition value.
  * itemColumns(optional):

  Example request body:
  ```javascript
  {
    "num": "1",
    "columns": [ "DocDueDate", "CardName"],
    "params": {
      "DocDate": {
        "op": ">=",
        "value": "2015-01-01"
      }
    },
    "itemcolumns": ["BaseDocNum", "Price", "ShipDate"]
  }
  ```

  Example response body:
  ```javascript
  [
    {
      "items": [
        {
          "ShipDate": "2015-06-19 00:00:00",
          "BaseDocNum": "452",
          "Price": "140.000000"
        },
        {
          "ShipDate": "2015-06-19 00:00:00",
          "BaseDocNum": "452",
          "Price": "0.000000"
        }
      ],
      "DocDueDate": "2015-07-20 00:00:00",
      "DocEntry": "364",
      "CardName": "Maxi-Teq"
    }
  ]
  ```

  Example script by curl:
  ```bash
  curl -u admin:secret -X POST -H 'Content-Type: application/json' http://192.168.44.148:5000/v1/shipments -d '{"num": "1", "columns": [ "DocDueDate", "CardName"], "params": {"DocDate": {"op": ">=", "value": "2015-01-01"}}, "itemcolumns": ["BaseDocNum", "Price", "ShipDate"]}'
  ```
