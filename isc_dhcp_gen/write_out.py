import isc_dhcp_gen.syntax.dhcpd
from functools import reduce
from os import environ
from os.path import join
import ntpath
from isc_dhcp_gen.util import file_namify


def generate_syntax_for_subnet(subnet: dict):
    ipv4_str = subnet['SUBNET'].ipv4
    net_str = subnet['SUBNET'].netmask.mask
    return isc_dhcp_gen.syntax.dhcpd.SUBNET.format(
        ipv4=ipv4_str,
        netmask=net_str,
        gw=subnet['GATEWAY'],
        pool=isc_dhcp_gen.syntax.dhcpd.gen_pool(subnet).replace("\n", "\n\t"),
        area=subnet['AREA'],
        func=subnet['FUNCTION']) + '\n'


def generate_syntax_for_group(group: dict):
    return reduce(lambda x, y: x + "\n" + generate_syntax_for_subnet(y), group, "")


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
        with open(self.outfile_name_path_prefix + "index" + self.outfile_suffix, "w") as index_file:
            for k in self.files:
                for i in k:
                    with open(self.outfile_name_path_prefix + file_namify(i) + self.outfile_suffix, "w") as fh:
                        fh.write("# Automatically generated with github.com/kylelt/isc-gen")
                        fh.write(k[i])
                        index_file.write(isc_dhcp_gen.syntax.dhcpd.INCLUDE.format(absprefix="/etc/dhcp/scripts/cogcnets", fname=ntpath.basename(fh.name)))
