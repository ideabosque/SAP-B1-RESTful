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

## API

#### InfoAPI
  ```bash
  Get /v1/info
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
