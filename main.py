import sys
from isc_dhcp_gen.read_in import DataReader
from isc_dhcp_gen.transform import Transformer
from isc_dhcp_gen.write_out import DataWriter

app_props = {
    "in_file": None,
    "out_file_dir": None,
    "debug": True
}

def main(argumentVector:list):
    argv_len = len(argumentVector)
    for idx, val in enumerate(argumentVector):
        if val == '-i' and idx != argv_len -1:
            app_props["in_file"] = argumentVector[idx+1]

        if val == '-o' and idx != argv_len -1:
            app_props["out_file_dir"] = argumentVector[idx+1]

        if app_props["debug"]:
            print("ARGV[{}]: {}".format(idx, val))

    transformer = Transformer(DataReader(app_props["in_file"]).get_data())
    writer = DataWriter(transformer.get_sheets_grouped_by_area,
                        outfiles_name_prefix="subnets-",
                        outfiles_path=(app_props["out_file_dir"] if app_props["out_file_dir"] else "%USERPROFILE/Documents"))
    writer.generate_files()
    writer.write_files()

if __name__ == "__main__":
    main(sys.argv)
else:
    raise EnvironmentError("This is an entry to an application and should be used as so, not a lib file")