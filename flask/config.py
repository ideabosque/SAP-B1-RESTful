import os
import logging

basedir = os.path.abspath(os.path.dirname(__file__))

LOGGING_LOCATION = 'sapb1adaptor.log'
LOGGING_LEVEL = logging.INFO
LOGGING_FORMAT = '%(asctime)s %(levelname)-8s %(message)s'

DIAPI = 'SAPbobsCOM90'
SERVER = 'SAP91'
LANGUAGE = 'ln_English'
DBSERVERTYPE = 'dst_MSSQL2014'
DBUSERNAME = 'sa'
DBPASSWORD = '************'
COMPANYDB = 'SBODEMOUS'
B1USERNAME = 'manager'
B1PASSWORD = '************'
