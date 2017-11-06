from collections import namedtuple
from functools import reduce
SubnetV4 = namedtuple("SubnetV4", ['ipv4', 'netmask'])
NetMask = namedtuple("NetMask", ["slash", "mask"])
Ipv4Pool = namedtuple("Ipv4Pool", ["first", "last"])

class Transformer:

    def __init__(self, data: list):
        self.xlsx_data = data
        self.grouped = {}
        self.__parse_sheets()


    def __parse_sheets(self):
        for sheet in self.xlsx_data:

            # fill down
            for idx, row in enumerate(self.xlsx_data[sheet]):
                if row[0] is None:
                    row[0] = self.xlsx_data[sheet][idx-1][0]
                if row[1] is None:
                    row[1] = self.xlsx_data[sheet][idx-1][1]

            self.xlsx_data[sheet] = self.__amend_data(self.xlsx_data[sheet])


    def __amend_data(self, sheet:list):
        """ Grouped rows in a column give value for the first column and null for the rest  c1 X crest"""
        sentinel = ""
        dictorized = [{sheet[0][i]: row[i] for i in range(len(row)-1)} for row in sheet[1:]]

        for idx, vals in enumerate(dictorized):
            vals["HOST RANGE"] = vals["HOST RANGE"].replace(" - ", " ")
            vals["SUBNET"] = self.__build_subnet_tuple(subnet_serialised_with_slash=vals["SUBNET"])

        [print(x) for x in dictorized]
        return dictorized


    def get_sheets_grouped_by_area(self):
        return [self.__sheet_grouped_by_area(work_sheet) for work_sheet in self.xlsx_data]

    def __sheet_grouped_by_area(self, sheet):
        # unique_groups = set([sheet[row_key]["AREA"] for row_key in sheet[1:]])
        unique_groups = set([x["AREA"] for x in self.xlsx_data[sheet]])

        data = { area_name: [sheet_row for sheet_row in self.xlsx_data[sheet] if sheet_row["AREA"] == area_name]
            for area_name in unique_groups
                 }
        return data


    def __build_subnet_tuple(self, subnet_serialised_with_slash=None, subnet_serialised_with_netmask=None):
        if None == subnet_serialised_with_slash and None == subnet_serialised_with_netmask:
            raise ValueError("Expecting at least one netmask notation")

        if subnet_serialised_with_slash:
            ipv4, suffix = subnet_serialised_with_slash.split('/')
            # Convert the slash to 255.255.255.255 notation
            netmask = '.'.join(["255" for i in range(int(int(suffix)/8))])\
                      + ('' if (int(suffix) / 8 == 4) else '.' + str(255 - (pow(2, 8 - int(suffix) % 8)-1)))
            # if we haven't built a full netmask complete with .0's as necessay
            netmask = reduce(lambda x, y: x + '.0', range(3-netmask.count('.')), netmask)
            return SubnetV4._make((ipv4, NetMask._make((suffix, netmask))))

        if subnet_serialised_with_netmask:
            raise NotImplementedError("We don't support from nm to slash yet, fork me and fix it")