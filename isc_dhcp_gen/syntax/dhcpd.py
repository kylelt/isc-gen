
SUBNET = \
"""
# Subnet Description
# {area} - {func}
subnet {ipv4} netmask {netmask} {{
\toption routers {gw};
{pool}
}}"""
# --------------------
POOL_F = \
"""\tpool {{
\trange {range};
\t{failover}
\t{unknown}
}}"""
# --------------------
POOL = """\tpool {{
\trange {range};
\t{unknown}
}}"""
UNKNOWN_CLIENTS ="{deny} unknown-clients;"

INCLUDE = """include "{absprefix}/{fname}";
"""
# --------------------
FAILOVER = """failover peer "{relationship_name};" """

gen_pool = lambda x: \
    just_pool(x) \
    if "DHCP FAILOVER PAIR" not in x or x["DHCP FAILOVER PAIR"] is None \
    else pool_w_failover(x)


# I am writing range=x[HOST RANGE] more than once i should internalise the optional to just_pool somehow
unknown_clients = lambda x: "" \
    if "ALLOW UNKNOWN HOSTS" not in x\
    or x["ALLOW UNKNOWN HOSTS"] is None\
    else UNKNOWN_CLIENTS.format(deny="deny" if x["ALLOW UNKNOWN HOSTS"] is "N" else "allow")
just_pool = lambda x: POOL.format(range=x["HOST RANGE"], unknown=unknown_clients(x))
pool_w_failover = lambda x: POOL_F.format(range=x["HOST RANGE"],
                                          failover=FAILOVER.format(relationship_name=x["DHCP FAILOVER PAIR"]),
                                          unknown=unknown_clients(x))