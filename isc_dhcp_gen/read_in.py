from pyexcel_xlsx import get_data

class DataReader:
    """ wrap pyexcel_xlsx """

    def __init__(self,file_path:str):
        self.excel_data = get_data(file_path)

    def get_data(self):
        return self.excel_data
