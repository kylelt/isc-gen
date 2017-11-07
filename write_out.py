# Write out to dhcpd.conf subnet format
from syntax.dhcpd import SUBNET, POOL
from functools import reduce
from os import environ
from os.path import join
from util import file_namify


def generate_syntax_for_subnet(subnet: dict):
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

def generate_syntax_for_group(group: dict):
    print(group)
    return reduce(lambda x, y: x + "\n" + generate_syntax_for_subnet(y), group, " # generated subnet")


class DataWriter:

    def __init__(self, data_set: dict, outfiles_name_prefix="", outfiles_path=join(environ["USERPROFILE"],"Documents")):
        self.data_set = data_set
        self.files = []
        self.outfile_name_path_prefix = join(outfiles_path,outfiles_name_prefix)
        self.outfile_suffix = ".conf"

    def generate_files(self):
        for sheet in self.data_set:
            for subnet_group in sheet:
                self.files.append({subnet_group: generate_syntax_for_group(sheet[subnet_group])})

    def write_files(self):
        for k in self.files:
            for i in k:
                with open(self.outfile_name_path_prefix + file_namify(i) + self.outfile_suffix, "w") as fh:
                    fh.write("# Automatically generated with github.com/kylelt/isc-gen")
                    fh.write(k[i])