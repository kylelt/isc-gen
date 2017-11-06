
SUBNET = """
# {area} - {func}
subnet {ipv4} netmask {netmask} {{
    option routers {gw};\
    {pool}
}}"""

POOL = """
pool {{
   range {range};
}}
"""