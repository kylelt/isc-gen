# handle the vlsm data sheet as our DSL
#import re
from functools import reduce
from typing import IO
import json
from pyexcel_xlsx import get_data

class DataReader:
    # we will need this eventually
    # subnet_format = "([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})/([0-9]{1,2})"

    # Stub pattern validators

    # @staticmethod
    # def validateAddress(x:str):
    #     return True if x else False
    #
    # @staticmethod
    # def validateHostRange(x:str):
    #     return True if x else False
    #
    # @staticmethod
    # def validateBroadcastRange(x:str):
    #     return True if x else False
    #
    # @staticmethod
    # def validateClients(x:str):
    #     return True if x else False
    #
    # @staticmethod
    # def validateIsStr(x:str):
    #     return True if x else False
    #
    # validationMap = {
    #     "AREA": validateIsStr,
    #     "FUNCTION": validateIsStr,
    #     "SUBNET": validateSubnet,
    #     "HOST RANGE": validateHostRange,
    #     "BROADCAST ADDRESS": validateBroadcastRange
    # }

    # def validateData(self, rows: list):
    #     """ Show which row we don't like the data in """
    #     for i in range(len(rows)-1):
    #         if not self.validateRow(rows[i]):
    #             raise SyntaxError("Invalid DSL Syntax on line %s, %s" % (i, rows[i]))
    #
    #     return True
    #
    # def validateRow(self, rowDict: dict):
    #     return reduce(
    #         lambda x, y: x and DataReader.validationMap[y](rowDict[y]),
    #         rowDict,
    #         True)

    def __init__(self,file_path:str):
        self.excel_data = get_data(file_path)

    def get_data(self):
        print(self.excel_data)

        return self.excel_data
