# Write out to dhcpd.conf subnet format
from syntax.dhcpd import SUBNET, POOL
from functools import reduce

class DataWriter():
    def __init__(self, data_set: dict):
        self.data_set = data_set
        self.files = []

    def generate_files(self):
        for sheet in self.data_set:
            for subnet_group in sheet:
                self.files.append({subnet_group:self.generate_syntax_for_group(sheet[subnet_group])})


    def generate_syntax_for_group(self, group: dict):
        print(group)
        return reduce(lambda x, y: x + "\n" + self.generate_syntax_for_subnet(y), group, " # generated subnet")

    def generate_syntax_for_subnet(self, subnet):
        print(subnet['SUBNET'])
        ipv4_str = subnet['SUBNET'].ipv4
        net_str = subnet['SUBNET'].netmask.mask
        return SUBNET.format(
            ipv4=ipv4_str,
            netmask=net_str,
            gw=subnet["GATEWAY"],
            pool=POOL.format(range=subnet["HOST RANGE"]).replace("\n", "\n\t"),
            area=subnet["AREA"],
            func=subnet["FUNCTION"]
        ) + "\n"

    def get_files(self):

        with open('C:/users/kyle.lewer/dhcpd.conf', 'w') as fh:
            for k in self.files:
                for i in k:
                    fh.write(k[i])
