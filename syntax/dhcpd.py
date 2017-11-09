
SUBNET = \
"""
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
}}"""
# --------------------
POOL = """\tpool {{
\trange {range};
}}"""
# --------------------
FAILOVER = """failover peer "{relationship_name};" """

gen_pool = lambda x: \
    just_pool(x) \
    if "DHCP FAILOVER PAIR" not in x or x["DHCP FAILOVER PAIR"] is None \
    else pool_w_failover(x)


# I am writing range=x[HOST RANGE] more than once i should internalise the optional to just_pool somehow
just_pool = lambda x: POOL.format(range=x["HOST RANGE"])
pool_w_failover = lambda x: POOL_F.format(range=x["HOST RANGE"], failover=FAILOVER.format(relationship_name=x["DHCP FAILOVER PAIR"]))